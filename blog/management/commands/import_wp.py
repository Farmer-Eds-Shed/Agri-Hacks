import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup, Comment
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from cloudinary.uploader import upload as cloudinary_upload
from blog.models import Post, Category

NS = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/',
}


class Command(BaseCommand):
    help = 'Import WordPress posts from an exported XML file'

    def add_arguments(self, parser):
        parser.add_argument('xml_path', type=str, help='Path to WordPress export XML file')
        parser.add_argument('--author', type=str, default='admin', help='Username of the author to assign')

    def handle(self, *args, **options):
        xml_path = options['xml_path']
        author_username = options['author']
        author = User.objects.get(username=author_username)

        tree = ET.parse(xml_path)
        root = tree.getroot()
        count = 0

        for item in root.findall('./channel/item'):
            post_type = item.find('wp:post_type', NS).text
            status = item.find('wp:status', NS).text

            if post_type != 'post' or status != 'publish':
                continue

            title = item.find('title').text or 'Untitled'
            raw_content = item.find('content:encoded', NS).text or ''
            pub_date = item.find('wp:post_date', NS).text
            published_at = make_aware(parse_datetime(pub_date))

            soup = BeautifulSoup(raw_content, 'html.parser')

            # Find first image and upload to Cloudinary
            first_img_tag = soup.find('img')
            featured_image_url = 'placeholder'
            if first_img_tag and first_img_tag.get('src'):
                try:
                    upload_result = cloudinary_upload(first_img_tag['src'])
                    featured_image_url = upload_result.get('public_id')
                except Exception as e:
                    self.stderr.write(f"⚠️  Image upload failed for '{title}': {e}")

            # Strip all images in body and replace with placeholders
            for img in soup.find_all('img'):
                placeholder = soup.new_tag('p')
                placeholder['class'] = 'image-placeholder'
                placeholder.string = '[Image removed — hosted externally]'
                img.replace_with(placeholder)

            # Remove WP comment wrappers
            for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
                if 'wp:code' in comment:
                    comment.extract()

            # Find both <p> and <pre> blocks to keep code
            content_blocks = soup.find_all(['p', 'pre'])

            concept = str(content_blocks[0]) if content_blocks else ''
            document = ''.join(str(el) for el in content_blocks[1:]) if len(content_blocks) > 1 else ''

            # Handle category
            category_obj = None
            for cat in item.findall('category'):
                if cat.attrib.get('domain') == 'category':
                    category_name = cat.text.strip()
                    category_obj, _ = Category.objects.get_or_create(name=category_name)
                    break

            # Create post
            post = Post.objects.create(
                title=title,
                author=author,
                featured_image=featured_image_url,
                concept=concept,
                document=document,
                created_on=published_at,
                status=1,
                category=category_obj
            )

            count += 1
            self.stdout.write(f"✅ Imported: {title}")

        self.stdout.write(self.style.SUCCESS(f"\n🎉 {count} posts imported successfully."))

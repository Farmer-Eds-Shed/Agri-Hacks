# Agri-Hacks


A blog site for sharing Agriculture related hacks. Code Institute Portfolio 4 Assessment
#### - By FarmerEd


![am I responsive screenshot](static/images/readme_img/Agri-Hacks-responsive.png)
### **[Live Site:](https://agri-hacks-60be548e369f.herokuapp.com/)** <br>
### [Repository:](https://github.com/Farmer-Eds-Shed/Agri-Hacks/)

---
## Table of contents
<a name="contents">Back to Top</a>
 1. [ User Experience UX ](#ux)
 1. [Agile Development](#agile)
 1. [ Features ](#features)   
 1. [ Technology used ](#tech) 
 1. [ Testing ](#testing)  
 1. [ Bugs ](#bugs)  
 1. [ Deployment](#deployment)
 1. [ Credits](#credits)
 1. [ Content](#content)   



## User Experience UX
<a name="ux"></a>
A visitor to Agri-Hacks would be a farmer looking to share their on farm innovation and labour saving hacks or a farmer simply looking for insperation for projects to use on their own farms. All types of farm enterprises are welcome from back yard farmers to the largest enterprises.

### User Stories

#### Epic | Registration
- As a Site User I can register an account so that I can comment on and create new blog posts.
- As a Site Admin I can manage user accounts.

#### Epic | Categories
- As a site user I can group my posts so that other users can browse and filter similar content.
- As a User I can search so that I can easily find blogs of interest.
- As a site user, I can view a paginated list of posts so that I can select which post I want to view.
- As a Site Admin I can add/remove categories.

#### Epic | Functioning Blog CRUD
- As a Site User, I can click on a post so that I can read the full text.
- As a Site User I can create, read, update and delete my own posts so that I can manage my blog content.
- As a Site User I can create draft posts so that I can finish writing the content later.
- As a Site User I can see all post I created so that I can manage and track comments on past posts.
- As a Site User I can Upload Cover images so that I can showcase my blog.
- As a Site Admin I can create, read, update and delete posts so that I can moderate content.

#### Epic | Post Ranking
- As a Site User I can like blog posts so that popular posts can be ranked.
- As a Site User I can mark which blog posts I've made so that users can see what's being made.

#### Epic | About Page
- As a site user I can find an about page so that I can learn about the Site and provide feedback.
- As a Site User I can fill in a form so that I can provide feedback / report issues.
- As a Site Admin I can review/manage feedback so that I can review issues and general feedback on the site.
- As a Site Admin I can add/remove issue categories so that I can sort feedback.

#### Epic | Comments
- As a Site User I can view comments on an individual post so that I can read the conversation.
- As a Site User I can leave comments on a post so that I can be involved in the conversation.
- As a Site Admin I can create, read, update and delete posts so that I can moderate content.

#### User stories not yet implemented
The following user stories were scoped out of the project due to time constraints and labelled as "Won't Have Now" on the project board on Github. It is intended that these user stories will be implemented later.

- As a site user I can manage my own account so that I can update profile info/ passwords.
- As a Site User I can sort posts by popularity so that I can find the best projects.




### PLanning
- Database Structure

  ![ERD Diagram](static/images/readme_img/Agri-Hacks-ERD.png)

- Database Schema
    - #### Category Model

        | id | Field |
        |--|--|
        |name|TextField
        |slug|SlugField

    - #### Post Model

        | id | Field |
        |--|--|
        |title |Charfield|
        |category |ForeignKey|
        |author|ForeignKey|
        |featured_image|CloudinaryField|
        |concept|TextField|
        |document|TextField|
        |created_on|DateTimeField|
        |Status|IntegerField|
        |updated_on|DateTimeField
        |Likes|ManyToManyField
        |made_one|ManyToMany

    - #### Comment Model

        | id | Field
        |--|--|
        |post|ForeignKey
        |Author|ForeignKey
        |body|TextField
        |created_on|DateTimeField
        |updated_on|DateTimeField

    - #### About Model

        | id | Field
        |--|--|   
        |title|CharField
        |updated_on|DateTimeField
        |content|TextField
        |order|IntegerField
        |status|IntegerField

    - #### Issues Model

        | id | Field
        |--|--| 
        |name|CharField
        |slug|SlugField

    - #### Feedback Model

        | id | Field
        |--|--| 
        |issue|ForeignKey
        |name|CharField
        |email|EmailField
        |message|TextField
        |read|BooleanField

## Agile Development


## Features


<a name="tech"></a>
##  Technology Used

### Html

 - Used to structure webpages and the base templating language

### CSS

 - Custom CSS used to style the pages and give the site an agri theme.

### JavaScript

 -  Used to add 

### Python

 -  Used for the logic in this project.

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

### Font Awesome

 -  Icon library used for Iconss on links and like buttons.

### Bootstrap 5
 - Used as the base front end framework to work alongside Django

### Jinja Templating with Django
 - Used to render logic within html documents and make the website more dynamic.

### GitHub
 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku
- Used to host and deploy this project

### Heroku PostgreSQL
-Heroku PostgreSQL was used as the database for this project during development and in production.

### Cloudinary
- Used to host the static files for this project including blog cover pictures.

### Git
- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

[Back to Top of page](#contents)

---

## Testing

## Bugs

## Deployment

## Credits
- © Ronyzmbow | <a href="https://www.stockfreeimages.com/">Stock Free Images</a>

## Content
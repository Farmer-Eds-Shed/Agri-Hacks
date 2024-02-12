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

[Back to Top of page](#contents)

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

[Back to Top of page](#contents)

## Agile Development

<a name="agile"></a>

This project was developed following the priciples of Agile Development, GitHub Projects and Milestones were used to track planning and progress. <br>

User stories were created as Issues and assigned to a Milestone(Epic), progress was tracked via the projects board. Each user story was given an acceptance criteria to clearly define when it was completed. <br>

As User Stories were worked on they were moved into the "In Progress" section of the Project board, when a user story matched its acceptance criteria it was closed and moved the  "Done" section. When new features were decided upon after the initial project planning they were also added to the "To Do" Section. 

[Back to Top of page](#contents)



## Features

<a name="features"></a>

#### User based Features Implemented:

- **Users can** create an account **(Create)**
- **Users can** log into their account
- **Users can** log out of their account
- **Users can** create a blog post **(Create)**
- **Users can** read a blog post **(Read)**
- **Users can** edit their own posts **(Update)**
- **Users can** delete their own posts **(Delete)**
- **Users can** leave comments **(Create)**
- **Users can** read all comments **(Read)**
- **Users can** edit their own comments **(Update)**
- **Users can** delete their own comments **(Delete)**
- **Users can** like / unlike posts **(Update)**
- **Users can** mark / unmark projects they will/have made **(Update)**
- **Users can** read About page **(Read)**
- **Users can** contact site admins by contact form **(create)** 

#### Admin based features Implemented:

- **Admins can** moderate posts **(CRUD)**
- **Admins can** moderate comments **(CRUD)**
- **Admins can** Add / Remove Post Categories **(CRUD)**
- **Admins can** Review feedback **(CRUD)**
- **Admins can** Create new / update feedback issue categories **(CRUD)**
- **Adnins can** Manage User Accounts **(CRUD)**
- **Admins can** Maintain the About Page **(CRUD)**


#### Account restrictions:

- **Users connot** edit any other users posts
- **Users cannot** edit any other users comments
- **Users cannot** like/made_this the same post more than once
- **Users cannot** access the admin panel 


[Back to Top of page](#contents)

##  Technology Used

<a name="tech"></a>

### Html

 - Used to structure webpages and the base templating language

### CSS

 - Custom CSS used to style the pages and give the site an agri theme.

### JavaScript

 -  Used to add comments CRUD functionality, like / made_this functions and to activate Bootstrap dopdown menus. 

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

### HTMX
 - Used for Like / Made_this functionality, to avoid page refresh on click.

### GitHub
 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku
- Used to host and deploy this project

### Elephant PostgreSQL
-Heroku PostgreSQL was used as the database for this project during development and in production.

### Cloudinary
- Used to host the static files for this project including blog cover pictures.

### Git
- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

[Back to Top of page](#contents)

---

## Testing

Manual testing was used through out the project development. Reults of the final testing phase are shown below.


## Bugs

## Deployment

## Credits
- © Ronyzmbow | <a href="https://www.stockfreeimages.com/">Stock Free Images</a>

## Content
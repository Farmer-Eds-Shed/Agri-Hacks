# Agri-Hacks


A blog site for sharing Agriculture related hacks. Code Institute Portfolio 4 Assessment
#### - By FarmerEd


![am I responsive screenshot](static/images/readme_img/Agri-Hacks-responsive.png)
### **[Live Site:](https://agri-hacks-60be548e369f.herokuapp.com/)** <br>
### [Repository:](https://github.com/Farmer-Eds-Shed/Agri-Hacks/)

---
## Table of contents
<a name="contents">Back to Top</a>
 1. [ UX ](#ux)
 1. [Agile Development](#agile)
 1. [ Features ](#features)   
 1. [ Technology used ](#tech) 
 1. [ Testing ](#testing)  
 1. [ Bugs ](#bugs)  
 1. [ Deployment](#deployment)
 1. [ Credits](#credits)
 1. [ Content](#content)   



## UX
<a name="ux"></a>
PLanning
- Database Structure
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
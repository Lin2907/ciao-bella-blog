# Ciao Bella Blog



### Overview
Ciao Bella Blog is a Django-based web application that offers a modern and user-friendly platform for cosmetic tips and products.
<br>
It includes a homepage with an about section, restaurant recommendation, a product gallery, and an entertaining quiz. 

Additionally, the blog features skincare and product articles , allowing users to read, comment, like, and interact with the content once logged in.

Responsivness images

Live Site can be found [here.](https://ciao-bella-blog-52e670d348e8.herokuapp.com/)

## Table of Contents
### User Experience
### Design
### Wireframes
### Database Design
### Features
### Languages and Technologies
### Packages
### Tools and Programs Used
### Testing
### Code Validation
### Manual Testing
### Deployment
### Content
### Credits


## User Experience

### User Stories

  + As a User I can browse the blog and read articles without signing in so that I can explore content freely
  + As a User I can see a clear option to sign up for an account so that I can access additional features of the blog like commenting and liking articles
  + As a logged in User I can leave comments on a post so that I can share my thoughts and engage with other users.
  + As a Site User / Admin I can view comments on an individual post so that I can read the conversation.
  + As a logged in User I can edit or delete my comments so that I can be involved in the conversation.
  + As a Site User I can like the articles so that I can show appreciation for content that I enjoy.


### Site Admin
  + As a Site Admin I can create, read, update and delete posts so that I can manage my blog content .

## Design

### Color Scheme

#### Primary Colors
  + Dark Washed Rose: `rgb(214, 10, 112)`
  + White 

  <img src = "static/md-images/main-color.png" alt= "Color used">

## Wireframes

### Desktop

Home Page <br>
<img src= "static/md-images/landing-page.png" alt="Home page"> <br>
Blog Page <br>
<img src= "static/md-images/stories-page.png" alt="Blog posts page"> <br>
Register Page <br>
<img src= "static/md-images/register-page.png" alt="Register page"> <br>
Log in Page <br>
<img src= "static/md-images/log-in-page.png" alt="Log in page"> <br>
404 Error page <br>
<img src= "static/md-images/404-page.png" alt="Error 404 page"> <br>

### Mobile

Home Page <br>
<img src= "static/md-images/landing-mobile.png" alt="Home mobile page"> <br>
Blog Page <br>
<img src= "static/md-images/posts-page.png" alt="Blog posts mobile page"> <br>
Register Page <br>
<img src= "static/md-images/comment-page.png" alt="Detailed post and comment mobile page"> <br>
Log in Page <br>
<img src= "static/md-images/500-page.png" alt="Server error page"> <br>
404 Error page <br>
<img src= "static/md-images/404-mobile.png" alt="Error 404 page"> <br>






### Typography



## Database Design
ERD - Entity Relationship Diagram


### Models


## Agile Development

### Project Board

<img src = "static/md-images /project-board.png" alt = "Project Board">


## To easily group my User Stories into a more structured format I created following Epics:

  + Initial Set Up


  + UX Design


  + User Experience

  + User Authentication


  + Documentation
This Epic was used to keep track of what was needed for creating and planning the README.

MoSCoW


Kanban

## Features
 ### Navbar
  + The navbar was created using Bootstrap 5 in order to ensure it would be responsive across various viewports. 
  + When a user is not signed in the navbar will display the following:

     * Home
     * Skincare
     * Register
     * Log in

  + When the user is signed in the following is instead displayed:

     * Home
     * Skincare
     * Log out


Logged in


Mobile non-expanded


Mobile expanded


Footer



Home Page







Blog List Page



Search post 




Post Details Page




Comments





Sign Up
From here if the user does not have an account they may register their account.



Log In



Log Out




## Languages and Technologies

HTML was used for the markup and templating.
Django as the web framework.
Python was used for all backend work.
CSS was used to style the site.
JavaScript and JQuery were used for managing random products gallery on home page.
Bootstrap 5 was used throughout some elements for a responsive framekwork.

## Packages
The following packages were installed throughout the development.

crispy-bootsrap5	This package was used to create a reusable DRY approach to forms.
Django-allAuth	This package was used to provide templates, views and models necessary for user authentication.
Summernote was used to allow for a more creative approach when posting to the database through a custom model. Text fields can now have various font and layout styling added to them.
Whitenoise	was used to allow the app to serve it's own static files which would be needed for deployment.

## Tools and Programs Used
GitPod was used as the main IDE for the project.
Git was used for version control.
GitHub for hosting my repository.
Heroku was used for deployment.
FontAwesome for providing all icons used throughout the site.
ERDplus for creating the database ERD.
AmIResponsive for creating the README header image.
Favicon.io for creating a favicon.
Figma for creating the wireframes.
Testing
Code Validation
Lighthouse
All of the pages for this project were tested using Google-Lighthouse.

## Home Page


## Blog post List


## Post Detail


## Sign up


## Sign In

# Validation

## CSS Validation
For CSS validation W3C-CSS-Validation was used.



## HTML Validation
HTML markup was validated using W3C-HTML

# JavaScript Validation
JSHINT was used to validate the comment script.

# Python Validation
All of the Python files were validated using PEP8 with CI-Python-Linter

# Manual Testing (need to do a separate file)
Full testing of the functionality of the site was done on the following devices:

Laptop Used : Samsung Galaxy Book2 Pro 360 Notebook
Mobile : iPhone 11

The following browsers were used to test the functionality of the site.

  + Microsoft Edge , Safari

# Ciao Bella Blog



### Overview
Ciao Bella Blog is a Django-based web application that offers a modern and user-friendly platform for cosmetic tips and products.
<br>
It includes a homepage with an about section, restaurant recommendation, a product gallery, and an entertaining quiz. 

Additionally, the blog features skincare and product articles , allowing users to read, comment, like, and interact with the content once logged in.

<img src = "static/md-images/responsive-design.png" alt= "Mockup for responsivness"> 


Live Site can be found [here.](https://ciao-bella-blog-52e670d348e8.herokuapp.com/)

## Table of Contents
- [User Experience](#user-experience)
- [Design](#design)
- [Wireframes](#wireframes)
- [Database Design](#database-design)
- [Features](#features)
 -[Features left to implement](#features-left-to-implement)
- [Languages and Technologies](#languages-and-technologies)
- [Packages](#packages)
- [Tools and Programs Used](#tools-and-programs-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Content](#content)
- [Credits](#credits)


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
Blog detail and comment Page <br>
<img src= "static/md-images/comment-page.png" alt="Detailed post and comment mobile page"> <br>
Server error Page <br>
<img src= "static/md-images/500-page.png" alt="Server error page"> <br>
404 Error page <br>
<img src= "static/md-images/404-mobile.png" alt="Error 404 page"> <br>

### Typography

Font used : Dancing Script - gives feminine elegance with its cursive strokes adding a touch of charm and sophistication. 

<img src="static/md-images/dancing-script.png" alt="Font image">


## Database Design
ERD - Entity Relationship Diagram

<img src="static/md-images/erd.png" alt="Entity Relationship Diagram">

### Models

#### Blog Post Model

The blog post model is the central model for the entire application. <br>
Each blog post features essential details like the title, author, content, published date, and a featured image. <br>
Additionally, posts can include optional attributes: ingredients, how to use, and benefits.

#### User Model
The User model is Django's built model,used for authentication purposes.


#### Comment Model

The Comment model is used to store all of the comments created by the users. It is linked to the Blog Post model so that the comments are correctly aligned with the related blog post.

#### Liked post Model

The Liked post model has the purpose of adding a like feature to the posts, where User can express their preferences by liking or unliking blog posts.

## Agile Development

### Project Board

<img src = "static/md-images/project-board.png" alt = "Project Board">

  + MoSCoW

For this project the MoSCoW technique, (Must have, Should have, Could have, Won't have) was essential for planning out the User Stories. 


  + Kanban

To help visualise the project and plan accordingly with a schedule the Kanban system is used - implemented through GitHub Projects.

## Features

 ### Navbar

  + The navbar is created using Bootstrap 5 in order to ensure it would be responsive across various viewports. 

   + When a user is not signed in the navbar will display the following:

  <img src = "static/md-images/navbar.png" alt= "Navigation">

  + When the user is signed in the following is instead displayed:

  <img src = "static/md-images/navbar-logged.png" alt= "Navigation bar user logged in">


   + Navbar Mobile expanded
  
  <img src = "static/md-images/mobile-expanded.png" alt= "Navigation bar mobile">



### Footer

The footer for this application is containing links to various social media platforms, the navigation and search option.

<img src = "static/md-images/footer.png" alt= "Footer">

### Home Page

#### Landing page hero image 

<img src = "static/md-images/landing-image.png" alt= "Home page">

#### About me Section

<img src = "static/md-images/about-me.png" alt= "About me"> 

#### Gallery Section

The gallery showcases a random selection of images  that highlight the topic of blog posts.

<img src = "static/md-images/gallery.png" alt= "Gallery"> 

### Blog Page - Skincare

The blog posts page includes search option making it simple for User to find and explore content. <br>

<img src = "static/md-images/blog-posts.png" alt= "Blog post"> 

For better user experience and readability , the posts are spread on more then one page (pagination included). <br>

<img src = "static/md-images/pagination.png" alt= "Pagination"> 

### Post Details Page

<img src = "static/md-images/post-detail.png" alt= "Detailed blog post"> 

#### Comments Section

<img src = "static/md-images/comment-section.png" alt= "Comments"> 

#### Like post 

<img src = "static/md-images/likes.png" alt= "Like count"> 

#### Optional attributes

<img src = "static/md-images/optional-attributes.png" alt= "Post optional text"> 

### Sign Up
From here if the user does not have an account they may register their account.

<img src = "static/md-images/register.png" alt= "Register account"> 

### Log In
<img src = "static/md-images/log-in.png" alt= "Login"> 

### Log Out

<img src = "static/md-images/sign-out.png" alt= "Sign out"> 

### Custom 404 error page

<img src = "static/md-images/404-custom-page.png" alt= "404 custom error page"> 

## Features left to implement

+ Report Inappropriate Comments or Content: Enable users to flag comments or posts they find inappropriate for review.
+ User-Posted Images: Allow users to upload images in their blog posts and comments.
+ Modify Username or Password: Provide functionality for users to update their username and change their password.
+ Reset Password: Implement a password reset feature for users who have forgotten their login credentials.


## Languages and Technologies

+ HTML was used for the markup and templating.
+ Django as the web framework.
+ Python was used for all backend work.
+ CSS was used to style the site.
+ JavaScript and JQuery were used for managing random products gallery on home page and updating comments.
+ Bootstrap 5 was used throughout some elements for a responsive framework.

## Packages

The following packages were installed throughout the development:

+ Crispy-bootstrap5	- This package was used to create a reusable DRY approach to forms. 
+ Django-allAuth  - This package was used to provide templates, views and models necessary for user authentication. 
+ Summernote  - This was used to allow for a more creative approach when posting to the database through a custom model <br> so the text fields can have various font and layout styling added to them. 
+ Whitenoise- This was used to allow the app to serve it's own static files needed for deployment.

## Tools and Programs Used
+ [GitPod](https://gitpod.io/workspaces) was used as the main IDE for the project. 
+ [GitHub](https://github.com/) for hosting the repository.
+ [Heroku](https://id.heroku.com/login) was used for deployment.
+ [FontAwesome](https://fontawesome.com/) for providing all icons used throughout the site.
+ [Smartdraw](https://app.smartdraw.com/editor.aspx?credID=-61278721&depoId=55466879&flags=128) for creating the database ERD.
+ [Techsini.com](https://techsini.com/multi-mockup/index.php) for creating the README mockup image.
+ [Favicon.io](https://favicon.io/) for creating a favicon.
+ [Figma](https://www.figma.com/) and [Balsamiq](https://balsamiq.com/) for creating the wireframes.

## Testing 
 + This section can be found under Testing.md

## Deployment

For this project the application was deployed to Heroku using the following steps:

 + Log into Heroku account and navigate to the dashboard. Click on 'New' to create a new app. Set region to EU, click on 'Create app'.
 + In the 'Settings' tab in 'Reveal Config Vars' add the  environment variables for the Database, Secret Key and CollecStatic.
 + Navigate to the 'Deploy' tab and under 'Deployment Method' click on 'GitHub'.
 + Locate the repository from GitHub, paste the link and click 'Connect'.
 + Ensure that the selected branch is 'main branch' before clicking to Deploy.
 + Once the build is finished there should be a message saying 'Your app was successfully deployed' with a 'View' button.

## Forking the repository
In order to fork the repository to make a copy the steps are:

+ Log into GitHub and locate the repository for https://github.com/Lin2907/ciao-bella-blog
+ At the top of the repository above settings locate the 'Fork' button There is now a copy of the repository in the Github account

## Cloning the repository
+ On GitHub navigate to the main page of the repository
+ Above the list of files click the dropdown code menu
+ Select the https option and copy the link
+ Open the GitPod Bash terminal
+ Change the current working directory to the desired destination location
+ Type the git clone command with the copied URL.
+ Press enter to create the local clone

## Credits
  ### Content
 + Images were taken from Pixabey and [Pexels](https://www.pexels.com/).
 + Blog posts were generated with Chat Gpt.
 + Django and Bootstrap official Documentation, W3 Schools, Code Institute Walkthrough Project.
 
 I would like to say special thanks to my mentor Mitko for helping and supporting me througough this and all previous projects.

Enjoy !!!

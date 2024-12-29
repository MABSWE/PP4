# CATABLOG - A Community Blog Platform

![Project Mockup](static/img/mockup.png)

### Live Link:

💻 [CATABLOG](LINK)

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [User Stories](#user-stories)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Validation](#validation)
- [Testing](#testing)
- [Database](#database)
- [Wireframes](#wireframes)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

---

## About the Project

CATABLOG is a full-stack web application designed as a blogging platform for cat lovers. Users can browse blog posts, leave comments, and create their own posts with images. The application demonstrates modern web development practices with user authentication and role-based permissions.

## Features

- User authentication (register, login, and logout).
- Create, edit, and delete posts (authenticated users only).
- Comment system with edit and delete options for the comment owner.
- Responsive design for desktop and mobile devices.
- Contact form with validation and success confirmation.

## User Stories

### As a Visitor

1. **Home Page**: I want to access a welcoming homepage that provides an overview of the application's functionality.
2. **Blog**: I want to view a list of all published blog posts so that I can easily find articles of interest.
3. **Read Article**: I want to click on a blog post to read its full content along with any associated comments.
4. **About Page**: I want to read more about the application and its purpose on a dedicated information page.
5. **Contact**: I want to fill out a contact form to send messages or inquiries to the application's administrator.
6. **Contact Confirmation**: I want to see a success message after submitting a contact form so that I know my message has been received.

### As a Registered User

1. **Create Post**: I want to create new blog posts and upload images to share my thoughts with others.
2. **Comment**: I want to add comments to a blog post to participate in discussions.
3. **Edit Comment**: I want to edit my own comments to correct mistakes or update my thoughts.
4. **Delete Comment**: I want to delete my own comments if I no longer want them to be visible.
5. **Authentication**: I want to register an account and log in to access personalized functionality.
6. **Logout**: I want to log out of my account securely after using the application.

### As an Administrator

1. **Role Management**: I want to manage user roles and permissions to ensure only authorized users access restricted functionality.
2. **Moderation**: I want to oversee and manage content such as blog posts and comments to maintain quality and security.

## Technologies Used

### Front-End

- HTML5
- CSS3
- Bootstrap

### Back-End

- Python 3
- Django Framework

### Database

- SQLite (Development)

### Others

- Git and GitHub (Version control)
- Render (Deployment)

## Validation

### HTML Validation

W3C was used for validating html code

## Validation

### HTML Validation

W3C was used for validating html code

<details>
  <summary>home.html</summary>
  <img src="blog/static/images/validation/about_valid.png" alt="home.html Validation">
</details>
<hr>
<details>
  <summary>about.html</summary>
  <img src="blog/static/images/validation/about_valid.png" alt="about.html Validation">
</details>
<hr>
<details>
  <summary>base.html</summary>
  <img src="blog/static/images/validation/base_valid.png" alt="base.html Validation">
</details>
<hr>
<details>
  <summary>blog.html</summary>
  <img src="blog/static/images/validation/blog_valid.png" alt="blog.html Validation">
</details>
<hr>
<details>
  <summary>contact.html</summary>
  <img src="blog/static/images/validation/contact_valid.png" alt="contact.html Validation">
</details>
<hr>
<details>
  <summary>detail_view.html</summary>
  <img src="blog/static/images/validation/detail_valid.png" alt="detail_view.html Validation">
</details>
<hr>
<details>
  <summary>login.html</summary>
  <img src="blog/static/images/validation/login_valid.png" alt="login.html Validation">
</details>
<hr>
<details>
  <summary>register.html</summary>
  <img src="blog/static/images/validation/register_valid.png" alt="register.html Validation">
</details>
<hr>
<details>
  <summary>delete.html</summary>
  <img src="blog/static/images/validation/delete_valid.png" alt="delete.html Validation">
</details>
<hr>
<details>
  <summary>edit.html</summary>
  <img src="blog/static/images/validation/edit_valid.png" alt="edit.html Validation">
</details>
<hr>

##### Back to [top](#table-of-contents)<hr>

### CSS Validation

The W3C Jigsaw CSS Validation Service

<details><summary>style.css</summary>
  <img src="blog/static/images/validation/css_valid.png" alt="Base.css image"></a>
</details><hr>

### PEP8 Validation

Service was used to check the Python code. To ensure that all Python code adheres to the PEP 8 style guide, the following steps were:

<details><summary>Running pycodestyle .</summary><img src="read_img/pep8_1.png" alt="Pep8 image 1">
  <img src="read_img/pep8_2.png" alt="Pep8 image 2"></details><hr>
<details><summary>Running autopep8 --in-place --aggressive --aggressive **/*.py</summary><img src="read_img/pep8_3.png"></details><hr>
<details><summary>Manual fix</summary><img src="read_img/pep8_4.png"></details><hr>

##### Back to [top](#table-of-contents)<hr>

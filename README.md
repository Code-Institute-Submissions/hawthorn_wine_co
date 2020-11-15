## Introduction

Milestone Project 4: Full-Stack Frameworks with Django - Code Institute

The Hawthorn Wine Co. is a Full-Stack webpage for a real-life business opening in early 2021.
The main purpose is to offer an online store selling imported wines.
The site will also function to build the brand's identity and to incorporate the business owners desired colour schemes, logos, fonts etc. as well as links to their social media.
My main purpose when creating the webpage was to ensure that the site provided a pleasant and uncomplicated user experience allowing the user to access the appropriate information and make a purchase hassle free.

Click the link below to run my project in the live environment:

[Hawthorn Wine Co.](https://.herokuapp.com/)

## Table of Contents
>- [UX](#ux)
>  * [Goals](#goals)
>    + [Business Goals](#business-goals)
>  * [User Stories](#user-stories)
>  * [Wireframes](#wireframes)
>  * [Design Choices](#design-choices)
>    + [Color Choice](#color-choice)
>    + [Typography](#typography)
>      - [Title Font](#title-font)
>      - [Base Font](#base-font)
>    + [Image Choice](#image-choice)
>      - [Service Levels](#service-levels)
>    + [Design Elements](#design-elements)
>- [Features](#features)
>  * [Implemented Features](#implemente
>- [Technologies Used](#technologies-used)
>  * [Programming Languages](#programming-languages)
>  * [Framework & Extensions](#framework--extensions)
>  * [Fonts](#fonts)
>  * [Tools](#tools)
>  * [APIs](#apis)
>- [Defensive Programming](#defensive-programming)
>  * [Additional Security Checks](#additional-security-checks)
>  * [Custom Validation](#custom-validation)
>- [Testing](#testing)
>- [Deployment](#deployment)
>  * [Requirements](#requirements)
>  * [Local](#local)
>  * [Heroku](#heroku)
>- [Credits](#credits)
>  * [Content](#content)
>  * [Media](#media)
>  * [Acknowledgements](#acknowledgements)
>    

### Project Purpose 

  **Build a book review and recommendation site**

1. External user’s goal:
   -Find wines to purchase
   -Join Wine Club

2. Site owner's goal:
   -Sell Wines
   -Build brand aesthetic
   -Create a database of customers


## User Experience (UX)

-   ### User stories

    -   #### Viewing and Navigation

        1. As a Shopper, I want to be able to easily be able to navigate throughout the site to find wines and then select for purchase.
        2. As a Shopper, I want to be able to view individual wine details so that I can identify the price, description, and all necessary details.
        3. As a Shopper, I want to easily view the total of my purchases at any time so as to avoid spending too much.

    -   #### Registration and User Accounts

        4. As a Site User, I want to easily register for a personal account and be able to view my profile.
        5. As a Site User, I want to easily login or logout to access my personla information.
        6. As a Site User, I want to be able to recover my password if forgotten to regain access to my account.
        7. As a Site User, I want to be able to recover my password if forgotten to regain access to my account.
        8. As a Site User, I want to receive an email confirmation agter registering and to verify that my account registration was sucessful.
        8. As a Site User, I want to be have a personalised user profile to that I can view my personal order history and save payment information.

     -   #### Sorting and Searching
      9. As a Shopper, I want to be able to easily sort the list of available wines by type, price, country etc.
      10. As a Shopper, I want to be able to search for a product by name or description and find a specific product I would like to purchase.
      11. As a Shopper, I want to be able to easily see what I've searched for and the number of results so I can quickly see if the product is available.


     -   #### Purchasing and Checkout
     12. As a Shopper, I want to easily select the quantity of a product when I select it.




-   ### Design
    -   #### Colour Scheme
        -   The three main colours used throughout the site are  and black, with also used
        -   The site's colour scheme and styling was based on the Owner's request that the site have an independent feel to reflect the business type.  I picked an artistic style font giving a hand-drawn feel for the Main-Logo font to achieve this ideal.
    -   #### Typography
        -   Clean, modern and minimalist.
    -   #### Imagery
        -   The main image for the site is a large,background hero image.
        -   The .

*   ### Wireframes
    -   I drew the Wireframes for this project as I find drawing them allows for more detailed notes as well as being a more efficient     use of time.

    -   Home Page Wireframe - [View](https://github.com/jmurrii/MS3/)

    -   Mobile Wireframe - [View](https://github.com/jmurrii/)

    -   Products Page Wireframe - [View](https://github.com/jmurrii/)

    -   Browse Page Wireframe - [View](https://github.com/jmurrii/)

## Features

-   Responsive on all device sizes.

-   Submit, Edit and Delete operations to manage book recommendations.

-   About page with link to article which inspired the project plus clear instructions on how to proceed.

### Future Features 

 # Login System
- A User Login System would open up the possibility of users being able to login and edit their uploads securely.

 # Chart System
- When enough users have submitted books to the site I would like to implement a chart system recording the most popular books. This     would enhance the user experience and make the site more useful.

 # Upload Image with Book Submissions
- Providing the possibility to upload an image/link to the book cover would make the site more visually appealing.


## Technologies Used

### Design
    Photoshop, Logomakr, GoogleFonts, FontAwesome

### Front-End

- [HTML](https://en.wikipedia.org/wiki/HTML5) Used for storing all my pages.
- [CSS](https://no.wikipedia.org/wiki/Cascading_Style_Sheets) Used for the styling of my webpage.
- [Javascript](https://no.wikipedia.org/wiki/JavaScript) Used for initializing my buttons and some functions for my payment methods(Stripe API).
- [Stripe](https://stripe.com/en-no) Used for accepting payments for feature upvotes.
- [Bootstrap](https://getbootstrap.com/docs/4.4/) Used for styling of the webpage.
- [Font-Awesome-Icons](https://fontawesome.com/icons?d=gallery&m=free) used for styling my navigation bar and some other sections.
- [Jquery](https://en.wikipedia.org/wiki/JQuery) Used for manipulating the dom and for the Stripe API development.

### Back-End

- [Django](https://docs.djangoproject.com/en/3.0/releases/1.11/) For all the functionality and all my coding.
- [Git](https://en.wikipedia.org/wiki/Git) Used for writing commands and inserting new documents in my webpage
- [Github](https://github.com/) Used to store my webpage for the users to have access to that and for my tutors and mentor to help me with my Milestone Project.
- [PostgreSQL](https://www.postgresql.org/)Used for deployment in Heroku.
- [Gunicorn](https://docs.gunicorn.org/en/stable/) Used as the Http server.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) Used for the deployment of my project.


## Testing


### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.
- [view](https://github.com/jmurrii/MS3/blob/master/documentation/PEP8%20Validation.png)

### Testing User Stories from User Experience (UX) Section

-   ### User stories

    -   #### Viewing and Navigation

        1. As a Shopper, I want to be able to easily be able to navigate throughout the site to find wines and then select for purchase.
        2. As a Shopper, I want to be able to view individual wine details so that I can identify the price, description, and all necessary details.
        3. As a Shopper, I want to easily view the total of my purchases at any time so as to avoid spending too much.

    -   #### Registration and User Accounts

        4. As a Site User, I want to easily register for a personal account and be able to view my profile.
        5. As a Site User, I want to easily login or logout to access my personla information.
        6. As a Site User, I want to be able to recover my password if forgotten to regain access to my account.
        7. As a Site User, I want to be able to recover my password if forgotten to regain access to my account.
        8. As a Site User, I want to receive an email confirmation agter registering and to verify that my account registration was sucessful.
        8. As a Site User, I want to be have a personalised user profile to that I can view my personal order history and save payment information.

     -   #### Sorting and Searching
      9. As a Shopper, I want to be able to easily sort the list of available wines by type, price, country etc.
      10. As a Shopper, I want to be able to search for a product by name or description and find a specific product I would like to purchase.
      11. As a Shopper, I want to be able to easily see what I've searched for and the number of results so I can quickly see if the product is available.


     -   #### Purchasing and Checkout
     12. As a Shopper, I want to easily select the quantity of a product when I select it.




       


-   #### Site Owner Goals
        
    1. As a site owner I want to earn money on each book purchased via a link from the site.

       1. Building up a community of people passionate about books and providing a space where they can share recommendations could       lead to an opportunity to affiliate with some online book store.
 

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site to point out any bugs and/or user experience issues.

### Known Bugs

-   Hamburger icon in Navbar stretches over Hero Image on small screens.

## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. 


To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Run the `snap install --classic heroku` command in the terminal window to instal heroku in my local workspace.
3. Ran the `heroku login -i` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git.
5. Linked the Heroku app as the remote master branch.
6. Created a requirements.txt file.
7. Created a Procfile
8. Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
9. Ran the `heroku ps:scale web=1` command in the terminal window to run the app in Heroku.
10. Entered the following Config Var in Heroku:

    ```MONGO_URI : <link to MongoDB>```


The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Minimalist Reading](https://minimalist-reading-ms3.herokuapp.com/)


### Forking the GitHub Repository

#### Note:
- For Secret Key contact me @ jonmurrii@gmail.com

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   
-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.


### Content

-   All content was written by the developer.

-   Format of README.md followed *[this](https://github.com/Code-Institute-Solutions/SampleREADME#code-institute-website)* example.

-   I took much inspiration from this [MS3 project](https://github.com/Pysched/MS3-DM)

### Media

-   All Images used in the site were taken from [Pexels](https://www.pexels.com/).

-   Favicon created at [Logomakr](https://logomakr.com/).

### Acknowledgements

-   My Mentor Aaoron Sinnott for helpful feedback and advice throughout.

-   Tutor support at Code Institute for their support.
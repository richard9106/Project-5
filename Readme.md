{% load static %}
# Project Name - Iron Haven Fitness


* [Link to Deployed Project](https://Iron Haven Fitness2023-9cc8e49ac2b8.herokuapp.com/)

## CONTENTS
* [USER EXPERIENCE (UX)](#user-experience)
  * [Purpose & target audience](#purpose-and-target-audience)
  * [Goals](#goals)
* [PROJECT DESIGN](#project-design)
  * [Wireframes](#wireframes)
  * [User Stories](#user-stories)
  * [Logic](#logic)
  * [Color Scheme](#color-scheme)
  * [Imagery](#imagery)
  * [Typography](#typography)
  * [MVP](#mvp)
* [FEATURES](#features)
* [VALIDATION](#validation)
* [TECH STACK](#tech-stack)
  * [Languages and Frameworks](#languages-and-frameworks)
  * [Tools and Libraries](#tools-and-libraries)
* [TESTING](#testing)
  * [Tests performed](#tests-performed)
  * [User Story Tests](#user-story-tests)
  * [Bugs resolved](#bugs-resolved)
  * [Unresolved bugs](#unresolved-bugs)
  * [Improvements & future developments](#improvements-and-future-developments)
* [DEPLOYMENT](#deployment)
* [FORKING & CLONING INSTRUCTIONS](#forking-and-cloning-instructions)
* [SECURITY SETTINGS](#security-settings)
* [CREDITS](#credits)
  * [Resources](#resources)
  * [Content](#content)
  * [Media](#media)
  


## USER EXPERIENCE

   ### Purpose and target audience

Iron Haven Fitness is a gym website that sells memberships and also has some products for its users.

It is designed with the intention that potential users see the services that the gym offers.It contains an area to see the available classes and a section of products to which you have access if you are a member.



<img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/site_images/hosted_site.png">

* [Back to Contents](#contents)

  ### Goals
  #### Goals for the first time user
  1. To be able to create an account easily.
  2. To be able to customise and update their profile.
  3. To easily update and change or cancel their memberships.
  4. To easily be able to reserve or cancel  gym classes if they need it .
  5. To easily be able to purchase for products and see the shopping gab.
  6. To be able to see how much they are going to speend before pay.
  7. To be able to  contact or subscribe yo the gym news.


  #### Goals for the returning user <br>
  8. All the pages of the app should be secure, so once logged out, the only way to access pages for products and classes is via the login page.<br>
  9. The app should feel familiar to the returning user.

  #### Goals for the Administrator <br>
  10. The administrator can easily update or override any information on the backend as a superuser.

  #### Goals for the Site Owner <br>
  11. The app should have the capacity to scale. <br>
  12. More choices of classes and products can easily be added and customised.<br>
  13. Images are validated to ensure they are not oversized dragging on site performance and storage resources. <br>



* [Back to Contents](#contents)

## PROJECT DESIGN

  ### Wireframes

   The initial wireframes were created in [Miro](https://miro.com/es/) to understand how the site would work, and this layout would drive User Stories, the logic required and overall design artwork decisions.



   - <img src="/workspace/Project-5/static/doc_images/wireframe_1.png"

   <details>
    <summary><u>Click to View More Wireframe Images</u></summary>

<span style="display:flex; gap:50px">


![Mobile ](./static/doc_images/wireframe_2.png)

![Table ](./static/doc_images/wireframe_3.png)


</span>

    
   

   </details>

* [Back to Contents](#contents)

  ### User Stories
  All the user stories with their acceptance criteria can be viewed on the next link [GitHub Project board](https://github.com/users/richard9106/projects/10)


  There were  User Stories Created including:

1. [US1] Project General Requirements
    - As a developer, I can understand the goals of the site so that development decisions can be made accordingly.
2. [US2] Setup Repo
    - As a developer, I will set up the repo and install the necessary packages so that I can start building the initial models to manage the information.
3. [US3] Profiles Model
    - As a superuser, I can log in to the admin panel	so that I can manage users and other parts of the system as it develops
4. [US4] Jobs Model
    - As a superuser, I can create a new products, gym classes and memeberships.
5. [US5] Create NavBar
    - As a website user, I can view the basic navbar so that I can easily navigate the website on desktop and mobile
6. [US6] User Login
    - As a website user, I can log in so that I can access all the functions of the site, and I can easily see if I am logged in or not
7. [US7] User Logout 
    - As a website user, I can log out so that I can protect my profile data, and I can easily see if I need to log in again
8. [US8] User Registration
    - As a website user, I can register for an account so that I can access the benefits os a memebership of the site
9. [US9] View Home Page
    - As a user I can view the home page so that I can see all the details about Iron Haven Fitnes
10. [US10] View Profile Page
    - As a logged in user I can view my profile so that I can see the details, classes and memebership information
11. [US11] Edit Profile
    - As a logged in user I can edit my profile so that I can change my personal info
12. [US12] Update Password
    - As a logged-in user, I can update my password so that I can change my password if I need to
13. [US13] Update Username
    - As a logged-in user, I can change my username so that I can change my username if I want to
14. [US14] View all the classes
    - As a logged-in user, I can register for a class and be able to see it on my profile
15. [US15] View all the products
    - As a logged-in user, I can  be able see and purchase for products and easily see my shopping bag
16. [US16] Change my memebership
    - As a logged-in user, I can change my membership if I want to
17. [US17] UX & Testing
    - As a developer, I can test each user story function so that I can verify each function works as intended
18. [US18] Deploy to Heroku
    - As a developer, I can deploy to Heroku so that I can host the site in production
19. [US19] Complete Readme Documentation
    - As a developer, I can submit a comprehensive Readme document so that other developers can understand the project's development process


* [Back to Contents](#contents)

  ### Logic
  The database schema and website logic was conceived and created using [Lucid](https://lucid.app/) as follows:

  Database Structure:


![data base structure ](./static/doc_images/iron_fitnes.png)

* [Back to Contents](#contents)

  ### Color Scheme
  The main colours of orange, dark blue and white were chosen for maximum contrast. I used [Coolors](https://coolors.co) to generate a colour palette.


![data base structure ](./static/doc_images/palet_color.png)


  I used [Canva](https://www.canva.com/) to generate a logo and a style guide.


<span style="display:flex; gap:50px; text-align:center;">


![data base structure ](./static/images/logo1.png)

![data base structure ](./static/images/logo2.png)



</span>


  * [Back to Contents](#contents)

  ### Imagery
  - I used FontAwesome https://fontawesome.com/ for various icons in the navbar, shopping bag, and other places for visual effects.

   <br>

  - I used [Pexels](https://www.pexels.com/es-es/) for free images .

  * [Back to Contents](#contents)

  ### Typography
   * I used a default Google font of Roboto and sans serif throughout the website for visual clarity and consistency.
   


  ### MVP (minimun vialble product)

  Using the GitHub project board I prioritised user stories to give me an incremental MVP.

  At each stage of achieving an MVP, I would aim to complete a piece of functioning work.  Styling issues would be noted as a small-item, logged to the Kanban board and I would revisit to make incremental visual improvements once the functionality logic was completed.

  Every commit message thoroughly detailed the work that had been completed.  Some of the more complex pieces of functionality required updates and development across several pages for the functions to work as expected and this was captured in the commit history.

1. I created the basic models for profiles and jobs first so I could upload information to pull into the front end.
2. I built the Navbar and routes
3. I built the Login, Logout and registration functionality
4. I built the Profile Area with CRUD functionality
5. I built the Jobs section with CRUD functionality
6. I built the comments section below each job card with CRUD functionality
7. I built the Invoice Model and frontend components and linked them to the relevant JobCard
8. I built the Watch Jobs functionality and views
9. I built the filters and views for My Jobs and Assigned Jobs


   * [Back to Contents](#contents)

## FEATURES
* The following fully responsive website pages have been implemented:
1. Register
2. Login
3. AllJobs with Status Dashboard, filter and search functionality
4. MyJobs with Status Dashboard, filter and search functionality
5. Assigned Jobs with Status Dashboard, filter and search functionality
6. Watched Jobs with Status Dashboard, filter and search functionality
7. Job Card with comments and links to assigned user profile, invoice, and conditional editing and ability to watch a job
8. Add Invoice functionality with custom validation and alerts
9. AddJob form with custom validation and alerts
10. All Invoices with Status Dashboard, filter and search functionality, links to conditional editing, assigned users and relevant JobCard
11. Profile page with editing functionality and custom validation

  <details>
    <summary><u>Click to View Images</u></summary>
  

  </details>


  * [Back to Contents](#contents)

* UX features and User Interactions to note:
  - Unauthenticated users can only access the login or register page.  All other pages are protected at the Route level and only available to users who have registered and logged in to their account.
  - Users can always see where they are by the nav icon that highlights yellow or by the breadrcumb Viewing bar at the top of each screen. [US5, US6,]
  - Users can hover over each icon in the NavBar to see the Nav label, and users will know they are logged in by seeing their name next to the Profile link.
  - All users can access their own Profile page where they can view or edit their profile, username or password. [US3, US11, US12, US13, US14]
  - Users can view all the jobs, jobs only created by them or jobs assigned to them. [US4, US15, US31 and US32]
  - A dashboard allows them to organise each view according to its status and the status counter lets the user filter by and know at all times how many jobs are Pending, Underway or Completed. [US16, US17]
  - Users can filter by jobs that are recently created (the default), recently updated or by their due date. [US16, US17]
  - Users can enter a keyword to search by job type, description, created by or assigned to. [US16, US17]
  - On each job card, users can click through to view the profiles of the user who created the job or the user who is assigned to the job. [ US11 ]
  - A jobs can be edited by the person who created it and allows updates to any of the fields including the image. [ US19 ]
  - An invoice can be added by the two users involved in the job - those who created it and those who are assigned to the job. [ US25 ]
  - Any user can view the invoice summary by opening the accordion feature by clicking "Click To View Invoice Summary", where they can find a button to view the invoice card or edit it if they have permission. [ US26 ]
  - Users can also click an eye icon which will add the job to a Watch list if they want to keep track of a job. [ US32 ]
  - Users will see if any comments have been left on a job and will know the amount of comments that have been left on that specific job. [US21, US22, US23, US24]
  - Users can click on the comment bubble icon and view the job card, and invoice summary, leave a comment, leave a reply to a comment and edit or delete any of their comments. [US21, US22, US23, US24]
  - Users can view all invoices in the system and use familiar dashboard features to view and filter the status, order by dates and search using keywords. [ US29 ]
  - On each invoice card, users can click through to view the profiles of the user who created the invoice or the user who is assigned to the job. [ US11 ]
  - Invoices can be edited only by those who created or were assigned to the job. [US27 and US30]
  - Any user can click on the "View Job Summary" accordion and find a link to view the full job card
  - Any user can click the "BackToTop" button incorporated on Jobs and Invoices pages to help navigate long page lists.
  <br>

  <details>
    <summary><u>Click to View UX Features Images</u></summary>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/navbar.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/navbar_mob.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/dashboard.png"><br>
     - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/dashboard_mob.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/conditional_editing.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/conditional_editing_mob.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/conditional_adding_invoice.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/conditional_adding_invoice_mob.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/view_invoice_accordion.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/view_invoice_accordion_mob.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/commenting_and_watching.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/commenting_and_watching_mob.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/comments_and_replies.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/comments_and_replies_mob.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/back_to_top.png"><br>
    - <img src="https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/documentation/images/features/back_to_top_mob.png"><br>

  </details>

  * [Back to Contents](#contents)

## VALIDATION
Various validation methods have been incorporated:
 1. Onscreen success messages after user actions
 2. Onscreen warnings if form fields have been omitted
 3. Onscreen modal confirmation step before updating or deleting items
 4. No-Data to display icon
 5. Custom 404 page for redirecting logged-in users to non-existing pages
 6. General catch-all redirects for logged-out users to the Login page for non-existing pages.
 7. Date validation to prevent booking or invoicing a past date
 8. Image validation to prevent oversized images from being uploaded
 9. Form validation to capture email and phone formats correctly


 <details>
  <summary><u>Click to View Validation Images</u></summary>

</details>

 * [Back to Contents](#contents)

## TECH STACK
The site has been built with the following tech, tools and libraries

### Languages and Frameworks

* HTML5
* CSS
* JavaScript
* Python
* Django - web framework
* Django REST Framework - API framework
* Django AllAuth - user authentication
* Psycopg2 - postgreSQL adapter for python
* ElephantSQL - database hosting
* Cloudinary - media hosting
* Pillow - python image processing library
* Gunicorn - WSGI HTTP server for UNIX
* Bootstrap 5 and react-bootsrap - frontend responsive styling framework
* Heroku - live site hosting


### Tools and Libraries
* GitHub Projects - agile management, kanban, roadmap and milestones
* GitHub Repo - code storage
* Git - version control
* GitPod & VS Code - IDE
* [Miro](https://balsamiq.com/) - creating wireframes
* [Coolors](https://coolors.co) - color pallette generator
* [Image resizer](https://www.reduceimages.com/) - resizing images for optimal storage
* [Canva](https://www.canva.com/) - creating artwork
* Google Fonts - consistent typography
* [Lucid Chart](https://lucid.app/) - creating a database schema
* [FontAwesome](https://fontawesome.com/) - icons
* [W3C HTML Validator](https://validator.w3.org/) - html code validation
* [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) - css code validation
* LightHouse - measures performance, accessibility, best practices and SEO
* Chrome Dev Tools - for development debugging
* [CI Python Linter](https://pep8ci.herokuapp.com/) - code analysis tool conforming to pep8
* Prettier - code formatter for html, css and javascript
* ESLint - code analysis tool for javascript





### Refactoring Opportunities

Due to time constraints on completing this project, I was unable to refactor all of the code.  Two notable components could help streamline the app further:

1. Dashboard used in AllJobs Page and AllInvoices Page
2. Accordion used in JobCard and InvoiceCard
3. Confrimation Modal used in Editing Jobs, Editing Invoices, Editing Profiles, and Deleting Jobs and Deleting Invoices.
4. SuccessMessage Timeout function could benefit from being a resusable component.

* [Back to Contents](#contents)


## TESTING
FOR DETAILED TEST REPORTS AND RESULTS PLEASE [VIEW THEM HERE:](https://github.com/rstan-dev/Iron Haven Fitness-PP5/blob/main/TESTING.md).

  ### Tests performed
  The site was thoroughly tested during development with each feature tested before committing to GitHub.  The testing regime included the following:
  1. Incremental development and live testing.
  2. Django Models Automated Testing using Jest.
  3. Early user observation test.
  4. React Tests.
  5. Manual user story tests.
  6. Django APITest re-run and additional automated testing using jest.
  7. HTML, CSS, ESLINT, PYLINT, Lighthouse tests.
  8. Browser Compatibility tests.
  9. Final Production user tests

  ### User Story Tests
  Each user story was tested manually according to a structured test sheet [VIEW IT HERE:](https://docs.google.com/spreadsheets/d/1esaHTm738sbXP-JMxzEvQ63mgN3IazsXGUL8tRsX0ZI/edit#gid=165646488), with results being recorded and any failures rectified.

  * [Back to Contents](#contents)

  ### Bugs resolved:
  The following bugs were recorded and rectified [See test sheet](https://docs.google.com/spreadsheets/d/1esaHTm738sbXP-JMxzEvQ63mgN3IazsXGUL8tRsX0ZI/edit#gid=165646488)



  * [Back to Contents](#contents)

  ### Unresolved bugs:

  There are no other known bugs at this time.


  ### Improvements and future developments:
  The app was initially built with enough basic fields and functionality to ensure I could deliver an MVP that would meet assessment criteria within the allocated time frame.

  There is scope to improve the app that would enhance the user experience and add more valuable functions, that could easily be developed on top of the existing structure:

  * Add consistent user feedback on the email and phone fields validation. Currently it is using the default browser message validation, and was left as is due to time constraints.

  * Create a Manager Profile who has access to all profiles, jobs and invoices on the front end, to allow moderation and site overrides.  Currently, this work can be undertaken in the Django Admin area which has not been configured for any UX.

  * Upgrade to Bootstrap 5 - will allow improved design and functionality for the Accordion and Modal components - negating the need for the deprecated findDOMNode method.

  * Consider using a modal to contain comments and replies as per the original concept.

  * Consider adding InfiniteScroll to the comment-replies section. This was left as it was deemed unlikely that there would be a vast number of replies to a single comment.  InfiniteScroll has been added to the parent comment list.



  * [Back to Contents](#contents)

## DEPLOYMENT
  for a deployment, keep in mind that depending on the functionalities, some extra configuration may be missing. Very important is the configuration of variables in Heroku and the add-ons since without these activated you will not be able to see the project correctly

  Initially, Django was installed following this Code Institute [DRF Cheatsheet](https://docs.google.com/document/d/1LCLxWhmW_4VTE4GXsnHgmPUwSPKNT4KyMxSH8agbVqU/edit#heading=h.mpopj7v69qqn)

   1. Create a Cloudinary account and gather API key
   2. Create ElephantSQL database and gather API key
   3. Install Django
   4. Create project
   5. Install Cloudinary Storage
   6. Install Pillow (image processing)
   7. Update INSTALLED_APPs
       * all apps in the django project must be make migrations
       * python manage.py makemigrations
       * python manage.py migrate
       * to pass external data to the models if you need it.
          - create the fixture folder
          - add your file.json to the folder
          - python manage.py loaddata 'name.json' 
   8. Create env.py file
       * Add CLOUDINARY_KEY (from Cloudinary API key)
       * Add SECRET_KEY - (a unique password)
       * ADD DATABASE_URL - (postgres ElephantSQL API key)
       * STRIPE_SECRET_KEY - (stripe secrete key all)
       * DEBUG = True (if you have to push to heroku set False)
   9. Update settings.py
       * CLOUDINARY_STORAGE
       * Define Media Storage URL
       * Set DEFAULT_FILE_STORAGE
       * Set DATABASES
       * set STRIPE settings
    

  ### Deployment to Heroku involved the following steps and changes:
   1. Set up DEBUG in settins.py to False
   2. install gunicorn ==22.0.0
   3. Create a Procfile (web: gunicorn core.wsgi:application) 
   4. Create a runtime.txt file and add the following: Python-3.12.3
   5. Terminate all servers.
       * Ensure DEBUG and DEV in env.py are commented out
       * python3 manage.py runserver
   6. Check project is displaying in the preview on port 8000 or gitpod
   7. Log into your Heroku account, create a new app, and access the dashboard for your application
   8. Go to Settings and open the Config Vars add all the Api keys in your env.py
       * Add CLOUDINARY_KEY (the Cloudinary API key)
       * Add SECRET_KEY - (the unique password)
       * Add DATABASE_URL - (postgres ElephantSQL API key)
       * Add STRIPE_SECRET_KEY - (stripe payments Api key)
   9. Ensure your application has an ALLOWED_HOST your '.herokuapp.com' - '.gitpod.io'
   10. Ensure in Resources in heroku dasboard change your dinos active.
   11. Go to the Deploy tab, connect the project to GitHub, and choose main branch to deploy
       * Click Deploy Branch (manually)
       * (Optional) Select Enable Automatic Deploys


* [Back to Contents](#contents)

## FORKING AND CLONING INSTRUCTIONS
You can create a copy of a GitHub Repository without affecting the original by forking or cloning it.

### Here's a step-by-step guide to forking:
Forking is often used for proposing changes or using the project as a starting point for your own idea. Forking will apear on your GitHub profile.
1. Log into GitHub or sign up for an account.
2. Go to the [Iron Haven Fitness Repository](https://github.com/richard9106/Project-5)
3. Click "Fork" on the right side of the repository's page to create a copy in your own repository.

### Here's a step-by-step guide to cloning:
Cloning is often used for experimenting locally.  It will not show up on your GitHub profile.
1. Go to the [Iron Haven Fitness Repository](https://github.com/richard9106/Project-5)
2. Click the green code button, then the arrow, and select the "clone by https" option to copy the URL.
3. Open your preferred code editor and navigate to the directory where you want to clone the repository.
4. Type 'git clone', paste the copied URL, and press enter. The repository will then be cloned to your machine.

* [Back to Contents](#contents)

## SECURITY SETTINGS
The following precautions were taken regarding the security of the site:
1. An env.py was created at the start of the project, and added to .gitignore, to contain the following settings:
   - CLOUDINARY_URL
   - SECRET_KEY
   - DATABASE_URL
   - STRIPE_SECRET_KEY
2. These values were added to the Config Vars section of Heroku's Settings page.
3. Heroku is configured with 2FA


* [Back to Contents](#contents)

## CREDITS:
The entire concept was created specifically for this assessment and is not a copy of any other project.

Initially, parts of the project were based on the Moments walkthrough project:
  * CI Template for setting up the repo - [View Here](https://github.com/Code-Institute-Org/cra-template-moments)
  * The Profile Model - similar to the Mind Well project 4 Profile model
  * The Bag, Payments and Product model - similar to the Boutique Ado but customised further for replies
  * Example readme.md from - [View Here](https://github.com/rstan-dev/GarageGuru-PP5?tab=readme-ov-file#logic)



  ### Code
  * All Python logic was written and developed specifically for this project, using the Boutique ado  Build an Ecommerce as a reference.
  * All frontend HTML, CSS, JavaScript were incrementally written specifically for this project.

  * [Back to Contents](#contents)

  ### Resources
  I used the following resources to help develop features and functionality:
 
  * ChatGPT was used to help troubleshoot and explain code functions
  * Google and StackOverflow were also used for more context and understanding
  * I reached out to Code Institute team members and tutor support from time to time


  * [Back to Contents](#contents)



  ### Media
  * The Iron Haven Fitness logo was custom-designed for this project.
  * Logo icon created in Canva Pro.
  * images from pexel
  * Icons - font awesome.

  * [Back to Contents](#contents)


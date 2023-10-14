# Tangled Treasures

Welcome to Tangled Treasures!

View the live project here: [Tangled Treasures]()

## Index – Table of Contents

* [User Experience (UX)](#user-experience-ux)
  * [User Stories](#user-stories)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories

* US01: View site.
  * As a **Site User** I can **access the Home page** so that I can **understand the site purpose and decide if relevant to my needs**.
* US02: Pagination.
  * As a **Site User** I can **view a paginated lists of items** so that **I can select the item to view**.
* US03: View a list of items.
  * As a **Site User** I can **view a lists of items** so that **I can select an item to buy**.
* US04: Account registration.
  * As a **Site User** I can **register for an account** so that **I can have a personal account and save my personal information**.
* US05: Login and/or logout
  * As a **Registered Site User** I can **login and/or logout** so that **I can access my account information**.
* US06: Recoved password:
  * As a **Registered Site User** I can **recover access to my account** so that **I can easily retrieve my password**.
* US07: Email confirmation after registering.
  * As a **Registered Site User** I can **receive an email confirmation after registering** so that **I can verify that my account registration was successful**.
* US08: User profile.
  * As a **Registered Site User** I can **get a personalised profile page** so that **I can view my details and order confirmations**.
* US09: Sort the list of items.
  * As a **Site User** I can **sort the list of items** so that **I can identify the best rated, best priced and categorically sorted items**.
* US10: Add an item.
  * As a **Site Admin** I can **add an item** so that **I can add new items to my store**.
* US11: Edit/Update an item.
  * As a **Site Admin** I can **edit an item** so that **I can change product prices, descriptions, images and other info**.
* US12: Delete an item.
  * As a **Site Admin** I can **delete an item** so that **I can remove items that are no longer for sale**.

## Features

### Existing Features

* **Favicon**

  * A Favicon has been implemented using the image on the logo and main image of the website.
  * It will be easier for the User to identify the website if they have more than one tab open.
  * ![Favicon](./static/images/favicon.png)

* **Navigation Bar**

* **The landing page image**

* **The listings list**

* **The listings details**

* **The Admin functionalities**
  
* **The Footer**

* **Sign In/Register Form**

* **Sign Up Form**

* **Logout Form**

### Features Left to Implement

/

## Technologies Used

### Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.

### Frameworks & Software

* [Github](https://github.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Django](https://www.djangoproject.com/)
* [Gitpod](https://www.gitpod.io/)
* [Balsamiq](https://balsamiq.com/)
* [Heroku](https://en.wikipedia.org/wiki/Heroku)
* [AmIresponsive](https://ui.dev/amiresponsive)
* [Favicon](https://favicon.io/)
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)
* [Cloudinary](https://cloudinary.com/)
* [Canva](https://www.canva.com/colors/color-wheel/ )
* [HTML Validation](https://validator.w3.org/)
* [CSS Validation](https://jigsaw.w3.org/css-validator/)
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)

## Testing
* I tested this page in different browsers: Chrome, Edge, Safari.
* The project is responsive, and it looks and works well on different browsers and screen sizes.
  ![Future Home](./static/images/mockup.webp)

### Validator Testing

- HTML
  * No errors were returned when passing through the official W3C validator:
    * [Home Page](./static/images/html_test.png)

* CSS
  * No errors were found when passing through the official [(Jigsaw) validator]()
    * [Home Page](http://jigsaw.w3.org/css-validator/validator?lang=it&profile=css3svg&uri=https%3A%2F%2Ffuture-home.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1)

* Python
  * I used [Python linter](https://pep8ci.herokuapp.com/), and one error was returned on the settings.py file:
    * Line 128 is too long (87 characters over 79 allowed), but unfortunately it is not possible to modify it.
    [Settings.py](./static/images/Settings.py.png)

  * The remaining Python files did not show any errors:
    * [Asgi.py](./static/images/asgy_py.png)
    * [Urls.py](./static/images/urls_py.png)
    * [Wsgi.py](./static/images/wsgi_py.png)
    * [Admin.py](./static/images/admin_py.png)
    * [Apps.py](./static/images/apps_py.png)
    * [Forms.py](./static/images/forms_py.png)
    * [Models.py](./static/images/models_py.png)
    * [Tests.py](./static/images/tests_py.png)
    * [Urls.py](./static/images/urls_app_py.png)
    * [Views.py](./static/images/views_py.png)

* Accessibility
  * Performance, accessibility and best practices were assessed through Lighthouse in devtools and passed the testing with good scores.
    ![Lighthouse](./static/images/lighthouse.png)
  * The Performance score might be improved converting the .png files in .webp files, in order to compress the images and facilitate the upload when the page is loaded. For lack of time, I did not convert them, but it is certainly an improvement that can be made.

### Manual Testing

* Navigation Bar:
  * 
* Home Page:

* List of items:
  * The list of items is fully responsive and displays 4 items on larger screens, 3 on medium screens, 2 on small screens and 1 on mobile devices. The feature has been tested for numerous screen sizes and works well.
* Opening an item:
  * 
* Footer:
  * When clicked, the "Facebook" icon opens a new tab and redirects to www.facebook.com.
  * When clicked, the "Twitter" icon opens a new tab and redirects to www.twitter.com.
  * When clicked, the "YouTube" icon opens a new tab and redirects to www.youtube.com.
  * When clicked, the "Instagram" icon opens a new tab and redirects to www.instagram.com.
* When signing in as a regular user:
  * 
* When signing in as an Admin:
  * 
* Security:
  * 

### Fixed Bugs

* The project had to be start from scratch, due to an issue with the payments. The original project was modified and reverted back to previous commits in order to fix the issue, but in the end some crucial code was lost and it was easier to start again, using the code already written up on verison 1. That repository is still accessible here [PP5 - Tangled Treasures](https://github.com/ValeP314/pp5-tangled-treasures/tree/main). 

### Unfixed Bugs

- Payments: there was an issue with checkout_order that I wasn't able to address in the short amout of time I had.


## Deployment

The live link can be found here - [Tangled Treasures]()

## Credits  

### Content

* The main structure and the README file are inspired to the I Think Therefore I Blog and Boutique Ado projects.
* [W3 School](https://www.w3schools.com/), [StackOverflow.com](https://stackoverflow.com/) and [Slack](https://slack.com/intl/it-it/) were consulted regularly for tips on general coding.
* I searched for other PP5 projects on GitHub, to make sure I was working in the right direction.

### Images

- The [homepage]() image was taken from Freepik (<https://www.freepik.com/free-photo/top-view-tea-mug-yarn-basket-with-pine-cones_11630959.htm#page=2&query=crochet&position=33&from_view=search&track=sph>).
* the pictures used for the various items, were taken from Freepik, Pixabay, Pexels and Vecteezy.
* The [icon]() image was taken from Vecteezy (<https://www.vecteezy.com/free-vector/crochet>).
* The icons were taken from [Font Awesome](https://fontawesome.com/)
* The [favicon](./media/) was created uploading the icon image onto [Favicon.io](https://favicon.io/favicon-generator/).
* The [mockup] was simulated using [AmIResponsive](https://ui.dev/amiresponsive)
* The colours for the form were selected through [Coolors](https://coolors.co/)

### Disclaimer

The information provided on this site is intended for educational purposes only.

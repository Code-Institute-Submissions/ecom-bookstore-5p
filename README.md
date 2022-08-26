# Bookstore
A website for Buying Books
See [here]() for the deployed site.

### Note: 
See [Features](#features=left-to-implement) about current limitations.

## User Stories
I used github [issues](https://github.com/edenobrega/ecom-bookstore-5p/issues) to create User Stories that would be automated to create a card in github [projects](https://github.com/edenobrega/ecom-bookstore-5p/projects/1)

![](documentation/user_stories/issues_stories.png)
![](documentation/user_stories/projects_stories.png)

## Business Model
The purpose of this site is to provide a business with an online store to sell their books from, with a built in admin page for creating books and modifying them, an accounts system for users, a search bar for users to find books and a fully working checkout system using stripe to allow users to purchase one or more books.
## UX

### Wireframes
Basket

![](documentation/wireframes/basket.png)


Checkout

![](documentation/wireframes/checkout_one.png)


Orders

![](documentation/wireframes/my_orders.png)


Search form

![](documentation/wireframes/search.png)


Search Results

![](documentation/wireframes/results.png)
### ERD
Entity Relationship Diagram used for the project
All tables shown are custom tables, UserID refers to default table made by django
![](documentation/wireframes/erd.png)
## Features

### Existing Features

- Nav bar
    - Contains links to all useful pages on site:
        - Home
        - Search
        - Login
        - Register
        - Logout
        - Reset Password
        - Basket
        - Checkout
        - My Orders

![](documentation/features/navbar.png)
![](documentation/features/logged_navbar.png)

- Index Page 
    - Shows the 3 latest created books

- Search
    - Make a search for a book using either the Name, Genre, Author or multiple at the same time
    - The similarity check returns a number from 0 to 1 so it is easy to change the threshold

![](documentation/features/searchform.png)
![](documentation/features/searchform_dropdown.png)

- Results
    - Once a search is made the results will be returned

![](documentation/features/results.png)


- Checkout
    - After the initial checkout you are sent to a page with stripe to make the payment

![](documentation/features/checkout.png)
![](documentation/features/checkout_stripe.png)

- My Orders
    - See a list of all your prior orders

![](documentation/features/my_orders.png)

- Newsletter
    - Users can sign up for a newsletter

![](documentation/features/newsletter_signup.png)
### Admin Features
- Books
    - See a list of all books
    - Delete, Modify or Create a new book using buttons on the right

![](documentation/features/admin/admin_books.png)

- Create Book

![](documentation/features/admin/admin_create_book.png)

- Add genres to a book

![](documentation/features/admin/admin_add_genres.png)

- Genres
    - See a list of Genres that can be added to a book
    - Modify the name of a Genre
    - Delete Genres

![](documentation/features/admin/admin_genre_list.png)

![](documentation/features/admin/admin_modify_genre.png)


- Newsletter
    - A user with in the group 'newsletter_writer' can use this page to write a newsletter and send it out to all who have signedup for newsletters

![](documentation/features/admin/newsletter_create.png)
### Other
- Emails
    - Using [signals](postoffice/signals.py), everytime the Book model is about to be changed and if the stock has changed from 0 an email will be sent to all those who wanted to be notified.

- Custom Templates
    - [group_check.py](bookstoreadmin/templatetags/group_check.py) a custom template tag to check the group of the user in the template
    - [tempmath.py](basket/templatetags/tempmath.py)
        - convert_total used to convert the session value 'total' into a readable value
        - discount calculates the value of a book with a discount

- [custom_converters.py](basket/custom_converters.py) used to allow negative numbers to be put into a url, this is so that negative numbers can be passed into "modify basket"

- [custom_models.py](books/custom_models.py) has a custom model which only allows a value between two numbers, this is for selecting the discount, from 1 - 100
## CRUD
### Create
- Creating a new Book

![](documentation/features/admin/admin_create_book.png)
### Read
- Viewing Books

![](documentation/features/admin/admin_books.png)

- View Search Results

![](documentation/features/results.png)
### Update
- Modify Book

![](documentation/features/admin/admin_modify_book.png)
### Delete
- Delete Book

![](documentation/features/admin/admin_delete.png)

## Features left to implement
- Favorites
    - Add the ability to have a list of favorites
- e-books
    - Have the user able to buy e-books and read them from the site or via download
    - Have users able to upload there own e-books to be sold
- Shipping
    - Have a backend for new orders to be listed for the website owners to then use to ship the items and check orders as sent

# Testing
See [TESTING.md](TESTING.md)
# Deployment

1. You will need a [Cloudinary](https://cloudinary.com) account to be able to store images and static files
    1. Go to [Cloudinary](https://cloudinary.com)
    2. Create an account
    3. Go to your [console](https://cloudinary.com/console/)
    4. A square should be present with the header "Api Environment variable", copy this value for later
2. Create an account on heroku and login
3. In Heroku, select new and "Create new app"
4. Select a unique name and select a region for hosting, and create the app
1. Next we need to add the "Heroku Postgres" add-on and get the database "URI"
    1. Navigate to the Resources tab 
    2. A search bar saying "Quickly add add-ons from Elements" should be present, in it search for "Heroku Postgres"
    3. Add the add-on, and in the popup which asks for a "Plan name" select "Hobby Dev - Free"
    1. On the "Resources tab" select the add-on we have added, and select the "Settings" tab
    1. A section titled "Database Credentials" will have a button saying "View Credentials..." select it and copy the the string given under "URI" and keep it somewhere safe for a later step
5. Navigate to settings for your new app, scroll down and click the button "Reveal Config Vars" and add the following:
    6. A variable called "CLOUDINARY_URL" and paste in the value from step 1, make sure you remove the "CLOUDINARY_URL=" at the start of the key
    7. A variable called "DATABASE_URL" and add the URI gotten from step 5
    8. A variable called "DJANGO_SECRET" and enter anything you want
    9. Another variable called "EMAIL_HOST_PASS" being the email accounts password
    8. A variable called "EMAIL_HOST_USER" being the email for the above account
    9. For the following stripe keys, logon [here](https://dashboard.stripe.com/test/dashboard) and you will be lead to the dashboard and on the right will be the keys we need for below
        1. Create a variable called "STRIPE_PUBLIC_KEY" and enter the key that is on the dashboard called "Publishable key"
        2. Create another variable called "STRIPE_SECRET_KEY" and enter the key labelled "Secret key" on the stripe dashboard
    8. Create another variable called "SECRET_KEY" and name it anything you want
    9. If you want to deploy the app in DEBUG mode then follow the indented step, if not skip it
        1. Create the final variable "DEBUG" and set it to FALSE, or delete it/don't create it at all
1. To deploy, select the "Deploy" tab in the navbar
1. Scroll down to the "Deployment method" section and connect 
1. Once connected, select the repository to be used
1. At the bottom of the deploy page, select "Deploy Branch" 

# Local Deployment
In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/edenobrega/ecom-bookstore-5p.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/edenobrega/ecom-bookstore-5p)

1. Create a file in the root called `env.py`, insde of the file copy the following:
    1. `import os`
    2. os.environ["DJANGO_SECRET"] = ""
    3. os.environ['STRIPE_PUBLIC_KEY'] = ''
    4. os.environ['STRIPE_SECRET_KEY'] = ''
    5. os.environ['EMAIL_HOST_PASS'] = ''
    6. os.environ['EMAIL_HOST_USER'] = ''
    7. os.environ['DEVELOPMENT'] = ''
    8. os.environ['DATABASE_URL'] = ''
    9. os.environ['CLOUDINARY_URL'] = ''

The following steps will all be done in your IDE Terminal
1. pip3 install -r requirements.txt
2. Eenter `python3 manage.py makemigrations`
3. And then enter `python3 manage.py migrate`
4. To run the site enter `python3 manage.py runserver`
## Technologies

## Credits
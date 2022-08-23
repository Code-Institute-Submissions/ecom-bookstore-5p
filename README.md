# Bookstore
A website for Buying Books
See [here]() for the deployed site.

### Note: 
See [Features](#features=left-to-implement) about current limitations.

## User Stories
I used github [issues](https://github.com/edenobrega/ecom-bookstore-5p/issues) to create User Stories that would be automated to create a card in github [projects](https://github.com/edenobrega/ecom-bookstore-5p/projects/1)

![](documentation/user_stories/issues_stories.png)
![](documentation/user_stories/projects_stories.png)
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

# Testing
See [TESTING.md](TESTING.md)
# Deployment

# Local Deployment

## Technologies

## Credits
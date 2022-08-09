# Bookstore
A website for  .
See [here]() for the deployed site.

### Note: 
See [Features](#features=left-to-implement) about current limitations.

## User Stories
I used github [issues](https://github.com/edenobrega/ecom-bookstore-5p/issues) to create User Stories that would be automated to create a card in github [projects](https://github.com/edenobrega/ecom-bookstore-5p/projects/1)

![](documentation/User%20Stories/issues_stories.png)
![](documentation/User%20Stories/projects_stories.png)
## UX

### Wireframes
Basket

![](documentation/Wireframes/basket.png)


Checkout

![](documentation/Wireframes/checkout_one.png)


Orders

![](documentation/Wireframes/my_orders.png)


Search form

![](documentation/Wireframes/search.png)


Search Results

![](documentation/Wireframes/results.png)
### ERD
Entity Relationship Diagram used for the project
![](documentation/Wireframes/ERD.png)
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

![](documentation/Features/navbar.png)
![](documentation/Features/logged_navbar.png)

- Index Page 
    - Shows the 3 latest created books

- Search
    - Make a search for a book using either the Name, Genre, Author or multiple at the same time
    - The similarity check returns a number from 0 to 1 so it is easy to change the threshold

![](documentation/Features/searchform.png)
![](documentation/Features/searchform_dropdown.png)

- Results
    - Once a search is made the results will be returned

![](documentation/Features/results.png)


- Checkout
    - After the initial checkout you are sent to a page with stripe to make the payment

![](documentation/Features/checkout.png)
![](documentation/Features/checkout_stripe.png)

- My Orders
    - See a list of all your prior orders

![](documentation/Features/my_orders.png)
### Admin Features
- Books
    - See a list of all books
    - Delete, Modify or Create a new book using buttons on the right

![](documentation/Features/admin/admin_books.png)

- Create Book

![](documentation/Features/admin/admin_create_book.png)

- Add genres to a book

![](documentation/Features/admin/admin_add_genres.png)

- Genres
    - See a list of Genres that can be added to a book
    - Modify the name of a Genre
    - Delete Genres

![](documentation/Features/admin/admin_genre_list.png)

![](documentation/Features/admin/admin_modify_genre.png)
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

![](documentation/Features/admin/admin_create_book.png)
### Read
- Viewing Books

![](documentation/Features/admin/admin_books.png)

- View Search Results

![](documentation/Features/results.png)
### Update
- Modify Book

![](documentation/Features/admin/admin_modify_book.png)
### Delete
- Delete Book

![](documentation/Features/admin/admin_delete.png)

## Features left to implement

# Testing
See [TESTING.md](TESTING.md)
# Deployment

# Local Deployment

## Technologies

## Credits
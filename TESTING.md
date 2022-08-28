# Testing
## Accounts
- When trying to login, if the account doesnt exist or the password is incorrect an error will appear
![](documentation/testing/login_fail.png)

- If the correct information is entered then you will be logged in and the navbar will change
![](documentation/testing/successful_login.png)

- If you don't fill out the whole form you will be given an error
![](documentation/testing/register_fail.png)
## Book
- If you search for a product it will return the results
![](documentation/testing/search_start.png)
![](documentation/testing/search_end.png)

- If you search for a book with a name with no matches an error will be shown
![](documentation/testing/search_fail_start.png)
![](documentation/testing/search_fail_end.png)

- If the item is out of stock or not available a button will appear
![](documentation/testing/item_outof_stock.png)
## Email
- Selecting "Notify Me!" will display a pop up that asks for your email.
![](documentation/testing/item_notify_form.png)

- If you do not have a watch on the item already a message will say so
![](documentation/testing/notify_success.png)

- If you already have a watch on the book a message will tell you
![](documentation/testing/notify_already_signed.png)
## Admin

## Basket
- If you have no products in your basket a message will tell you 
![](documentation/testing/empty_basket.png)

- If the book has been successfully added to your basket a message will tell you and your basket total will change
![](documentation/testing/add_to_basket.png)

- If you have an item in your basket it will appear in your basket
![](documentation/testing/basket_items.png)

## Checkout
- If you have items in your basket you will be met by a checkout form
![](documentation/testing/successful_checkout.png)

- Successfully filling out the checkout form will lead you to a stripe checkout form
![](documentation/testing/stripe_checkout.png)

- If basket is empty or out of stock the checkout form wont be shown, and you will be given a message
![](documentation/testing/checkout_empty_basket.png)
## Orders
- The my orders page will list all of your prior completed orders
![](documentation/testing/my_orders.png)

# Responsiveness
- Responsive on a small sized window

![](documentation/testing/responsiveness_small.png)

- Responsive on a desktop

![](documentation/testing/responsiveness_desktop.png)

# Code Validation
- Validated using https://validator.w3.org

-[Basket](documentation/testing/validation/html/basket.png)
-[Checkout](documentation/testing/validation/html/checkout.png)
-[Index](documentation/testing/validation/html/index.png)
-[Login](documentation/testing/validation/html/login.png)
-[Newsletter Signup](documentation/testing/validation/html/newsletter_signup.png)
-[Results](documentation/testing/validation/html/results.png)
-[Search](documentation/testing/validation/html/search.png)
-[Signup](documentation/testing/validation/html/signup.png)
-[View Book](documentation/testing/validation/html/view_book.png)
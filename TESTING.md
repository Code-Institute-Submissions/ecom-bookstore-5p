# Testing
## Accounts
- When trying to login, if the account doesnt exist or the password is incorrect an error will appear
![](documentation/Testing/login_fail.png)

- If the correct information is entered then you will be logged in and the navbar will change
![](documentation/Testing/successful_login.png)

- If you don't fill out the whole form you will be given an error
![](documentation/Testing/register_fail.png)
## Book
- If you search for a product it will return the results
![](documentation/Testing/search_start.png)
![](documentation/Testing/search_end.png)

- If you search for a book with a name with no matches an error will be shown
![](documentation/Testing/search_fail_start.png)
![](documentation/Testing/search_fail_end.png)

- If the item is out of stock or not available a button will appear
![](documentation/Testing/item_outof_stock.png)
## Email
- Selecting "Notify Me!" will display a pop up that asks for your email.
![](documentation/Testing/item_notify_form.png)

- If you do not have a watch on the item already a message will say so
![](documentation/Testing/notify_success.png)

- If you already have a watch on the book a message will tell you
![](documentation/Testing/notify_already_signed.png)
## Admin

## Basket
- If you have no products in your basket a message will tell you 
![](documentation/Testing/empty_basket.png)

- If the book has been successfully added to your basket a message will tell you and your basket total will change
![](documentation/Testing/add_to_basket.png)

- If you have an item in your basket it will appear in your basket
![](documentation/Testing/basket_items.png)

## Checkout
- If you have items in your basket you will be met by a checkout form
![](documentation/Testing/successful_checkout.png)

- Successfully filling out the checkout form will lead you to a stripe checkout form
![](documentation/Testing/stripe_checkout.png)

- If basket is empty or out of stock the checkout form wont be shown, and you will be given a message
![](documentation/Testing/checkout_empty_basket.png)
## Orders
- The my orders page will list all of your prior completed orders
![](documentation/Testing/my_orders.png)

# Responsiveness
- Responsive on a small sized window

![](documentation/Testing/responsiveness_small.png)

- Responsive on a desktop

![](documentation/Testing/responsiveness_desktop.png)
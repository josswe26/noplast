# NoPlast Testing

[Back to the README.md file](https://github.com/josswe26/noplast#noplast)  

[Back to the Testing section in the README.md file](https://github.com/josswe26/noplast#testing)

[View the live website here](https://noplast.herokuapp.com/)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)

***


## Testing User Stories


### Epic 1 - Shopping Experience


#### As a shopper, I want to easily find the products and their details.

* Products page is available, displaying the products and their main details.


#### As a shopper, I want to view products on a specific category.

* Links to each product category are provided in the home page.

* A product navigation bar is present in the products page, allowing the shopper to filter products per category.


#### As a shopper, I want to be able to sort the products depending on their price, rating or category.
* A sorting functionality is provided in the products page, allowing the shopper to sort products by price, name, rating and category.


#### As a shopper, I want to be able to search for products using specific keywords.

* A search bar is available on the website header, allowing the shopper to find a product by keyword across the whole website.


#### As a shopper, I want to easily select the quantity of products to be purchased.

* Quantity field is available in the product details page, allowing the shopper to select the desired product quantity before adding the product to the shopping bag.


#### As a shopper, I want to easily view the current purchase amount.

* The current purchase amount is available under the shopping cart icon in the header, making the information available across the whole website.


### Epic 2 - Shopping Bag and Checkout


#### As a shopper, I want to view all items currently on my shopping bag and be able to update them.
* Products added to the shopping bag are displayed in the shopping bag page.

* A quantity form is available in the shopping bag page for the shopper to update the product quantity.


#### As a shopper, I want to easily provide my shipping and payment information during the checkout.

* A form is available at the checkout for the shopper to provide the necessary information to complete the purchase.


#### As a shopper, I want to feel my personal and payment data is being handled securely.

* Stripe payments has been implemented as a payment method for the website in order to provide secure and easy transactions for the shoppers.


#### As a shopper, I want to receive an order confirmation once I have finished my purchase.

* A checkout success page is displayed to the shopper after completing the purchase.


#### As a shopper, I want to receive an order confirmation email for my records.

* An email is being sent to the email address provided by the shopper during the checkout.


### Epic 3 - shopper Accounts


#### As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website.

* All-auth has been implemented to handle user authentication, allowing the user to register an account.


#### As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.

* A confirmation is sent to the registered email address in order to validate it.


#### As a registered shopper, I want to easily log in and out from my account.

* All-auth has been implemented to handle user authentication, allowing the user to easily login and logout from their account.


#### As a registered shopper, I want to be able to recover access to my account in case I forget my password.

* All-auth can send a recovery link to the shopper's email address in the case they forget their credentials.


#### As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders.

* A profile page is available for the shopper to keep their contact information updated as well as access their past orders.


### Epic 4 - Product Reviews

#### As a shopper, I want to be able to read product reviews left by other shoppers.

* Product reviews are available in the product details page for each product.

#### As a shopper, I want to be able to sort the reviews by date or rating.

* A sorting functionality has been provided for the reviews for the shopper to sort the reviews either by date or rating.

#### As a registered shopper, I want to be able to leave product reviews and rate the products.

* Forms are available for registered shoppers if to review and rate products.

* Registered shoppers are also able to update or delete their existing reviews.


### Epic 5 - Favorites

#### As a registered shopper, I want to be able to keep a list of my favorite products to purchase again in the future.

* A favorites page has been created for registered shoppers to keep track of their favorite products.


#### As a registered shopper, I want to be able to easily add and remove favorite products.

* A favorites icon is present inside the image in the products details page, to easily add and remove products to the favorites list.

* A remove link is also provided for each product inside the favorites page.


### Epic 6 - Product Admin


#### As a site admin, I want to be able to add and update products.

* Full CRUD functionality has been implemented for site admins to manage the website products.


#### As a site admin, I want to be able to remove product no longer available.

* Full CRUD functionality has been implemented for site admins to manage the website products.

### Epic 7 - Support Organizations


#### As a site admin, I want to give the users the opportunity to support organizations helping to reduce plastic waste.

* An organizations page is available for all shoppers who want to learn more about organizations protecting the oceans.

* Links to the organization and donations pages are provided for each organization.


### Epic 8 - Newsletter Subscription

#### As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers.

* A newsletter subscription form had been added to the website footer, making it available for the shoppers across the whole website.

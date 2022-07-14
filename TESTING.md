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
6. [Unit Testing](#unit-testing)

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


## Code Validation

### HTML

* No errors were returned when passing through the [W3C Markup Validator](https://validator.w3.org/) validator. However, managed to find a stray end tag div in toast_success.html which was fixed.

### CSS
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) found no errors on my CSS files.

### Python

Pylint was used continuously during the development process to analyze the Python code for programming errors.

The code was then checked for errors via the terminal command "python3 -m flake8". This returned a number of whitespace and indentation errors which were rectified where possible. (The unfixed errors were situated in root files such as .vscode/artictern)

Other errors regarding unused imports were corrected by removing the unnecessary files.

### Javascript

* [JSHint](https://jshint.com/) found a total of 6 warnings concerning missing or unnecessary semicolons. These warnings were corrected.


## Accessibility

Lighthouse in Chrome DevTools has been used to confirm that the colors and fonts being used throughout the website are easy to read and accessible. See reports in the table below:


### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Home | ![Home Lighthouse Report](assets/testing/lighthouse-home.png) |
| Products | ![Products Lighthouse Report](assets/testing/lighthouse-products.png) |
| Product Details | ![Product Details Lighthouse Report](assets/testing/lighthouse-product-details.png) |
| Add Product | ![Add Product Lighthouse Report](assets/testing/lighthouse-product-add.png) |
| Edit Product | ![Edit Product Lighthouse Report](assets/testing/lighthouse-product-edit.png) |
| Shopping Bag !| ![Shopping Bag Lighthouse Report](assets/testing/lighthouse-bag.png) |
| Checkout | ![Checkout Lighthouse Report](assets/testing/lighthouse-checkout.png) |
| Checkout Success | ![Checkout Success Lighthouse Report](assets/testing/lighthouse-checkout-success.png) |
| Profile | ![Profile Lighthouse Report](assets/testing/lighthouse-profile.png) |
| Favorites | ![Favorites Lighthouse Report](assets/testing/lighthouse-favorites.png) |
| Reviews | ![Reviews Lighthouse Report](assets/testing/lighthouse-reviews.png) |
| Add Review | ![Add Review Lighthouse Report](assets/testing/lighthouse-review-add.png) |
| Edit Review | ![Edit Review Lighthouse Report](assets/testing/lighthouse-review-edit.png) |
| Organizations | ![Organizations Lighthouse Report](assets/testing/lighthouse-organizations.png) |

The low score on the product admin pages, depends mostly on the aria-labels being suggested for the "Select image" button and the image example.

## Tools Testing


### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

* Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.


### Responsiveness

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing


### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues. | Pass |
Safari | No appearance, responsiveness nor functionality issues. | Pass |
Mozilla Firefox | No responsiveness nor functionality issues. | Pass |
Microsoft Edge | No appearance, responsiveness nor functionality issues. | Pass |


### Device Compatibility

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
Dell Optiplex 7060 | Windows 11 | No appearance, responsiveness nor functionality issues. | Pass |
MacBook Pro 15" | macOS Big Sur | No appearance, responsiveness nor functionality issues. | Pass |
Dell Latitude 5300 | Windows 10 | No appearance, responsiveness nor functionality issues. | Pass |
iPad Pro 12.9" | iOS 15 | No appearance, responsiveness nor functionality issues. | Pass |
iPad Pro 10.5" | iOS 15 |No appearance, responsiveness nor functionality issues. | Pass |
iPhone XR | iOS 15 |No appearance, responsiveness nor functionality issues. | Pass |
iPhone 7 | iOS 15 |No appearance, responsiveness nor functionality issues. | Pass |

**Note**

The appearance of the product quantity form on the shopping bag page can be improved on smaller devices.

### Test Results

#### General

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Main Logo Link | Clicking the link redirects to the home page. | Pass |
Shop Link | Clicking the link redirects to the products page. | Pass |
About Link | Clicking the link redirects to about section in the home page. | Pass |
Support Link | Clicking the link redirects to the organizations page. | Pass |
My Account Icon - Register Link | Clicking the link redirects to the account sign up page. | Pass |
My Account Icon - Login Link | Clicking the link redirects to the account sign in page. | Pass |
My Account Icon - Logout link | Clicking the link redirects to the account sign out page. | Pass |
My Account Icon - Product Management Link | Clicking the link redirects to the add product page. | Pass |
My Account Icon - My Profile Link | Clicking the link redirects to the profile page. | Pass |
My Account Icon - My Reviews Link | Clicking the link redirects to the reviews page. | Pass |
Shopping Cart Icon | Clicking the link redirects to the shopping cart. | Pass |
Search Bar | Clicking the link redirects to the products page and display the matching products. | Pass |
Privacy Policy Link | Clicking the link opens the privacy policy. | Pass |
Facebook Icon | Clicking the link open the business Facebook page on a separate tab. | Pass |
Newsletter Form | Email address gets registered to the database when submitting the form. | Pass |


#### Home Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Categories Links | Clicking any of the links will redirect to the products page and filter the products on that category. | Pass |
Down Arrow Link | Clicking the link redirects to about section in the home page. | Pass |


#### Products Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Product Navigation Bar Links | Clicking any of the links will filter the products on that category. | Pass |
Sort By Selector | Sort by functionality sort the products depending on the selection. | Pass |
Favorites Link | Clicking the link redirects to the favorites page. | Pass |
Product Image | Clicking the image redirect to the product details page for that specific product. | Pass |
Product Edit Link | Clicking the link redirects to the edit product page. | Pass |
Product Delete Link | Clicking the link delete the product from the database. | Pass |


#### Product Details Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Product Navigation Bar Links | Clicking any of the links will redirect to the products page and filter the products on that category. | Pass
Product Image | Clicking the image opens it on a separate tab. | Pass |
Favorites Icon | Clicking the icon toggle the product on the favorites database. | Pass |
Product Edit Link | Clicking the link redirects to the edit product page. | Pass |
Product Delete Link | Clicking the link deletes the product from the database. | Pass |
Decrease Quantity Button | Decreases the quantity on the input form. | Pass |
Increase Quantity Button | Increases the quantity on the input form. | Pass |
Keep Shopping Button | Clicking the button redirects to the products page. | Pass |
Add To Bag Button | Clicking the button adds the specified quantity of the product to the shopping bag. | Pass |
Reviews Link | Clicking the link toggle the product reviews. | Pass |
Sort By Selector | Sort by functionality sort the reviews depending on the selection. | Pass |
Review Edit Link | Clicking the link redirects to the edit review page. | Pass |
Review Delete Link | Clicking the link delete the review from the database. | Pass |
Leave A Review Button | Clicking the button redirects to the add review page. | Pass |


#### Add Product Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Select Image Button | Clicking the button allows to add an image to the form | Pass |
Add Product Form | Product gets registered to the database when submitting the form. | Pass |
Cancel Button | Clicking the button redirects to the products page. | Pass |


#### Edit Product Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Select Image Button | Clicking the button allows to add or replace the image | Pass |
Edit Product Form | Product gets updated when submitting the form. | Pass |
Cancel Button | Clicking the button redirects to the products page. | Pass |


#### Shopping Bag Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Decrease Quantity Button | Decreases the quantity on the input form. | Pass |
Increase Quantity Button | Increases the quantity on the input form. | Pass |
Update Link | Clicking the link update the product quantity on the shopping bag. | Pass
Delete Link | Clicking the link removed the product from the shopping bag. | Pass
Keep Shopping Button | Clicking the button redirects to the products page. | Pass |
Secure Checkout Button | Clicking the button redirects to the checkout page. | Pass |


#### Checkout Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Checkout Form | An order gets created when submitted the form. | Pass |
Login Link | Clicking the link redirects to the account sign in page. | Pass |
Register Link | Clicking the link redirects to the account sign up page. | Pass |
Save Information Check | Checking the box update the user's profile information during the checkout process. | Pass |
Adjust Bag Link | Clicking the link redirects to shopping bag page. | Pass |


#### Checkout Success Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Want To Help? Button | Clicking the button redirects to the organizations page. | Pass |


#### Profile Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Update Information Form | User's information gets updated when submitting the form. | Pass |
Order Link | Clicking the link redirects to order view. | Pass |


#### Favorites Page
Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Remove Link | Clicking the link removes the product from the user's favorites list. | Pass |


#### Reviews Page
Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Product Link | Clicking the link redirect to the product details page. | Pass |
Edit Link | Clicking the link redirect to the edit review page. | Pass |
Delete Link | Clicking the link deletes the review from the database. | Pass |


#### Add Review Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Add Review Form | Review gets registered to the database when submitting the form. | Pass |
Cancel Button | Clicking the button redirects to the product details page. | Pass |


#### Edit Review Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Edit Review Form | Review gets updated when submitting the form. | Pass |
Cancel Button | Clicking the button redirects to the products page. | Pass |


#### Organizations Page
Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Learn More Button | Clicking the button opens the organization's page on a separate tab. | Pass |
Donate Button | Clicking the button opens the organization's donation page on a separate tab. | Pass |


## Unit Testing

Unit tests were written for views on the favorites and reviews app, practicing test-driven development on those methods.
# NoPlast


![NoPlast mockup images](assets/readme/mockup-image.png)


NoPlast is an ecommerce website offering a variety of plastic-free products. 

The main purpose of the website is to provide site users with eco-friendly alternatives to single-use plastic products that are bad for the environment. 

Another goal the website wants to achieve is to create consciousness about plastic pollution and in this way reduce plastic waste. Site users are also given the option to support charities that are fighting to protect our world's oceans from plastic pollution by making a donation. 

Visit the deployed website [here](https://noplast.herokuapp.com/).


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
        1. [Database Model](#database-model)
    4. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    5. [Surface](#surface)
        1. [Color Scheme](#color-scheme)
        2. [Typography](#typography)
2. [Marketing](#marketing)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md]()
5. [Deployment](#deployment)
6. [Finished Product](#finished-product)
7. [Credits](#credits)
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)


***


## User Experience (UX)


### Strategy


#### Project Goals

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly for an easy shopping experience.

* The website desing and colors are appealing to the customers.

* Customers are offered the opportunity to register an account.

* Easy shopping process to create a pleaseant experince for the customer.


#### User Goals

**Epic 1 - Shopping Experience**

* As a shopper, I want to easily find the products and their details.

* As a shopper, I want to view products on a specific category.

* As a shopper, I want to be able to sort the products depending on their price, rating or category.

* As a shopper, I want to be able to search for products using specific keywords.

* As a shopper, I want to easily select the quantity of products to be purchased.

* As a shopper, I want to easily view the current purchase amount.

**Epic 2 - Shopping Bag and Checkout**

* As a shopper, I want to view all items currently on my shopping bag and be able to update them.

* As a shopper, I want to easily provide my shipping and payment information during the checkout.

* As a shopper, I want to feel my personal and payment data is being handled securely.

* As a shopper, I want to receive an order confirmation once I have finished my purchase.

* As a shopper, I want to receive an order confirmation email for my records.

**Epic 3 - User Accounts**

* As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website.

* As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.

* As a registered shopper, I want to easily log in and out from my account.

* As a registered shopper, I want to be able to recover access to my account in case I forget my password.

* As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders.

**Epic 4 - Product Reviews**

* As a shopper, I want to be able to read product reviews left by other shoppers.

* As a shopper, I want to be able to sort the revies by date or rating.

* As a registered shopper, I want to be able to leave product reviews and rate the products.

**Epic 5 - Favorites**

* As a registered shopper, I want to be able to keep a list of my favorite products to purchase again in the future.

* As a registered shopper, I want to be able to easily add and remove favorite products.


**Epic 6 - Product Admin**

* As a site admin, I want to be able to add and update and products.

* As a site admin, I want to be able to remove product no longer available.

**Epic 7 - Support Organizations**

* As a site admin, I want to give the users the opportunity to support organizations helping to reduce plastic waste.

**Epic 8 - Newsletter Subscription**

As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers.


#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Create, edit and delete products | 5 | 5
Account registration | 5 | 5
User profile | 5 | 5
Wishlist | 4 | 4
Save shipment information | 5 | 5
Product quick view | 3 | 2
Sort products by different criteria | 5 | 5
Search products by name or description | 5 | 5
Product details view | 5 | 5
Display similar products at the a product details view | 3 | 2
Rate products | 4 | 3
Write product reviews | 4 | 3
Display current purchase total | 5 | 5
View current shopping cart | 5 | 5
Edit quantities inside the shopping bag | 4 | 4
Shopping cart quick view | 3 | 3
Card payment | 5 | 5
Additional payment options | 3 | 2
Donations | 4 | 3
Newsletter subscription | 5 | 5
Bonus system | 3 | 1
**Total** | **95** | **87**


### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases. The first phase will include the features that have been identified in order to build the minimum viable product.


**First Phase**

* Responsive design

* Create, edit and delete products

* Account registration

* User profile

* Save shipment information

* Sort products by different criteria

* Search products by name or description

* Product details view

* Display current purchase total

* View current shopping cart

* Edit quantities inside the shopping bag

* Card payment

* Newsletter subscription


**Second Phase**

* Wishlist

* Rate products

* Write product reviews

* Donations


**Third Phase**

* Product quick view

* Display similar products at the a product details view

* Shopping cart quick view

* Additional payment options

* Bonus system


#### User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

**Start**
![User Stories Progress - Start](assets/readme/user-stories-start.png)

**Sprint 1**
![User Stories Progress - Sprint 1](assets/readme/user-stories-print1.png)

**Sprint 2**
![User Stories Progress - Sprint 2](assets/readme/user-stories-sprint2.png)

**Sprint 3**
![User Stories Progress - Sprint 3](assets/readme/user-stories-sprint3.png)

**Sprint 4**
![User Stories Progress - Sprint 4](assets/readme/user-stories-sprint4.png)

**Sprint 5**
![User Stories Progress - Sprint 5](assets/readme/user-stories-sprint5.png)

**Sprint 6**
![User Stories Progress - Sprint 6](assets/readme/user-stories-sprint6.png)


### Structure


#### Database Model

The database model has been designed using [drawsql](https://drawsql.app/). The type of database being used for the is relational database being managed using SQLite3 during development and deployed using [PostgreSQL](https://www.postgresql.org/).

![NoPlast Database Model](assets/readme/db-model.png)


### Skeleton


#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Home | ![Desktop home wireframe image](assets/wireframes/home-desktop.png) | ![Mobile home wireframe image](assets/wireframes/home-mobile.png)
Products | ![Desktop products wireframe image](assets/wireframes/products-desktop.png) | ![Mobile products wireframe image](assets/wireframes/products-mobile.png)
Product Details | ![Desktop product details wireframe image](assets/wireframes/product-details-desktop.png) | ![Mobile product details wireframe image](assets/wireframes/product-details-mobile.png)
Shopping Bag (Quick View) | ![Desktop quick shopping bag wireframe image](assets/wireframes/quick-bag-desktop.png) | ![Mobile quick shopping bag wireframe image](assets/wireframes/quick-bag-mobile.png)
Shopping Bag | ![Desktop shopping bag wireframe image](assets/wireframes/shopping-bag-desktop.png) | ![Mobile shopping bag wireframe image](assets/wireframes/shopping-bag-mobile.png)
Checkout | ![Desktop checkout wireframe image](assets/wireframes/checkout-desktop.png) | ![Mobile checkout wireframe image](assets/wireframes/checkout-mobile.png)
Profile | ![Desktop profile wireframe image](assets/wireframes/profile-desktop.png) | ![Mobile profile wireframe image](assets/wireframes/profile-mobile.png)

### Surface


#### Color Scheme

![Color scheme image](assets/readme/color-scheme.png)

The colors used in the website are a series of blue tones to represent the stunning ocean colors and this way captivate our shoppers.

We use Oxford Blue (#001F3D) for the main text, main buttons, navbar links and other links, as well as in some dark backgrounds to create color contrast across the website.

For secondary buttons, footer background, as well as for links transitions we use a Blue Sapphire (#055772). As well as to highlight some of the text and titles.

Cerulean Crayola (#09ABD7) is sparingly used, mainly in transitions and to highlight some critical links.

We used Ghost White (#F4F6FC) for the main background and in text located within the dark backgrounds.


#### Typography

The font used across the whole site is Oswald. It was used in two different weights.

After some research on popular ecommerce business fonts. We decided to go with Oswald mainly for its simplicity, which makes it easy to read but at the same time being attention-grabbing.


[Back to top ⇧](#noplast)


## Marketing


## Features


[Back to top ⇧](#noplast)


## Technologies Used


### Languages Used


### Libraries and Frameworks


### Packages / Dependecies Installed


### Database Management


### Tools and Programs


[Back to top ⇧](#noplast)


## Testing

The testing documentation can be found [here]().


[Back to top ⇧](#noplast)

## Deployment


[Back to top ⇧](#noplast)


## Finished Product


[Back to top ⇧](#noplast)


## Credits


### Content


### Media


### Code


## Known Bugs


[Back to top ⇧](#noplast)

## Acknowledgements


[Back to top ⇧](#noplast)
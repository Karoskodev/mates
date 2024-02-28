# MATES E-SHOP

![am I responsive screenshot](media/readme/responsive.png)

## E-commerce Store for Chess Enthusiasts
> The e-commerce chess store sells a variety of chess sets and accessories online, providing a convenient shopping experience for chess enthusiasts of all levels.


### - By Tomas Karavasilev

## **[LIVE SITE](https://matesapp-6452160599de.herokuapp.com/) | [REPOSITORY](https://github.com/Karoskodev/mates)**

-----

## Table of contents
<a name="contents">Back to Top</a>
 1. [ UX ](#ux)
 2. [ Business Model ](#business)
 3. [ SEO ](#seo)
 4. [Agile Development](#agile)
 5. [ Features ](#features)  
 6. [ Features Left to Implement ](#left)  
 7. [ Technology used ](#tech) 
 8. [ Testing ](#testing)  
 9. [ Bugs ](#bugs)  
 10. [ Deployment](#deployment)
 11. [ Credits](#credits)
 12. [ Content](#content)  
 13. [ Acknowledgements](#acknowledgements)  

 ---

 ## UX

 <a name="ux"></a>
 ### Color pallete

 I tried to stick with the color scheme reminiscent of the chessboard, chess, chess pieces and wood.
 <br>
 
 ![Color](media/readme/color.jpg)

 ### Database Schema

 ![Lucid Diagram](media/readme/database.png)

 -----
### Models
<br>

#### User Profile Model

| id | Field |
|--|--|
|user|OneToOneField|
|user_image|imagefield|
|user_title|charfield|
|user_nickname|charfield|
|phone_number|charfield|
|street address1|charfield|
|street address2|charfield|
|county|charfield|
|postcode|charfield|
|town or city|charfield|
|country|countryfield|


#### Order Model


| id | Field |
|--|--|
|order_number|CharField|
|user_profile|ForeignKey|
|full_name|CharField|
|email|EmailField|
|phone_number|CharField|
|country|CountryField|
|postcode|CharField|
|town_or_city|CharField|
|street_address1|CharField|
|street_address2|CharField|
|county|CharField|
|date|DateTimeField|
|delivery_cost|DecimalField|
|order_total|DecimalField|
|grand_total|DecimalField|
|original_bag|TextField|
|stripe_pid|CharField|


#### OrderLineItem Model


| id | Field |
|--|--|
|order|CharField|
|product|ForeignKey|
|quantity|CharField|
|lineitem_total|EmailField|


#### Product Model


| id | Field |
|--|--|
|category|ForeignKey|
|sku|CharField|
|name|CharField|
|description|TextField|
|price|DecimalField|
|rating|DecimalField|
|image_url|URLField|
|image|ImageField|


#### Category Model


| id | Field |
|--|--|
|name|CharField|
|friendly_name|CharField|


#### Post Model


| id | Field |
|--|--|
|title|CharField|
|slug|SlugField|
|featured_image|DateTimeField|
|updated_on|DateTimeField|
|created_on|DecimalField|
|content|TextField|
|status|IntegerField|



#### Contact Model


| id | Field |
|--|--|
|subject|CharField|
|email|EmailField|
|message|TextField|
|created_at|DateTimeField|


## UX design

### Wireframes

<br>
Main page:

![Wireframe Index](media/readme/mainwireframe.png)
<br>
Products page:

![Wireframe Index](media/readme/products.png)
<br>
Product Detail page:

![Wireframe Index](media/readme/detail.png)
<br>
Shoping Bag page:

![Wireframe Index](media/readme/bag.png)
<br>
Blog page:

![Wireframe Index](media/readme/blog.png)
<br>
Contact form page:

![Wireframe Index](media/readme/contact.png)
<br>
---

## Business Model

<a name="business"></a>

#### Business Overview
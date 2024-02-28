# MATES E-SHOP

![am I responsive screenshot](media/readme/responsive.png)

## E-commerce Store for Chess Enthusiasts
> The e-commerce chess store sells a variety of chess sets and accessories online, providing a convenient shopping experience for chess enthusiasts of all levels.


### - By Tomas Karavasilev

## **[LIVE SITE](https://matesapp-6452160599de.herokuapp.com/) | [REPOSITORY](https://github.com/Karoskodev/mates)**

---

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

 I tried to stick with the colors reminiscent of the chessboard, chess pieces and wood.
 <br>
 
 ![Color](media/readme/color.jpg)

 ### Database Schema

 ![Lucid Diagram](media/readme/database.png)

 ---
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
Mates Chess Eshop is a B2C e-commerce platform specializing in chess-related products, aiming to provide high-quality chess sets, boards, and accessories to customers worldwide through an online store.

Benefits for the Business Owner:
1. Scalability: Easily expand the business as it grows.
2. No Physical Location: No need for a brick-and-mortar store, allowing for global reach.
3. Global Targeting: Cater to customers worldwide, targeting chess enthusiasts.
4. Niche Branding: Focus on a specific niche, building a brand that resonates with chess players.
5. Low Startup Cost: Begin with a relatively low initial investment, allocating more budget to customer acquisition and marketing.
6. Impulse Buying: The lower price point encourages impulse purchases from customers.

Cons:
1. Initial Customer Acquisition: Overcoming industry saturation to attract initial customers.
2. Brand Establishment: Building a brand from scratch requires time and a solid marketing strategy.
3. Marketing Effort: Manual marketing or paid advertising is essential for gaining organic traffic.
4. Trust Building: Absence of physical presence may make it challenging to build trust without discounts or offers.

---

#### Site User

User 1:
The typical site user is a chess enthusiast, male, aged between 10 and 80, interested in chess. They seek quality chess products to enhance their gaming experience.

User 2:
Additional users include partners of User 1, browsing for gifts catering to the chess interest.

---

#### Goals for the Website:

User-Friendly Interface: Ensure an easy-to-navigate website with a clear purpose.
Product Satisfaction: Provide products that meet user expectations.
Quick Checkout: Facilitate a seamless checkout process.
User Profiles: Enable users to create profiles, view past orders, and update information.

---

#### Marketing Strategy

Goals:

1. Facebook Promotion: Leverage the Facebook business page for store promotion.
2. Social Network Sharing: Encourage friends and family to share the page, enhancing visibility.
3. Soft Launch Sale: Initiate a soft online launch sale to stimulate early adoption and purchases.
4. Subscriber Engagement: Use Mailchimp to gather subscribers and send promotions for repeat business.
5. SEO Content: Develop meaningful articles and blog posts to enhance SEO ranking on search engines.
6. Paid Advertising: Utilize platforms like Google Ads and Facebook Ads to reach the target demographic.
7. Product-Centric Ads: Run multiple ads featuring different chess products, analyzing and focusing on high-performing ones.
8. Influencer Collaboration: Consider promoting custom-made products through influencers in the chess niche, targeting those with at least 10k followers.
9. By following this strategy, Mates Chess Eshop aims to establish itself as a go-to platform for chess enthusiasts, offering a seamless online shopping experience and valuable content to build a loyal customer base.

---

# SEO

<a name="seo"></a>

### SEO Project planning

As the decision to focus on a Mates store was made, comprehensive market research and keyword analysis became pivotal for effective online visibility. Here's an overview of the steps taken:
1. Google Trends Utilization
2. SEO Quake Tool
3. Wordtracker.com
4. A comprehensive list of carefully selected keywords was developed, considering factors such as search volume, competition, and relevance.
5. The selected keywords were strategically incorporated into various elements of the website
6. The content strategy focused on creating informative and engaging content related to chess

By adopting a data-driven approach and leveraging various tools, Mates Eshop aimed to establish a robust online presence, attracting chess enthusiasts.

### Keywords

Handmade chess set, handmade chess pieces, handmade chess board, chess cabinet, wooden chess set, digital chess clock, analog chess clock, play chess

### Sitemap.xml:
A comprehensive sitemap has been generated for the website to facilitate efficient indexing by search engines like Google. This strategic move ensures that once the site is live, search engines can systematically navigate and index its content. The sitemap acts as a roadmap, enhancing the discoverability of various pages and improving overall search engine optimization.

### Robots.txt:
To guide the crawling behavior of search engine bots, a robots.txt file has been meticulously crafted. In this file, specific directives have been set to optimize the crawling process. Notably, pages within the accounts app have been excluded from crawling, as they do not contribute to the site's search engine visibility.

### Facebook Business Page

To view the facebook business page you can click on the link below:

[Facebook Business Page](https://www.facebook.com/profile.php?id=61556545065240)

In case the page becomes inactive or deactivated by Facebook I have taken screenshots to display here also:

![FB Business page overview](media/readme/facebook.jpg)

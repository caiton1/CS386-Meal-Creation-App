# Deliverable 3 : Group 2 Analysis

## 1. System Description : 

The problem of planning meals throughout the busy week, especially with all the different dietary restrictions, affects everyone from on the go college students to young families. The impact of which is that they have to either take time away from their busy lives to try and figure this out on their own, or they sacrifice what they eat in order to get everything done. These issues cost people time, physical health, mental health, and performance in other aspects of their lives. For people with busy lives who need help picking and organizing meals effectively, our product Pick-My-Meals allows users to personally curate meals that fulfill their dietary needs while still maintaining other aspects of their lives. Unlike Hello Fresh our product is completely driven by user customization while not locking customers into frustrating subscriptions. Making the planning, buying, and cooking easier to fit around each person's schedule, unique cooking style, and dietary needs. Pick-My-Meals is a free meal planning website that allows those with busy lives and/or dietary needs to personally organize and curate meal plans that fit their lives more efficiently by letting them choose exactly what recipes they want to eat while we take care of calculating a detailed grocery list of what to buy, how much to get, and what it will cost them. Unlike other meal planning apps and websites, Pick-My-Meals doesn’t lock users into subscriptions just to find meals they want to eat, so no need to pay extra for shipping or subscription fees. Pick-My-Meals also stands out for the vast amount of recipes to choose from along with unique filters to allow the user to truly enjoy what they are eating. While other products may ship the groceries to you, the uptick in porch pirates and the worry of food spoiling at your door brings unneeded stress. Pick-My-Meals allows the customer to have peace of mind of where and how they are getting their groceries as well as allowing them to support their local businesses doing so. 

Our product will have a few key requirements in order to make our product user friendly and better than our competitors. Pick My Meals will utilize the **user's** *location*. This will allow our website to ***find*** the closest **stores** to the **user** to ***choose***. This is very helpful for **users** who want to shop local and natural, organically, support local farmers or simply find the most affordable option. Once the **user** ***chooses*** their desired **store**, all the *ingredients* that the **user** does not already have will ***fill*** their **cart**. From there the **user** will specify *pickup* as an in-store pickup, an online delivery via **store** or shop themselves.

**Users** will also have the ability to ***upload*** their own **post** to be shown as a **recipe**. In the **post**, one can add their own tags in the *description* such as “high protein”, “vegetarian”, “quick and easy”, etc. This will allow our website to have thousands of unique **recipes** to ***choose*** from. Our website will also include a **filter** that allows the **user** to easily ***find*** what they are looking for, whether it is a **recipe** with a specific *ingredient*, a holiday themed food, or a quick snack on the go.

These features make our product stand out from our competitors such as Hello Fresh or Blue Apron. Our product will allow for 100x the amount of selectable **recipes**, eliminates the need to pay for shipping and a subscription, eliminates the worry of ingredients being shipped fresh, allows for unlimited meal customization, and gives the customer the choice to ***choose*** where their *ingredients* are coming from. 

## 2. Model :

![UML diagram](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/dev/Deliverables/Deliverable3/uml_diagram_cs386.drawio.png)

## 3. Class Responsibilities

### Classes:  
**User** 
- User_id 
    * Specific key that uniquely identifies each user 
- User_password 
    * Unique password for each user 
- User_location 
    * Location of user
 
**Recipe** 
- directions 
    * Instructions on how to make the recipes. Values: peel, cut, bake, etc 
- serving_size 
    * The serving size of the recipe. So the amount of ingredients will correspond  to the serving size 
- ingredients 
    * The items necessary to make the meal 
- rating 
    * Ratings given by users who have made the recipe before
  
**Store**  
- Distance 
    * How close/far the store is from the customer. Will be used to determine which stores will shown to the customer 
- Pricing 
    * Will help determine if the store is cheap or expensive 
- Website 
    * We need to access the stores website in order to add things to the customer’s shopping cart 
- Priority 
    * We will prioritize stores that have partnerships with us. For example if we have a partnership with Walmart they will take high-priority so they will be recommended to customers 
- Pickup 
    * How the user wants to get their ingredients. Values: curbside, in-store, delivery, in-person 
- Store_id 
    * Specific key that uniquely identifies the store
  
**Cart**  
- ingredients 
    * Items necessary to create the recipe, will be added to the user’s shopping cart. Values can include garlic, pasta, chicken, lemon, pepper, etc. 
- num_people 
    * The amount of people that the user wants the recipe to feed. Will determine the serving size, thus determining the amount of needed ingredients 
- cost 
    * The cost of all the ingredients, the total of the user’s shopping cart, will be determined after the user chooses a store from the list presented to them
   
**Filter**  
- dietary_restriction 
    * Examples of this include vegetarian, vegan, gluten free etc.  
- meal_type 
    * Breakfast, lunch, dinner, snacks 
- food_type 
    * Ex. Chinese, Mexican 
- needed_utilities 
    * Ex. Stove, pot, pan, microwave,  
- preference 
    * does the user like the ingredients in this recipe or not, difficulty level of the recipe 
- budget 
    * How much is the user willing to pay for their recipe
  
**Order**  
- Store_id 
    * The identification of the store selected for the order 
- User_location 
    * Location of the user 
- Cost 
    * Total cost of the ingredients based off of the prices of the specific store 
- Date 
    * Date of the order/pickup 
- Pick_up 
    * Type of pickup 
        * Ex. curbside, instore, etc.
      
**Sponsor**  
- Store_id 
    * Identification of the store that is sponsoring our product 
- Priority 
    * Priority given to the sponsors based off of contracts with the company 
- Company 
    * The name and information of the companies that sponsor our product.
  
**Post**  
- Ingredients 
    * Items necessary for the recipe that is being posted 
- Directions 
    * Instructions and steps for making the recipe 
- Serving_size 
    * Serving size of the recipe. How many servings will be made/how many people can be fed 
- User_id 
    * Unique identification number for a user 


# Deliverable 7: Group 2  

## Description    
Our website provides a user-friendly platform for discovering and selecting unique recipes. In addition to standard features like instructions and nutritional information, our standout feature is the recipe recommendation tool. Catering to users uncertain about their culinary preferences, it presents a variety of recipes from our extensive database, allowing users to accept or decline suggestions. Accepted recipes integrate into a user's planned list, enhancing meal preparation organization.  

What sets us apart further are our advanced filters. In addition to traditional sorting options, our platform offers unique filters such as calorie count, beneficial for those adhering to specific dietary restrictions. Our pricing filter dynamically calculates recipe costs based on current grocery store prices, aiding users in managing their budgets efficiently. The platform also accommodates dietary restrictions, including allergies. With an emphasis on user-friendliness, our product eliminates subscription and shipping costs, offering a vast selection of recipes, customizable meals, and the flexibility for users to choose their preferred ingredient sources.  

## Verification
**Testing Framework:** pytest  
**Automated Tests:** [Unit Tests Folder](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/tree/main/website/unit_tests)  
**Test Case:**

This test case is an example of a test that uses mock objects. This test file uses local variables that are not taken from anywhere else. This file doesn’t depend on any of the other classes besides the class it is being tested on. Mock objects are used instead of getting them from other classes. This specific test tests the rating system and the rating calculation. The user token and ratings for a meal are mock objects used to make the tests work. 

[test_rating.py](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/main/website/unit_tests/test_rating.py)

**File Tested:**  
[rating.py](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/main/website/functions/rating.py) 

**Unit Test Execution:**
![Screenshot 2023-11-19 175108](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/ba0d43cc-66da-4b82-b568-9b0069b50d09)

## Acceptance Test  
**Framework Used**
For the acceptance test, we decided to develop the tests through Selenium because that was the best option to test our website. 

**Automated Tests Folder:** [Automated Tests Folder](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/tree/dev/website/acceptance_tests)

**Automated Test Example:**
This acceptance test is to see if the user can log onto the website. Once onto the website with an account it tests the searching feature. It will add meals to the favorite and planned lists. After all the tasks are completed, the test logs itself out. 

Test: [Acceptance Test](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/dev/website/acceptance_tests/acceptance_test.py)

Execution Video: [Execution Video](https://youtu.be/Q2Fv6mVV_U8)


## Validation
### User Evaluation #1
**Script:**  
1. Look through the recipes and see if there are any that interest you.  
1. After finding a recipe try to favorite it or add it to your planned list.  
1. Try using our recipe recommender.  
1. Report an issue.

**Data Collected**
- Account created and user data space set in database
- Added recipes to favorites list
- Thoughts on layout and issues reported  

What could improve our website?  
* Nice to know if you are logged in - hard to tell if logged in or not
* Would like to incorporate all search methods into one. Make the search function better
* Checkoff meals you have all already made so you don’t mix meals up
  
What did you like about our website?  
*  It was very easy to navigate through the website
* Liked how there were prices for each ingredient but it needs to be accurate to the actual prices around town
  
Did you find the website easy to use?    
*  Yes, the user found the website easy to use. She strongly agrees!
* The only thing hard to find was the meal recommender. It should be at the top of the dashboard, not at the bottom

  
**Reflection:**  
The user's successful engagement with various features of the website, such as creating an account, logging in, and saving favorite recipes, reflects the site's intuitive design. However, the notes reveal that the meal recommender's location at the bottom of the dashboard posed a minor navigational challenge. Relocating this feature to the top could optimize user accessibility, ensuring that users easily discover and utilize the meal recommender, a tool likely central to their experience.
The user was also talking about how the website needs to have more recipes. This was a feature we didn’t get to implement this semester. Once that is complete we would have a more solid website with more options the user can choose from. Another aspect that can be improved is the search functionality. They would like to combine search functionalities so we can search based on price and allergies.  


### User Evaluation #2
**Script:**  
1. Look through the recipes and see if there are any that interest you.  
1. After finding a recipe try to favorite it or add it to your planned list.  
1. Try using our recipe recommender.  
1. Report an issue.

**Data Collected**
- Account created and user data space set in database
- Added recipes to favorites list
- Thoughts on layout and issues reported  

What could improve our website?  
*  Add the cost totals to the recipes  
*  Add more recipes
  
What did you like about our website?  
*  Easy navigation  
*  That the cost of ingredients was included  
*  Liked the random meal suggester  
*  Thought the search filters were good and useful
  
Did you find the website easy to use?    
*  The user found the website easy to use  
*  Should specify if calories and price are being filtered from low to high or high to low  
*  Found it easy to report issues
  
**Reflection:**  
Through watching the user navigate the website and complete the given tasks I found that our website is easy to use and has features that users like. My tester got excited when he saw that the ingredients all had their estimated cost next to them, but he wished there was a total cost provided as well. He also liked the filters that we had since they are unique and convenient, being able to easily find affordable and high-calorie meals. However, he did say that he would have preferred it if it said specifically “sort from high to low” or vice versa. I would say that we have accomplished our value proposition. The website was user-friendly and offered unique features. My tester especially liked the random meal suggestions, he said it is a good way to easily discover new meals without having to put in any effort.  

### User Evaluation #3
**Script:**  
1. Create an account
1. Use the recipe filter to sort for their allergies
1. Find a recipe and add it to favorites or plan
1. Report an issue about the site

**Data Collected**
- Account created and user data space set in database
- Added recipes to favorites list
- Thoughts on layout and issues reported

What could improve our website?  
*  Display calorie and allergy information on the meal plan page
*  Add more recipes and add pictures
*  Have allergies stored upon second use
  
What did you like about our website?  
* Quick and easy to create account and get started
* The filtering system
* Favorite list made it easy to find wanted recipes
* Easy to report an issue or request
  
What stood out to you about our website?  
*  Easy to use and navigate
*  Relaxing color palette
*  Dedicated spot to report issues and ideas
*  Cool random recipe suggester
 
**Reflection:**  
I had my roommate Nate who I interviewed previously this semester about what he would want in Pick My Meals so we had a frame of reference from a user who would be interested in a product like this. He made an account easily and went directly to the recipe page. He enjoyed looking through the recipes and found the allergy filter easy to use to sort the recipes that would be available to him. He wished there were more recipes because after accounting for his allergy there was a fairly limited amount of available recipes. He reported that he liked the colors that we used for the website but noted that it could look a bit sharper with the fonts on the recipes. Overall he enjoyed the base website and is excited for what is to come. At the end of the day, while we are in the infancy of software deployment for our website I believe we have satisfied our value proposition. The website offers easy to use filtering and favoriting features that the testing user enjoyed, while still feeling unique from other competing websites. While there are some aspects that can be cleaned up, I like the spot where we are at. 

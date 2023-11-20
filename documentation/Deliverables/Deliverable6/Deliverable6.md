# Deliverable 6 Implementation 2: Group 2

## Introduction

Pick-My-Meals is a free meal-planning website. Our targets are those with busy lives and dietary needs like vegetarianism, or gluten-free. It allows users to pick curated recipes that fit their lifestyles and meet their dietary needs. Filters allow the user to specify whether they want recipes with specific ingredients, quick and easy meals, high protein, etc. We take care of calculating a detailed grocery list of what to buy, how much to get, and what it will cost. Pick-My-Meals stands out for the vast amount of recipes to choose from, unique filters, and the lack of subscription and shipping fees. While other products may ship the groceries to you, the uptick in porch pirates and the worry of food spoiling at your door brings unneeded stress. With us users know where their ingredients come from, which allows users to shop on a budget, or support local businesses. 

GitHub Link: https://github.com/caiton1/CS386-Meal-Creation-App-WIP-

## Implemented Requirements
============================================================
### Implemented Requirement #1 - Connor Aiton

**Requirement:** As a user, I want a simple way to look through and select recipes so that I can explore recipes easier.

**Issue:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/issues/82

**Pull request:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/pull/91

**Implemented by:** Connor Aiton

**Approved by:** Aiden Seay

**Print screen:** 

The recipe page shows a random generated recipe with quick data. When the user clicks green, it gets added to their planned recipes. When the user clicks red, it gets removed from their planned recipes

![Screenshot 2023-11-19 153031](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/7d4553b4-9216-42b9-a7a8-926b74ff2409)

Here I am showing the initial GET request followed by the user POSTing their decision to the server, which then will generate another recipe via a redirected GET request to itself:

![Screenshot 2023-11-19 153226](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/02fbf639-37d8-4b19-8889-34189ee2a4e7)

Result after deciding

![Screenshot 2023-11-19 153254](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/ae2bdec8-9804-4f9a-af72-4b656703320e)


============================================================
### Implemented Requirement #2 - Jared Brotamonte

**Requirement:** As a mother of 6, I want a recipe calculator so I don't have to tediously calculate how much I need for each recipe for my whole family.

**Issue:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/issues/87

**Pull request:** 

**Implemented by:** Jared Brotamonte

**Approved by:** Connor Aiton

**Print screen:**

This is the implementation of adjusting recipe's via a desired serving size

![Screenshot 2023-11-19 153434](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/d82f938f-928a-4dd7-ad81-4c6e341a871b)

Unit Testing:

![Screenshot 2023-11-19 153630](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/a1b4ab17-01c6-49fc-b700-f7a33601b025)


============================================================
### Implemented Requirement #3 - Sophia Ingram

**Requirement:** As a user who is a slight perfectionist, when I notice an issue with a website I want some sort of way to contact the developers so the issue can be fixed.

**Issue:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/issues/83

**Pull request:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/pull/94

**Implemented by:** Sophia Ingram

**Approved by:** Connor Aiton

**Print screen:**  

Screen where issue is reported on the website:

![Screenshot 2023-11-19 153759](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/225e948f-01ca-4337-97dc-afdca1cce7a0)

Unit Test:

![Screenshot 2023-11-19 154019](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/69bc16b8-7084-49bc-b390-8f9f27563f9e)







============================================================
### Implemented Requirement #4 - Elleana Negrelli

**Requirement:** As a user of the website, I want a page on the website that will keep track of all the recipes I want to shop ingredients for and keeps track of total cost so I don't have to do the calculations in my head.

**Issue:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/issues/84

**Pull request:** 

**Implemented by:** Elleana Negrelli

**Approved by:** Connor Aiton

**Print screen:**

[INSERT IMAGES HERE]




============================================================
### Implemented Requirement #5 - Aiden Seay

**Requirement:** As a cook, I want to have a rating system so that I can see what meals are good or not.

**Issue:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/issues/86

**Pull request:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/pull/93

**Implemented by:** Aiden Seay

**Approved by:** Connor Aiton

**Print screen:**

Rating calculation

![Screenshot 2023-11-19 165752](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/8e344dea-7ed9-4f64-af81-ff552cb85ab8)

Toggle functionality: This shows that the user can toggle their vote per meal item. Each user that has a vote per meal item is included in the list.

![Screenshot 2023-11-19 170216](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/b1cfcf70-4d07-4eac-aca1-86223028d5f2)

Unit Testing:

![Screenshot 2023-11-19 154217](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/065fbad7-b134-483a-a18e-e788b0415a2d)







============================================================
### Implemented Requirement #6 - Isaiah Swank

**Requirement:** As someone who values eating and using high quality ingredients, I want to be able to pick which store I get my ingredients from so I can use that store's specific ingredients.

**Issue:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/issues/81

**Pull request:** 

**Implemented by:** Isaiah Swank

**Approved by:** Connor Aiton

**Print screen:**

[INSERT IMAGES HERE]







## Tests
**Frame Work:** All unit testing in this project use pytest.

**Unit Test Folder:** https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/tree/main/website/unit_tests

**Example of a test case**

**Test Output**
[INSERT IMAGE HERE]



## Demo

[INSERT VIDEO LINK HERE]



## Code Quality

We managed code quality by changing who was in the quality assurance position, we switched it to someone who has the most knowledge about how the website works, that way we can be extra sure that our code works properly. We also made sure that this time around our pytests produced no warnings, since this could lead to issues within our project. Checking how our code worked with the website when we made a big change was super important, because our code could run with no issues but may not properly work on the website, so constantly checking it ensured good code quality.



## Lessons Learned

We learned that meeting more than once a week to work on deliverables works best for use. It allows us all to communicate and help each other that way we stay on track. It also helped with struggles that some of the group members had such as how to implement our code into the website, this helped ensure that not just one member was taking care of this task. If we were to continue developing the project we would make sure that everyone in the team understands the framework of the website, it would be helpful if everyone was well versed with this. It would make implementing our code and testing it on the website much quicker and easier.


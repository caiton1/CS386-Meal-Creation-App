# Deliverable 5 Design : Group 2

## Description

## Architecture (Jared Brotmonte)

## Class Diagram (Isaiah Swank)

## Sequence Diagram (Sophia Ingram)

## Design Patterns (Aiden Seay)

### Structural Design Pattern
The design pattern used here is the adapter design pattern. This design pattern is like a converter so multiple classes can interact with each other. While in this specific example, we don’t use classes, it is the same idea. In order to store all of our data, we need a cloud database (Firebase). In order to get all of the information we need to use, we made user.py. user.py is responsible for converting information into data we can use on the website. This would best fit the adapter design pattern as the adapter from the database to the website is user.py.

![AdapterDesign](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/9ed33c14-ce21-4d43-b644-84d776336bad)

LINKS:
* [views.py](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/main/website/views.py)
* [user.py](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/main/website/functions/user.py)

### Behavioral Design Pattern
The design pattern used here is the strategy design pattern. This design pattern defines a family of algorithms. An example of the strategy design pattern is used in the sort_by_cost functions. The UML class diagram for the strategy design pattern is below. The strategy is to sort meals by their cost. The context is the website for which the functions are sorting the meals for.

![StrategyDesign](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/assets/116912057/4ba259fa-1a1d-481f-8555-76b956a3ac92)

LINK:
* [sort_by_cost functions](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/main/website/functions/sort_by_cost.py)

Disclaimer: This project doesn't use classes so we are stretching these examples to best fit the design patterns. 

## Design Principles (Elleana Negrelli)

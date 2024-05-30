# CS386-Meal-Creation-App-(WIP)
Our product Pick-My-Meals is a free website that allows users to personally curate meals that fulfill their dietary needs through the use of custom filters. These filters allow users to select specific dietary needs or ingredients, that way they are provided with unique recipes. Unlike Hello Fresh our product is completely driven by user customization while not locking customers into frustrating subscriptions. Our product handles the grocery list by utilizing the customer’s location in order to find stores closest to them. Once a store is selected our product takes care of curating the grocery cart, saving the user time and money. This project will use teamwork and impliment software engineering concepts.

## Getting Started

### Prerequisites
1. Install python3

### Installation
1. Execute: pip install -r requirements.txt 
2. Depending on your system you will run:
    * Windows: python website/views.py
    * Linux:  python3 website/views.py
3. Setup firebase real time database
4. Create a web app on firebase, copy the app info given by firebase into the config.py inside website folder.

## Status
Our meal creation app is still being developed. We are currently working on creating a backend infastructure for our website.

## Testing
All of our tests are in [website/unit_tests](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/tree/main/website/unit_tests). These tests are used to test all of the functions for our website. Functions are located in [website/functions](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/tree/main/website/functions). 

## Setup
So far we have decided on using google cloud as our backend and use mainly python for this project for its ease of use and versatility. However we will use JS and C as we see fit either due to requrinments or better support.

*More details and information to come later as development progresses.*

## Contributing 
Please read [CONTRIBUTING.md](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/main/CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](https://github.com/caiton1/CS386-Meal-Creation-App-WIP-/blob/main/CODE_OF_CONDUCT.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
Version 0.2.0

## Authors
- **Connor Aiton** - [caiton1](https://github.com/caiton1) 
- **Aiden Seay** - [aidenseay](https://github.com/aidenseay)
- **Sophia Ingram** - [2502sophia](https://github.com/2502sophia) 
- **Isaiah Swank** - [Isaiah-Swank](https://github.com/Isaiah-Swank) 
- **Jared Brotamonte** - [JKBrotamonte](https://github.com/JKBrotamonte) 
- **Elleana Negrelli** - [enegrelli](https://github.com/enegrelli)

## Disclaimer
This product is not intended to be used in production and only as a project. There may still be security flaws such as XSS. There is also a lot of optimization to be done, such as how data is accessed. Our main concern is to have a working product by a deadline and scalability is not a top priority.

### License
This projected is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file.

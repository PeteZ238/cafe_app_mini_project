# cafe_app_mini_project
 Data engineering training mini project. Tha aim is to create an app for a pop-up cafe that logs and tracks orders. 

## Overview
The client has launched a pop-up cafe in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders.

## Requirements
As a business:
*   I want to maintain a collection of products and couriers.
*   When a customer makes a new order, I need to create this on the system.
*   I need to be able to update the status of an order, i.e. preparing, out-for-delivery, delivered.
*   When I exit my app, I need all data to be persisted and not lost.
*   When I start my app, I need to load all persisted data.
*   I need to be sure my app has been tested and proven to work well.
*   I need to receive regular software updates.

## Technical Specifications
### User Interface
You will be building a program that runs on the command line interface (CLI).
*   UI should be logical, clear and simple to navigate.
*   It should display a menu of options, some may be nested.
*   There should be the option to exit / return to main menu.
*   It should handle invlaid input.

## Future Improvements
*   Look into tail call optimisation and the methods calling into each other. While loops (hybrid of current and initial solution) might be a better solution for long term usage of the app.
*   Change data persistence method from txt files to csv (Pandas dataframes?)
*   Settings menu to allow customisation of the app (ie switch off action confirmation)
*   Extend product order update to update individual items rather than wipe products and start from scratch
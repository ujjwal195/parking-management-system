# parking-management-system

The Parking Management System is a Python-based application designed for a parking management system and it also utilizes MySQL database  to store information about parking slots, parking types, and transactions



## Table of Contents


### 1. Introduction

### 2. Requirment

### 3. Package imported

### 4. Function description

### 5. Main menu

### 6.:Conclusion:



## Introduction:

Parking Management system is designed to efficiently manage parking spaces in various locations with the help of  Parking Management System, user can easily track and monitor parking spaces, assign parking spots to vehicles, and generate reports for better analysis. This system provides a user-friendly interface that will allow the user to perform different tasks.The script provides various functionalities such as adding new parking types and slots, modifying records, vehicle login and logout, searching for parking information, generating reports, and more.

##Requirements

Python 3.x
MySQL Server



Detailed report on the code structure


## PACKAGE IMPORTED :

**"mysql.connector"**
It is one of the package which is imported which is  used as an  interface for connecting to and interacting with MySQL databases and will allow the user to execute SQL queries, fetch results, and manage database connections from the Python code.       

**Import time**
Function used for working with time-related operations

**Datetime** manipulating dates and times


## FUNCTION DESCRIPTION() :

**clear():**
This function clears the console screen to provide a clean and refreshed interface for the user in other words it is used to add extra lines between the code 


**made_by():** and the introduction()functions
Displays the name of the one who created it and it also  provides an introduction or overview of the Parking Management System and display a brief description of the system's purpose, its features etc.


**display_parking_type_records():** 
This function retrieves and displays the records of all the parking types stored in the system. Users can observe the various parking types and their associated costs because it retrieves the data from the database and shows it in an understandable fashion. 


**login():**
 Function is responsible for handling the user authentication process. It request the users to enter thier username and password and then verifies the credentials aganist the user database.

 
**add_parking_type_record():**
It allows the user to add a new parking type to the "parking_type" table. It ask the user to enter the slot ID, associates it with a specific parking type, and updates the availability status of the slot


 **add_parking_slot_record():** 
allows the user to add a new parking slot to the "parking_space" table. It prompts the user to select a parking type by its ID, and then provides options to modify the type name or its associated price


 **modify_parking_type_record():** 
It allows  users to modify records in the "parking_type".It asks the user to choose a parking type by its ID and then gives them the option to change the type name or the price that goes along with it.


**modify_parking_space_record() functions:** 
It allows  users to modify records in the "parking_space" tables .


**add_new_vehicle():** 
 This function facilitates vehicle login by adding a new record to the "transaction" table.The entered information is stored in the database to keep track of the parked vehicles.To maintain track of the parked cars, the entered data is saved in the database.


 **remove_vehicle():**
 This function handles vehicle logout by updating records in the "transaction" and "parking_space" tables.In order to identify the record and remove it from the database, it asks the user for the vehicle number. This tool aids in keeping a current list of parked cars.



 **The search_menu() function:**
It is a menu used for searching parking information based on different criteria.It offers a user-friendly interface with a variety of search options, including looking for parked cars, searching for parking spaces based on ID, and looking for open spots. A search request is fulfilled by the associated function once the user has chosen a search option.



**MAIN MENU:**
It acts as a serving loop for the  the main program. It displays a menu to the user and allows them to select different operations for managing the parking system. Depending on the user's choice, the corresponding functions are called to perform the desired operation.



**Conclusion:**
The Parking Management System provides a convenient way to manage parking operations, track vehicle entry and exit, and generate reports for efficient management and revenue tracking. With the help of Python and MySQL, the system offers a user-friendly interface and robust database integration.Its intuitive interface and comprehensive functionality make it a valuable tool for parking administrators.


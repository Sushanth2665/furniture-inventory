Furniture Inventory Management System
Overview

The Furniture Inventory Management System is a console-based application designed to help furniture store owners manage their inventory, track stock levels, and monitor sales. The system allows users to perform various operations such as adding, updating, viewing, and deleting furniture items. With this system, users can maintain an accurate record of their stock and sales, making it easier to keep track of available furniture, manage pricing, and ensure that the store operates efficiently.
Features

    Add Furniture: Users can input details about new furniture, including the name, type, material, price, and available quantity.
    Update Furniture: Users can modify the details of existing furniture items, such as changing the price or updating the stock quantity.
    View Furniture: A feature to view all the furniture in stock with their details, including name, type, material, price, and quantity.
    Delete Furniture: Users can remove a piece of furniture from the inventory when it is no longer available or needed.
    Track Sales: Keep track of sales made, updating the inventory accordingly.

Requirements

    Python 3.x or higher
    Console or terminal for running the program

How to Use

    Add Furniture:
        Select the option to add new furniture.
        Provide details such as the furniture name, type, material, price, and quantity.
        The system will store the new item in the inventory.

    Update Furniture:
        Choose the option to update existing furniture.
        Select a furniture item by its name or ID.
        Modify details like price or stock level as needed.
        Save the updated details.

    View Inventory:
        The system will display a list of all available furniture with details about each item, including the current stock and price.

    Delete Furniture:
        Choose to delete a piece of furniture by selecting its name or ID.
        The system will remove the item from the inventory.

    Track Sales:
        When a sale occurs, reduce the stock quantity for the sold items.
        The system will keep track of the number of sales made for each item.

Structure of the Program

    Data Input Handling: Uses input() to collect data such as name, material, price, quantity, and other details about the furniture items.
    CRUD Operations:
        Create: Allows adding new items.
        Read: Displays the available furniture items in the inventory.
        Update: Modify the details of existing items.
        Delete: Removes items from the inventory.
    Tracking Sales: Update stock levels based on sales made.

import tkinter as tk
from tkinter import messagebox

# Furniture inventory data structure
furniture_inventory = []

# Function to add a new furniture item
def add_furniture():
    name = entry_name.get()
    f_type = entry_type.get()
    material = entry_material.get()
    try:
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for price and quantity.")
        return

    # Create a furniture dictionary and add to inventory
    furniture = {
        "name": name,
        "type": f_type,
        "material": material,
        "price": price,
        "quantity": quantity,
        "sold": 0
    }
    furniture_inventory.append(furniture)
    update_furniture_list()
    messagebox.showinfo("Furniture Added", f"Furniture '{name}' added to inventory.")

# Function to update furniture item details
def update_furniture():
    selected_index = listbox_furniture.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a furniture item to update.")
        return

    index = selected_index[0]
    name = entry_name.get()
    f_type = entry_type.get()
    material = entry_material.get()
    try:
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for price and quantity.")
        return

    # Update the selected furniture
    furniture_inventory[index] = {
        "name": name,
        "type": f_type,
        "material": material,
        "price": price,
        "quantity": quantity,
        "sold": furniture_inventory[index]["sold"]
    }
    update_furniture_list()
    messagebox.showinfo("Furniture Updated", f"Furniture '{name}' updated.")

# Function to delete a furniture item
def delete_furniture():
    selected_index = listbox_furniture.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a furniture item to delete.")
        return

    index = selected_index[0]
    name = furniture_inventory[index]["name"]
    del furniture_inventory[index]
    update_furniture_list()
    messagebox.showinfo("Furniture Deleted", f"Furniture '{name}' deleted from inventory.")

# Function to track a sale and update stock levels
def track_sale():
    selected_index = listbox_furniture.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a furniture item to track the sale.")
        return

    index = selected_index[0]
    quantity_sold = entry_sale_quantity.get()

    try:
        quantity_sold = int(quantity_sold)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for quantity sold.")
        return

    if quantity_sold <= 0:
        messagebox.showerror("Invalid Sale", "Quantity sold must be a positive number.")
        return

    if quantity_sold > furniture_inventory[index]["quantity"]:
        messagebox.showerror("Insufficient Stock", "Not enough stock to complete the sale.")
        return

    # Update the quantity and sold count
    furniture_inventory[index]["quantity"] -= quantity_sold
    furniture_inventory[index]["sold"] += quantity_sold
    update_furniture_list()
    entry_sale_quantity.delete(0, tk.END)
    messagebox.showinfo("Sale Recorded", f"Sale of {quantity_sold} items of '{furniture_inventory[index]['name']}' recorded.")

# Function to update the list of furniture in the listbox
def update_furniture_list():
    listbox_furniture.delete(0, tk.END)
    for i, furniture in enumerate(furniture_inventory):
        furniture_info = f"{furniture['name']} - {furniture['type']} - {furniture['material']} - ${furniture['price']} - Quantity: {furniture['quantity']} - Sold: {furniture['sold']}"
        listbox_furniture.insert(tk.END, furniture_info)

# Function to display selected furniture details in entry fields for editing
def display_furniture_details(event):
    selected_index = listbox_furniture.curselection()
    if selected_index:
        index = selected_index[0]
        furniture = furniture_inventory[index]

        entry_name.delete(0, tk.END)
        entry_name.insert(0, furniture["name"])

        entry_type.delete(0, tk.END)
        entry_type.insert(0, furniture["type"])

        entry_material.delete(0, tk.END)
        entry_material.insert(0, furniture["material"])

        entry_price.delete(0, tk.END)
        entry_price.insert(0, furniture["price"])

        entry_quantity.delete(0, tk.END)
        entry_quantity.insert(0, furniture["quantity"])

# Tkinter GUI Setup
root = tk.Tk()
root.title("Furniture Inventory Management System")

# Furniture Input Fields
label_name = tk.Label(root, text="Furniture Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_type = tk.Label(root, text="Furniture Type:")
label_type.grid(row=1, column=0)
entry_type = tk.Entry(root)
entry_type.grid(row=1, column=1)

label_material = tk.Label(root, text="Material:")
label_material.grid(row=2, column=0)
entry_material = tk.Entry(root)
entry_material.grid(row=2, column=1)

label_price = tk.Label(root, text="Price ($):")
label_price.grid(row=3, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=3, column=1)

label_quantity = tk.Label(root, text="Quantity:")
label_quantity.grid(row=4, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=4, column=1)

button_add_furniture = tk.Button(root, text="Add Furniture", command=add_furniture)
button_add_furniture.grid(row=5, columnspan=2)

button_update_furniture = tk.Button(root, text="Update Furniture", command=update_furniture)
button_update_furniture.grid(row=6, columnspan=2)

button_delete_furniture = tk.Button(root, text="Delete Furniture", command=delete_furniture)
button_delete_furniture.grid(row=7, columnspan=2)

# Sale Tracking Fields
label_sale_quantity = tk.Label(root, text="Quantity Sold:")
label_sale_quantity.grid(row=8, column=0)
entry_sale_quantity = tk.Entry(root)
entry_sale_quantity.grid(row=8, column=1)

button_track_sale = tk.Button(root, text="Track Sale", command=track_sale)
button_track_sale.grid(row=9, columnspan=2)

# Furniture List Box
listbox_furniture = tk.Listbox(root, height=10, width=70)
listbox_furniture.grid(row=10, columnspan=2)
listbox_furniture.bind('<<ListboxSelect>>', display_furniture_details)

# Start the Tkinter event loop
root.mainloop()

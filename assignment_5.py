#que1
'''
# Inventory dictionary
inventory = {}

# Function to add a new product
def add_product(name, quantity, price):
    if name in inventory:
        print("Product already exists.")
    else:
        inventory[name] = (quantity, price)
        print(f"{name} added to inventory.")

# Function to remove a product
def remove_product(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print("Product not found.")

# Function to update product quantity
def update_quantity(name, quantity):
    if name in inventory:
        price = inventory[name][1]
        inventory[name] = (quantity, price)
        print(f"Quantity of {name} updated.")
    else:
        print("Product not found.")


# Function to view all products
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for name, (qty, price) in inventory.items():
            print(f"{name}: Quantity = {qty}, Price = {price}")

# Function to search for a product
def search_product(name):
    if name in inventory:
        qty, price = inventory[name]
        print(f"{name}: Quantity = {qty}, Price = {price}")
    else:
        print("Product not found.")

# Function to calculate total value of inventory
def total_value():
    total = sum(qty * price for qty, price in inventory.values())
    print(f"\nTotal Inventory Value: ₹{total:.2f}")

# Sample menu to test
def menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. View Inventory")
        print("5. Search Product")
        print("6. Total Inventory Value")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            name = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_product(name, qty, price)

        elif choice == '2':
            name = input("Enter product name to remove: ")
            remove_product(name)

        elif choice == '3':
            name = input("Enter product name to update: ")
            qty = int(input("Enter new quantity: "))
            update_quantity(name, qty)

        elif choice == '4':
            view_inventory()

        elif choice == '5':
            name = input("Enter product name to search: ")
            search_product(name)

        elif choice == '6':
            total_value()

        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
menu()

'''

#que2

student=[]

def add():
    info=[]
    name=input("enter name of student")
    info.append(name)
    n=int(input("number of subject"))
    m=[]
    for i in range(n):
        sub=int(input("enter marks"))
        m.append(sub)
    marks=tuple(m)
    info.append(marks)
    information=tuple(info)
    student.append(information)
    print(f"{name}->{marks}")

def remove():
    name=input("enter the name of the student to remove details")
    for i in range(len(student)):
        if name==student[i][0]:
            student.pop(i)
            print(f"{name} details has been removed successfully")
            break
    else:
        print("not found")


def average():
    name=input("enter name for calculationg average")
    info=list(student[0])
    
    for i in range(len(student)):
        total=0
        if name==student[i][0]:
            marks=list(student[i][1])
            for i in range(len(marks)):
                total=total+marks[i]
    avg=total/len(marks)
    print(f"average marks of {name} is {avg}")

def class_avg():
    count=0
    total=0
    for j in range(len(student)):
        marks=list(student[j][1])
        total+=sum(marks)
        count=count+len(marks)
    avg=total/count
    print(f"average marks of class is {avg}")

def high():
    high=max(student,key=lambda x:max(x[1]))
    low=min(student,key=lambda x:min(x[1]))
    print(f"{high[0]} has highest marks: {max(high[1])}")
    print(f"{low[0]}has lowest marks={min(low[1])}")
    
        
def display():
    for name,marks in student:
        print(f"{name}:{marks}")

def menu():
    while True:
        print("1.add\n2.remove\n3.average\n4.classavg\n5.max and min\n6.display\n7.exit")
        choice=int(input("enter your choice"))
        if choice==1:
            add()
        elif choice==2:
            remove()
        elif choice==3:
            average()
        elif choice==4:
            class_avg()
        elif choice==5:
            high()
        elif choice==6:
            display()
        elif choice==7:
            print("program closed")
            break
        else:
            print("enter correct choice")
            break

menu()




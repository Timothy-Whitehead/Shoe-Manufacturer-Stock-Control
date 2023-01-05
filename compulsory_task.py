
# Shoe Class with required methods built in
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    # Finds price of each shoe
    def get_cost(self):
        cost = self.cost
        return cost
        
        
    # finds quantity for each shoe
    def get_quantity(self):
        quantity = self.quantity
        return quantity
        
        
    # Creates string format for Class
    def __str__(self):
        shoe_string = f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
        return shoe_string
       
       

shoe_list = []
# My functions
# Reads from Inventory file, creates Shoe object and adds to list
def read_shoes_data():
    with open("inventory.txt", "r") as stock_file:   
        for line_num,line in  enumerate(stock_file):
            if line_num != 0:
                shoe_line = line.replace("\n", "")
                shoe_split = shoe_line.split(",")
                new_shoe = Shoe(shoe_split[0], shoe_split[1], shoe_split[2], float(shoe_split[3]), int(shoe_split[4]))
                shoe_list.append(new_shoe)

# Gets info from user, creates new Shoe object the adds to both list and file   
def capture_shoes():
    while True:
        try:
            print("Please enter the correct information when prompted")
            country = input("Country: ")
            code = input("Product code: ")
            product = input("Product name: ")
            cost = float(input("Unit Price: £"))
            quantity = int(input("Qantity: "))
            break
        except TypeError:
            print("Some of the info you've have netered is invalid.")

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    with open("inventory.txt", "a") as stock_file:
        shoe_line = f"{country},{code},{product},{cost},{quantity}\n"
        stock_file.write(shoe_line)

    
# Prints all Shoe object data. Uses string formatting to create a "table" for easy reading
def view_all(shoe_list):
    table_data = [["Country", "Code", "Product", "Cost", "Quantity"]]
    for shoe in shoe_list:
        row_data = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        table_data.append(row_data)
    for row in table_data:
        print(f"\n{row[0]:{20}}{row[1]:{10}}{row[2]:{20}}{row[3]:{7}}{row[4]:{7}}")

    
# Displays Shoe object with lowest stock quantity
# Give user option to order more then adds to Shoe.quantity
# updates file
def re_stock(shoe_list):
    shoe_min = shoe_list[0]
    for shoe in shoe_list:
        shoe_q = shoe.get_quantity()
        min_q = shoe_min.get_quantity()
        if shoe_q < min_q:
            shoe_min = shoe
    shoe_split = str(shoe_min).split(",")
    print(f"Country {shoe_split[0]}, Code {shoe_split[1]}, Product {shoe_split[2]}, Cost {shoe_split[3]}, Quantity {shoe_split[4]}")
    
    while True:
        restock = input("Would you like to restock? y/n: ").lower()
        if restock == "y":
            try:
                order = int(input("How many units would you like to order?: "))
            except TypeError:
                print("You have entered an invalid value.")
            shoe_min.quantity += order
            with open("inventory.txt", "w") as stock_file:
                for shoe in shoe_list:
                    stock_file.write(str(shoe) + "\n") 
            break
        elif restock == "n":
            break
        else:
            print("You have enterd an invalid value")
# Allows user to input an SKU number then displays all relevant data     
def search_shoe(shoe_list):
    search_code = input("Please enter a product code: ")
    search_shoe = 0
    for shoe in shoe_list:
        if shoe.code == search_code:
            search_shoe =shoe
    shoe_split = str(search_shoe).split(",")
    print(f"Country {shoe_split[0]}, Code {shoe_split[1]}, Product {shoe_split[2]}, Cost {shoe_split[3]}, Quantity {shoe_split[4]}")


# For each shoe calulates total stock value
# Prints table of Product names and values
def value_per_item(shoe_list):
    value_table = [["Product", "Stock Value"]]
    
    for shoe in shoe_list:
        cost = shoe.get_cost()
        quantity = shoe.get_quantity()
        value_table.append([shoe.product, (cost * quantity)])
    for row in value_table:
        print(f"{row[0]:{20}}{row[1]:{20}}")


# Finds Shoe with highest stock quantity and displays it as ON Sale
def highest_qty(shoe_list):
    shoe_max = shoe_list[0]
    for shoe in shoe_list:
        shoe_q = shoe.get_quantity()
        max_q = shoe.get_quantity()
        if shoe_q > max_q:
            shoe_max = shoe
    print(f"{shoe_max.product}s are ON SALE!!!")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    read_shoes_data()

    menu = input("""Please choose an option from the menu:
as - View All Stock
sp - Seach for a product by product code
np - Add New Product
ls - View Low Stock Items
si - View current Sale Items
sv - View Total Stock Value for each product 
ex - exit \n""").lower()
    
    if menu == "as":
        view_all(shoe_list)

        
    elif menu == "sp":
        seach_shoe(shoe_list)
        
    elif menu == "np":
        capture_shoes()
        
    elif menu == "ls":
        re_stock(shoe_list)

        
    elif menu == "si":
        highest_qty(shoe_list)
        
    elif menu == "sv":
        value_per_item(shoe_list)
        
    elif menu == "ex":
        print("Byeeeee!!!")
        break
    else:
        print("Sorry, you have made an invalid choice.")
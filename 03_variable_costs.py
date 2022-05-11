import pandas


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)
            print()


# not blanck function from mmf
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if not response:
            print(error)
        else:
            return response


# currenecy formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine
# set up dictionarys and lists

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}


# Get user data
product_name = not_blank("product name: ", "The product name cannot be blank.")

# loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("Item name: ", "The item name cannot be blank.")

    if item_name.lower() == "xxx":
        break

    quantity = num_check("Quantity: ", "The amount must be a whole more then 0", int)


    price = num_check("How much foir a single item? $", "The price must be more then 0", float)

    # add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

print()
variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# calculate cost of each component
variable_frame['Cost'] = variable_frame['Quantity']\
    * variable_frame['Price']

# Find sub total
variable_sub = variable_frame['Cost'].sum()

# currency Formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# *** Printing Area ***

print(variable_frame)
print()
print("Variable Costs: ${:.2f}".format(variable_sub))

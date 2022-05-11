import re
import pandas
# functions go here


# Checks that users input is not blank and returns name once input corretcly
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if not response:
            print(error)
        elif str.isspace(response):
            print(error)
        else:
            return response


# Number checker that checks users input for any scenario From last years code
def num_check(question, error, num_type, exit_code=None, low=None, high=None):

    valid = False
    while not valid:
        try:
            # Checks if user inputs exit code
            response = input(question)
            if response == exit_code:
                return response
            else:
                response = num_type(response)
            
            # Checks if they inputed correct number
            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# checks if string is valid
def string_checker(choice, error, options):


    for var_list in options:

        # if the snack is in one of the lists
        if choice in var_list:

            # Get full name of snack and put it 
            # in title case so it looks nice
            response = var_list[0].title()
            return response
            
    print(error)
    return "invalid choice"
        

# gets snacks
def get_snack():

    # holds snack order for a single user.
    snack_order = []

    # a list of all the snacks and valid responses to order snacks
    valid_snacks = [
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&Ms","M&M's", "m&m's", "mms", "m", "mm", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "h20", "d"],
        ["orange juice", "oj",  "o", "juice", "e", "tenthplace"]
    ]

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

        snack_row = []
        
        # asks user what snack they want
        desired_snack = input("Snack: ").lower()

        # breaks loop is exit code used 
        if desired_snack == "xxx" or desired_snack == "n":
            return snack_order

        # if item has a number separate it into two parts (number and item)
        if re.match(number_regex, desired_snack):
            amount= int(desired_snack[0])
            snack = (desired_snack[1:])

        # if item does not have a number infront, set number too 1
        else:
            amount = 1
            snack = desired_snack
        
        # remove white space around snack
        snack = snack.strip()
        
        # check if snack is valid
        snack_choice = string_checker(snack, snack_error, valid_snacks)

        # checks if amount is valid
        if amount >= 5:
            print("Sorry  - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack and amount to list
        snack_row.append(amount)
        snack_row.append(snack_choice)
        
        # append snack to list 
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


# checks if users age is valid
def ticket_check(tickets_sold, ticket_limit):

    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    # if there is one seat left
    else:
        print("*** There is 1 Seat left ***")

    return    


# gets ticket price
def ticket_price():
    
    # asks user for age
    age = num_check("Age: ", "<error> please enter age.", int , None, -1)

    # checks if users age is between the perameters 
    if age < 12:
        print("Only those who are above 12 years old can purchase a ticket \n"
        "Sorry for the inconvenience.")
        return "invalid ticket price"

    elif age > 130:
        print("Are you really that old??")
        print()
        return "invalid ticket price"
    
    else:
        # finds out ticket price 
        if age > 64:
            ticket_price = 6.5
        elif age < 16:
            ticket_price = 7.5
        else:
            ticket_price = 10.5
        return ticket_price


# currenecy formatting function
def currencey(x):
    return "${:.2f}".format(x)


# *** main routine ***
# regular expression to find if item starts with a number
number_regex = "^[1-9]"

# errors list
snack_error = "<error> Please enter 1 of the 4 snack options."
yes_no_error = "<error> please enter yes or no."

# yes no list
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]

# list of valid response for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]


# defines constants 
MAX_TICKETS = 5

# defines variables
name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists (to make data-frame)
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

surcharge_multi_list = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# lists to store sumamry data
# summary_headings = ["Popcorn", 'M&Ms', "Pita Chips", 'Water',
# "Orange Juice", 'Snack Profit', "ticket Price", "Total Profit"]

summary_headings = ["Popcorn", 'M&Ms', "Pita Chips", 'Water',
"Orange Juice", "Snack Profit", "ticket Price", "Total Profit"]

summary_data = []

# summary data dict
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Tickets': all_tickets,
    'Popcorn': popcorn,
    'M&Ms': mms,
    'Pita Chips': pita_chips,
    'Water': water,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_multi_list
    
}

# price dictionary
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# loop code where it asks user for details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # ask user for name 
    name = not_blank("Name: ", "<error> please enter your name")

    if name == "xxx":
        print()
        break

    # finds out ticket cost
    # and makes sure age is valid
    ticket_cost = ticket_price()
    if ticket_cost == "invalid ticket price":
        continue
    else:   
        # totals the ticket sales
        ticket_sales += ticket_cost
        print("Ticket Price: ${:.2f} ".format(ticket_cost))
        print()
        ticket_count += 1

    # adds name and ticket price to the initail listd
    all_names.append(name)
    all_tickets.append(ticket_cost)


    # gets order if they want one
    get_order = get_snack()
    print()
   
    # fill lists
    for item in snack_lists:
        item.append(0)
        
    # add stuf to the lists if they ask for an order.
    for item in get_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # ask user for there payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit): ").lower()
        how_pay = string_checker(how_pay, "<error> please input correct payment method.", pay_method)

    # do maths to figure our surcharge
    if how_pay == "Credit":
        surcharge_multiplier = 0.05 
    
    else:
        surcharge_multiplier = 0

    surcharge_multi_list.append(surcharge_multiplier)

    # finds out amount of tickets left
    ticket_check(ticket_count, MAX_TICKETS)
    print()

# Print information
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and ticket

movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']


movie_frame["Sub total"] = \
    movie_frame['Tickets'] + \
    movie_frame['Snacks']

movie_frame["Surcharge"] = \
    movie_frame["Sub total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub total"] + \
    movie_frame['Surcharge']

movie_frame = movie_frame.reindex(columns=['Tickets', 'Snacks', 'Popcorn', 'Pita Chips', 'M&Ms', 'Orange Juice', 'Water', 'Sub total', 'Surcharge', 'Total'])


# set up summary dataframe
# populate snack items...
for item in snack_lists:
    # sum itmer in each snack list 
    summary_data.append(sum(item))

# Get snack Profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2

# calculate ticket and total profit
tiket_profit = ticket_sales - (5 * ticket_count)
total_profit = snack_profit + tiket_profit

# appends profit data to lists
dollar_ammounts = [snack_profit, tiket_profit, total_profit]
for i in dollar_ammounts:
    i = "${:.2f}".format(i)
    summary_data.append(i)

# create summar frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# set max coumns to be printed..
pandas.set_option('display.max_columns', None)

# pre printing / export
# format currency valuse so they have $
add_dollars = ['Tickets', 'Snacks', 'Surcharge', 'Total', 'Sub total']
for i in add_dollars:
    movie_frame[i] = movie_frame[i].apply(currencey)

# write each fram to a seperate csv file
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")

print()
print("*** Ticket / Snack Information ***")
print("Note: For full details please see the excel file called ")
print()
print(movie_frame[['Tickets', 'Snacks', 'Sub total', "Surcharge", 'Total']])
print()

print('*** Snack / Profit Sumamry ***')
print()
print(summary_frame)
print()

# if you've sold put it prints that
if ticket_count == MAX_TICKETS:
    print("You have sold out")

# if you have not sold out it tells you how many sold and left
else:
    print("You sold {} tickets.".format(ticket_count))
    print("{} spaces remain.".format(MAX_TICKETS - ticket_count))
print()

# shows profit made 
print("Profit: {:.2f}".format(tiket_profit))

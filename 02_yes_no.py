def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            
            elif response == var_item[0]:
                return var_item

        print('Please enter either yes or no...\n')



# main routine
# asks user if they want snacks 
for i in range(1, 6):
    want_help = yes_no("Would you like to read instructions? ")
    print("Answer: {}\n".format(want_help))



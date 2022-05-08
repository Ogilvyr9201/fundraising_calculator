# Functions go here


# Number checker to make sure user inputs correctly
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
                    return 

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


# main routine
# ask user for there age

while 1 == 1:
    amount = num_check("How much do you need? ", "<error> please enter an interger above 0.", int, None, 0)
    print()
    cost = num_check("How much do it cost? $", "<error> please enter cost.", float, None, 0)
    print()
    print("Amount of Items: {}  Cost of Item: {}".format(amount, cost))
    print()
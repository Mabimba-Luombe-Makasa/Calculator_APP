# Application title amd tagline
print("Welcome to the Easy Command Line Calculator.")
print("Make simple calculations like addition, subtraction, multiplication, and division.\n")


# This function offers addition
def addition_formula(option_1, option_2):
    sum_answer = option_1 + option_2
    print("The sum of those two numbers is:", sum_answer, "\n")


# This function is for subtraction
def subtraction_formula(option_1, option_2):
    sub_answer = option_1 - option_2
    print("The difference of those two numbers is:", sub_answer, "\n")


# This function is for multiplication
def multiplication_formula(option_1, option_2):
    multiply_answer = option_1 * option_2
    print("The product of those two numbers is:", multiply_answer, "\n")


# This function is for division
def division_formula(option_1, option_2):
    # This If-Else Statement ensure there are errors if user divides by 0
    if option_2 == 0:
        print("Error: Division by zero is not allowed.\n")
    else:
        divide_answer = option_1 / option_2
        print("The division of those two numbers is:", divide_answer, "\n")


# While and Try-Except statements ensure user doesnt have errors if they enter a non-numerical character
while True:
    try:
        # This is the option menu
        user_selection = int(input("Press 1 for ADDITION.\n"
                                   "Press 2 for SUBTRACTION.\n"
                                   "Press 3 for MULTIPLICATION.\n"
                                   "Press 4 for DIVISION.\n"
                                   "Press 0 to EXIT.\n"))

        # This if statement is for addition and has error handling
        if user_selection == 1:
            while True:
                try:
                    option_1 = int(input("Please enter the first number you want to add: \n"))
                    option_2 = int(input("Please enter the second number you want to add: \n"))

                    addition_formula(option_1, option_2)
                    break
                except ValueError:
                    print("Please enter numerical characters.\n")

        # This elif statement is for subtraction and has error handling
        elif user_selection == 2:
            while True:
                try:
                    option_1 = int(input("Please enter the number you want to be the minuend: \n"))
                    option_2 = int(input("Please enter the number you want to be the subtrahend: \n"))

                    subtraction_formula(option_1, option_2)
                    break
                except ValueError:
                    print("Please enter numerical characters.\n")

        # This elif statement is for multiplication and has error handling
        elif user_selection == 3:
            while True:
                try:
                    option_1 = int(input("Please enter the first number you want to multiply: \n"))
                    option_2 = int(input("Please enter the second number you want to multiply: \n"))

                    multiplication_formula(option_1, option_2)
                    break
                except ValueError:
                    print("Please enter numerical characters.\n")

        # This if statement is for division and has error handling
        elif user_selection == 4:
            while True:
                try:
                    option_1 = int(input("Please enter the number you want to be the dividend: \n"))
                    option_2 = int(input("Please enter the number you want to be the divisor: \n"))

                    division_formula(option_1, option_2)
                    break
                except ValueError:
                    print("Please enter numerical characters.\n")

        # This is the exit option with a goodbye message
        elif user_selection == 0:
            print("Thank you for using the Easy Command Line Calculator. Goodbye...")
            break

        # Error message if user enters in the wrong number
        else:
            print("Invalid selection. Please try again...\n")
    except ValueError:
        print("Please select a numerical option. Try again...\n")

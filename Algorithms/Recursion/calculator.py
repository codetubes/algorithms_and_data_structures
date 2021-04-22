def add_numbers():
    print("Enter First Number")
    number1 = input()

    print("Enter Second number")
    number2=input()

    print(float(number1)+float(number2))


def subtract_numbers():
    print("Enter First Number")
    number1 = input()

    print("Enter Second number")
    number2 = input()

    print(float(number1) - float(number2))

def display_menu():
    print("--> Choose the operation <--")
    print("1. Add Numbers")
    print("2. Subtract Number")

    operation = input()

    if operation == "1":
        return add_numbers()
    elif operation == "2":
        return subtract_numbers()
    else:
        print("Wrong operation entered. pls try again")
        display_menu()

display_menu()





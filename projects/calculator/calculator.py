from replit import clear
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    number1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    wanna_continue = True

    while wanna_continue:
        selected_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))

        if selected_symbol in operations:
            calculation_function = operations[selected_symbol]
            result = calculation_function(number1, number2)
            print(f"{number1} {selected_symbol} {number2} = {result}")

            if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
                number1 = result
            else:
                wanna_continue = False
                clear()
                calculator()
        else:
            print('Invalid operator selected!')
            wanna_continue = False


calculator()

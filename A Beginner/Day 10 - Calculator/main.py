def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculadora():
    do_it_again = True
    first_number = float(input("What's the first number?\n"))

    while do_it_again:
        for symbols in operations:
            print(symbols)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?\n"))
        resultado = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {resultado}")
        choice = input(f"Type 'y' to continue calculating with {resultado}, or type 'n' to start a new calculation:\n").lower()
        if choice == "y":
            first_number = resultado
        else:
            do_it_again = False
            print("Goodbye!")
            calculadora()

        # angel = operations.get("+")
        # print(angel(2,30))

calculadora()
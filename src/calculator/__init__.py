from src.operations import addition, subtraction, multiplication, division
MAN_STRING = """This calculator supports (+)addition, (-)subtraction, (*) multiplicaiton and (/)division
    Enter two numbers with an operator between. ex: num1 + num2"""

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""
    
    
    #print message to welcome user to calculator
    print("Welcome to the calculator REPL! type 'exit' to quit or 'man' for instructions\n" + MAN_STRING)
    
    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break
        if user_input.lower() == "man":
            print(MAN_STRING)
            continue

        try:
            # Now we split the input into three parts: the operation (add, subtract, etc.) and the two numbers.
            num1, operator, num2 = user_input.split()
            # We have to make sure the numbers are actually numbers, so we convert them to floats.
            num1, num2 = float(num1), float(num2)
        except ValueError:
            # If the user doesn't type something correctly, like typing letters where numbers should be, we show an error.
            print("Invalid input. Please follow the format:  <num1> <operator> <num2>")
            continue

        # Now we check what operation the user asked for and call the right function (addition, subtraction, etc.).
        if operator == "+":
            result = addition(num1, num2)  # We call the addition function to add the two numbers.
        elif operator == "-":
            result = subtraction(num1, num2)  # We call the subtraction function to subtract the two numbers.
        elif operator == "*":
            result = multiplication(num1, num2)  # We call the multiplication function to multiply the two numbers.
        elif operator == "/":
            try:
                result = division(num1, num2)  # We call the division function to divide the two numbers.
            except ValueError as e:
                # This part handles the case where someone tries to divide by zero, which we can't do.
                # The division function will throw an error if someone tries dividing by zero, and we catch that error here.
                print(e)  # Show the error message.
                continue  # Go back to the top of the loop and try again.
        else:
            # If the user types an operation we don't understand, we show them a message.
            print(f"Unknown operator '{operator}'. Supported operations: (+)add, (-)subtract, (*)multiply, (/)divide.")
            continue  # Go back to the top of the loop and try again.

        print(f"Result: {result}")
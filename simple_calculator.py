print("Enter number to calculate:")
li = []  # List to store numbers entered by the user
operators = []  # List to store operators entered by the user

while True:
    num1 = float(input("Enter number: "))  # Taking numerical input from the user
    li.append(num1)  # Adding number to the list

    oper = input("Enter operator (+, -, *, /) or '=' to calculate: ")  # Taking operator input
    
    if oper in ['+', '-', '*', '/']:  # If operator is valid, store it
        operators.append(oper)
    elif oper == '=':  # If '=' is entered, stop taking inputs and proceed to calculation
        break  
    else:
        print("Invalid operator! Please enter a valid operator.")  # Error handling for invalid input

# Performing Calculation
result = li[0]  # Initialize result with the first number from the list

for i in range(1, len(li)):  # Loop through remaining numbers
    if operators[i - 1] == '+':  # Check the previous operator in the list
        result += li[i]  # Add current number if previous operator was '+'
    elif operators[i - 1] == '-':  # Check if previous operator was '-'
        result -= li[i]  # Subtract current number from result
    elif operators[i - 1] == '*':  # Check if previous operator was '*'
        result *= li[i]  # Multiply result by current number
    elif operators[i - 1] == '/':  # Check if previous operator was '/'
        result /= li[i]  # Divide result by current number

print("Final Result:", result)  # Display the calculated result

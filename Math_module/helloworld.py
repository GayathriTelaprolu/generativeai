import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python helloworld.py <number1> <number2>")
    sys.exit(1)

# Get the two numbers from command-line arguments
try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except ValueError:
    print("Error: Please enter valid numbers")
    sys.exit(1)

# Add the two numbers
result = num1 + num2

# Print the result
print(f"The sum of {num1} and {num2} is: {result}")

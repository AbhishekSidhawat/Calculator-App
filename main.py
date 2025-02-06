def add(numbers):
    """Adds all the numbers in the list."""
    return sum(numbers)

def subtract(numbers):
    """Subtracts all the numbers in the list from the first number."""
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result    

def multiply(numbers):
    """Multiplies all the numbers in the list."""
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    """Divides the first number by all other numbers in the list."""
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! You cannot divide by zero."
        result /= num    
    return result

def calculator():
    """Runs the calculator and prompts the user for input."""
    print("Welcome to the calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("\nChoose an operation (1-5): ")

        if choice == "5":
            print("Exiting calculator, goodbye!")
            break 

        if choice in ["1", "2", "3", "4"]: 
            try:
                n = int(input("How many numbers do you want to calculate? "))
                numbers = []  # Store user inputs as a list
                for i in range(n):
                    num = float(input(f"Enter number {i+1}: "))
                    numbers.append(num)

                if choice == "1":
                    print(f"Result: {add(numbers)}")   
                elif choice == "2":
                    print(f"Result: {subtract(numbers)}")
                elif choice == "3":
                    print(f"Result: {multiply(numbers)}") 
                elif choice == "4":
                    print(f"Result: {divide(numbers)}")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice! Please enter a number from 1 to 5.")

# Start the calculator
calculator()

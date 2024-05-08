def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero!"
    else:
        return x / y


def save_calculation(calculation, result):
    with open("calculations.txt", "a") as file:
        file.write(calculation + " = " + str(result) + "\n")


def display_file_contents():
    with open("calculations.txt", "r") as file:
        print(file.read())


def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Display file contents")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ("1", "2", "3", "4"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                save_calculation(f"{num1} + {num2}", result)
                print("Result:", result)
            elif choice == "2":
                result = subtract(num1, num2)
                save_calculation(f"{num1} - {num2}", result)
                print("Result:", result)
            elif choice == "3":
                result = multiply(num1, num2)
                save_calculation(f"{num1} * {num2}", result)
                print("Result:", result)
            elif choice == "4":
                result = divide(num1, num2)
                save_calculation(f"{num1} / {num2}", result)
                print("Result:", result)
        elif choice == "5":
            print("\nFile contents:")
            display_file_contents()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    calculator()

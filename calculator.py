# Defining color codes
COLORS = {
    "RED": 31,
    "GREEN": 32,
    "YELLOW": 33,
    "BLUE": 34,
    "MAGENTA": 35,
    "CYAN": 36,
    "WHITE": 37
}


def color_text(text, color_name):
    color_code = COLORS.get(color_name.upper(), COLORS["WHITE"])  # Default to white if color_name not found.
    return f"\033[{color_code}m{text}\033[0m"


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print(color_text("Error: Division by zero", "RED"))
        return None
    return x / y


def power_of(x, y):
    return x ** y


def modulus(x, y):
    return x % y


def is_prime(number):
    try:
        number = int(number)  # Attempt to convert to int, in case it's not.
    except ValueError:
        return False

    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_odd_even(number):
    return "Odd" if number % 2 else "Even"


def is_div_by_five(number):
    return number % 5 == 0


def validate_input(input_str):
    # Splitting the input and removing spaces.
    parts = input_str.strip().split()

    # Check if exactly two elements (numbers) are present after splitting.
    if len(parts) != 2:
        return None, color_text("Error: Please enter exactly two numbers separated by space.", "RED")

    try:
        # Convert parts to integers.
        numbers = list(map(int, parts))
        return numbers, None
    except ValueError:
        return None, color_text("Invalid input. Please enter integers only.", "RED")


def get_operation_args(operation):
    if operation in ['a', 'b', 'c', 'd', 'f']:
        input_str = input(color_text("Enter two numbers separated by space: ", "BLUE"))
    elif operation == 'e':
        input_str = input(color_text("Enter the base and exponent separated by space: ", "BLUE"))
    else:
        return None, "Invalid operation"

    return validate_input(input_str)


def display_menu():
    print(color_text("\nCalculator Menu:", "GREEN"))
    menu_options = ["a. Add", "b. Subtract", "c. Multiply", "d. Divide", "e. Power of", "f. Modulos", "g. Exit"]
    for option in menu_options:
        print(color_text(option, "CYAN"))


def handle_operation(operation, x, y):
    operations = {
        'a': add,
        'b': subtract,
        'c': multiply,
        'd': divide,
        'e': power_of,
        'f': modulus,
    }
    result = operations[operation](x, y)

    if result is not None:
        print(color_text(f"\nResult: {result}", "MAGENTA"))
        print("Prime Number:", color_text("Yes" if is_prime(result) else "No", "YELLOW"))
        print("Odd/Even:", color_text(is_odd_even(result), "YELLOW"))
        print("Divisible by 5:", color_text("Yes" if is_div_by_five(result) else "No", "YELLOW"))
    else:
        print(color_text("Operation could not be completed.", "RED"))


def main():
    while True:
        display_menu()
        choice = input(color_text("Choose an operation: ", "GREEN")).lower().strip()
        if choice == 'g':
            print(color_text("Exiting...", "RED"))
            break
        elif choice in ['a', 'b', 'c', 'd', 'e', 'f']:
            args, error = get_operation_args(choice)
            if error:
                print(error)
                continue
            handle_operation(choice, *args)
        else:
            print(color_text("Invalid choice. Please select a valid operation.", "RED"))


if __name__ == "__main__":
    main()

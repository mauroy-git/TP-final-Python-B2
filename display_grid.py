print("Welcome to la Vie de Conway")
print("Please enter grid size min 5 / max 63 to continue...")

def get_valid_input(dialog, min_size=5, max_size=63):
    while True:
        value = input(dialog)
        try:
            int_value = int(value)
            if min_size <= int_value <= max_size:
                return int_value
            else:
                print(f"Error: Please enter a number between {min_size} and {max_size}.")
        except ValueError:
            print("Error: Please enter a valid number (digits only).")

input_rows = get_valid_input("Enter number of rows: ")
input_columns = get_valid_input("Enter number of columns: ")

print("Loading...")
def safe_divide():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter tne denominator: "))
        result = numerator / denominator
    except ZeroDivisionError:
        print("You can't devide by zero")
    except ValueError:
        print("numerator and denominator must be numeric")
    else:
        print(f"The result is {result}")
    finally:
        print("Operation finished.")

def timer(func):
    import time
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # print(f"{func.__name__} took {end - start} seconds")
        return f"{result} \n{func.__name__} took {end - start} seconds"
    return wrapper


@timer
def read_number():
    try:
        num = int('as')
    except ValueError:
        print("That is not a valid integer.")
        return None
    else:
        print("Conversion successful.")
        return num
    
# Write a function get_item_from_list() that:
# Has a predefined list inside it, e.g. items = ["apple", "banana", "cherry"]
# Asks the user for an index number.
# Tries to print the item at that index using a try block.
# Handles:
# ValueError — if the user enters something that’s not an integer.
# IndexError — if the index is out of range.
# Uses else to print "Item retrieved successfully!"
# Uses finally to print "Operation complete."
# Then explain (in English, 2–3 sentences):
# Why we need two different except blocks here.
# What kind of error happens if you input "a" instead of a number.

def get_item_from_list():
    items = ["apple", "banana", "cherry"]
    try:
        index_input = input("Enter an index number: ")
        index = int(index_input)
        print(items[index])
    except ValueError:
        print("That is not a valid integer.")
        return None
    except IndexError:
        print("Index out of range.")
        return None
    else:
        print("Item retrieved successfully!")
    finally:
        print("Operation complete.")

# print(get_item_from_list())

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError
        balance -= amount
        print(f"New balance: {balance}")
        # return f"New balance: {balance}"
    except ValueError:
        print("Insufficient funds.")
    finally:
        print("Transaction finished.")

# withdraw(100, 101)

def safe_file_read(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("Unexpected error occurred.")

    else:
        print("File read successfully.")

    finally:
        print("Operation complete.")
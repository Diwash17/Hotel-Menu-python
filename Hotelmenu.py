
import json

def load_menu(file_path):
    """
    Load the menu from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing the menu.

    Returns:
        dict: A dictionary representing the menu, where keys are item names and values are prices.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def display_menu(menu):
    """
    Display the menu to the user.

    Args:
        menu (dict): A dictionary representing the menu, where keys are item names and values are prices.
    """
    print("Welcome to Quality Food Restaurant")
    print("Here is the menu:")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")

def take_order(menu):
    """
    Take the order from the user and calculate the total amount.

    Args:
        menu (dict): A dictionary representing the menu, where keys are item names and values are prices.

    Returns:
        tuple: The total amount for the order and the list of ordered items.
    """
    order_total = 0
    order_items = []
    while True:
        item = input("Enter the name of item you want to order (or type 'No' to finish): ").capitalize()
        if item == "No":
            if order_total == 0:
                print("You must order at least one item.")
                continue
            else:
                print("Thank you for your order!")
                break
        elif item in menu:
            while True:
                try:
                    quantity = int(input(f"How many {item}s do you want to order? "))
                    if quantity <= 0:
                        print("Please enter a valid quantity greater than zero.")
                    else:
                        order_total += menu[item] * quantity
                        order_items.append((item, quantity, menu[item] * quantity))
                        print(f"{quantity} {item}(s) has been added to your order.")
                        break 
                except ValueError:
                    print("Please enter a valid number for quantity.")
        else:
            print(f"Sorry, {item} is not available in our menu.")
    return order_total, order_items

def calculate_discount(order_total):
    """
    Calculate the discount based on the total order amount.

    Args:
        order_total (float): The total amount for the order.

    Returns:
        tuple: The total amount after applying the discount and the discount amount.
    """
    discount = 0
    if order_total > 2500:
        discount = order_total * 0.2
        order_total -= discount
        print("Congratulations! You have received a 20% discount.")
        print(f"Discount amount: Rs{discount}")
    elif order_total > 1000:
        discount = order_total * 0.1
        order_total -= discount
        print("Congratulations! You have received a 10% discount.")
        print(f"Discount amount: Rs{discount}")
    else:
        print("Order food worth more than 1000 to get exciting discount.")
    return order_total, discount

def calculate_final_price(order_total):
    """
    Calculate the final price including VAT.

    Args:
        order_total (float): The total amount for the order after applying any discounts.

    Returns:
        tuple: The final amount to be paid including VAT and the VAT amount.
    """
    vat = order_total * 0.13
    final_price = order_total + vat
    print("You need to pay 13% VAT according to the rule.")
    return final_price, vat

def print_receipt(final_price):
    """
    Print the final receipt with the total amount to be paid.

    Args:
        final_price (float): The final amount to be paid including VAT.
    """
    print(f"The total amount of items to pay is Rs{final_price}")

def save_receipt_as_text(order_items, order_total, discount, vat, final_price, file_path):
    """
    Save the receipt as a text file.

    Args:
        order_items (list): A list of tuples representing ordered items.
        order_total (float): The total amount for the order after applying the discount.
        discount (float): The discount amount.
        vat (float): The VAT amount.
        final_price (float): The final amount to be paid including VAT.
        file_path (str): The path to the text file where the receipt will be saved.
    """
    with open(file_path, 'w') as file:
        file.write('Welcome to Quality Food Restaurant\n')
        file.write('Receipt\n')
        file.write("-"*25+ "\n")
        for item, quantity, price in order_items:
            file.write(f"{item} x{quantity}: Rs{price}\n")
        file.write("-"*25+ "\n")
        file.write(f"Total before discount: Rs{order_total + discount}\n")
        file.write(f"Discount: -Rs{discount}\n")
        file.write(f"VAT (13%): Rs{vat}\n")
        file.write("-"*25+ "\n")
        file.write(f"Total to pay: Rs{final_price}\n")


from Hotelmenu import *

def main():
    """
    Main function to coordinate the flow of the program.
    """
    menu = load_menu('Menu.json')
    display_menu(menu)
    order_total, order_items = take_order(menu)
    order_total, discount = calculate_discount(order_total)
    final_price, vat = calculate_final_price(order_total)

    receipt_text_path = 'receipt.txt'
    save_receipt_as_text(order_items, order_total, discount, vat, final_price, receipt_text_path)
    
    print(f"The total amount of items to pay is Rs{final_price}")
    print(f"Receipt has been saved as a text file to {receipt_text_path}")

if __name__ == "__main__":
    main()


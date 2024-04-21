menu = {
    "Momo": 140,
    "Pizza": 180,
    "Coffee": 110,
    "Cold Drink": 70,
    "Chowemin": 120,
    "Burger": 160,
}

print("Welcome to Quality Food Restaurant")
print("""Pizza: Rs180
Coffee: Rs110
Cold Drink: Rs70
Chowemin: Rs120
Burger: Rs160
Momo: Rs140""")

order_total = 0
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
                    print(f"{quantity} {item}(s) has been added to your order.")
                    break  # Exit the inner loop if a valid quantity is entered
            except ValueError:
                print("Please enter a valid number for quantity.")
    else:
        print(f"Sorry, {item} is not available in our menu.")




if order_total > 1000:
    discount = order_total * 0.1
    order_total -= discount
    print("Congratulations! You have received a 10% discount.")
    print(f"Discount amount: Rs{discount}")



print(f"The total amount of items to pay is Rs{order_total}")

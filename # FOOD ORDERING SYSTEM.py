# FOOD ORDERING SYSTEM
# Python Mini Project

menu = {
    1: {"name": "Pizza", "price": 250},
    2: {"name": "Burger", "price": 120},
    3: {"name": "Biryani", "price": 200},
    4: {"name": "Fried Rice", "price": 150},
    5: {"name": "Noodles", "price": 130},
    6: {"name": "French Fries", "price": 100},
    7: {"name": "Ice Cream", "price": 80},
    8: {"name": "Cold Drink", "price": 50}
}

cart = []


# Display menu
def display_menu():
    print("\n========== FOOD MENU ==========")

    for number, item in menu.items():
        print(f"{number}. {item['name']} - ₹{item['price']}")

    print("===============================")


# Add item to cart
def add_to_cart():
    display_menu()

    try:
        choice = int(input("Enter food number: "))

        if choice not in menu:
            print("Invalid food number!")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        item = menu[choice]

        cart.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity
        })

        print(f"{quantity} x {item['name']} added to cart!")

    except ValueError:
        print("Please enter a valid number.")


# View cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n============= CART =============")

    total = 0

    for i, item in enumerate(cart, start=1):
        amount = item["price"] * item["quantity"]
        total += amount

        print(
            f"{i}. {item['name']} | "
            f"₹{item['price']} x {item['quantity']} = ₹{amount}"
        )

    print("--------------------------------")
    print(f"Total Amount: ₹{total}")
    print("================================")


# Calculate bill
def calculate_bill():
    if not cart:
        print("\nCart is empty!")
        return 0

    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["quantity"]

    # 5% GST
    gst = subtotal * 0.05

    total = subtotal + gst

    print("\n========== BILL ==========")
    print(f"Subtotal : ₹{subtotal:.2f}")
    print(f"GST 5%   : ₹{gst:.2f}")
    print("--------------------------")
    print(f"Total    : ₹{total:.2f}")
    print("==========================")

    return total


# Place order
def place_order():
    if not cart:
        print("\nPlease add items to cart first.")
        return

    print("\n========== ORDER ==========")

    name = input("Enter your name: ")
    phone = input("Enter phone number: ")
    address = input("Enter delivery address: ")

    total = calculate_bill()

    print("\nOrder placed successfully!")
    print("--------------------------")
    print("Customer :", name)
    print("Phone    :", phone)
    print("Address  :", address)
    print(f"Amount   : ₹{total:.2f}")
    print("Status   : Order Confirmed")
    print("===========================")


# Order status
def order_status():
    if not cart:
        print("\nNo order has been placed.")
        return

    print("\n========== ORDER STATUS ==========")
    print("Order Status: Confirmed")
    print("Restaurant Status: Preparing")
    print("Delivery Status: Waiting for pickup")
    print("==================================")


# Main program
def main():

    while True:

        print("\n")
        print("====================================")
        print("       FOOD ORDERING SYSTEM")
        print("====================================")
        print("1. Display Menu")
        print("2. Add Items to Cart")
        print("3. View Cart")
        print("4. Calculate Bill")
        print("5. Place Order")
        print("6. Order Status")
        print("7. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            view_cart()

        elif choice == "4":
            calculate_bill()

        elif choice == "5":
            place_order()

        elif choice == "6":
            order_status()

        elif choice == "7":
            print("\nThank you for using Food Ordering System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Start program
if __name__ == "__main__":
    main()
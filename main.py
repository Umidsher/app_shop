from login import login


def get_products():
    products = {
        'Laptop': 1200,
        'Smartphone': 800,
        'Tablet': 150,
        'Camera': 400,
        'Monitor': 250,
        'Keyboard': 100,
        'Mouse': 50,
        'Printer': 200
    }
    return products


def display_products():
    products = get_products()
    print("\nAvailable Products and Prices:")
    for product, price in products.items():
        print(f"{product}: ${price:.2f}")


def main():
    if login():
        display_products()
    else:
        print("Failed to log in. Please try again.")


if __name__ == "__main__":
    main()

cart = {}


def add_to_cart(product, quantity):
    if product in get_products():
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity
        print(f"Added {quantity} of {product} to the cart.")
    else:
        print("Product not available.")


def show_products_and_add_to_cart():
    products = get_products()
    print("\nAvailable Products:")
    for idx, (product, price) in enumerate(products.items(), 1):
        print(f"{idx}. {product} - ${price:.2f}")

    choice = int(input("Enter the number of the product you want to add to the cart: "))
    product_list = list(products.keys())

    if 1 <= choice <= len(product_list):
        product = product_list[choice - 1]
        quantity = int(input(f"Enter the quantity for {product}: "))
        add_to_cart(product, quantity)
    else:
        print("Invalid product selection.")


def main():
    if login():
        display_products()
        while True:
            show_products_and_add_to_cart()
            continue_shopping = input("Do you want to continue shopping? (yes/no): ")
            if continue_shopping.lower() != 'yes':
                break
        # tax_rate = 6
        # tax = round(tax_rate/100.0*(get_products.value), 2)
        print("\nYour cart:")
        for product, quantity in cart.items():
            print(f"{product}: {quantity}")
    else:
        print("Failed to log in. Please try again.")


if __name__ == "__main__":
    main()

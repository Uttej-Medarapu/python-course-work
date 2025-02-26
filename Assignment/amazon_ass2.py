# Taking user input for Amazon product details

product_name = input("Product Name: ")  # String
product_price = float(input("Price of the product: "))  # Float
best_seller_rank = int(input("Best Seller Rank: "))  # Integer
categories = tuple(input("Product Categories (comma-separated): ").split(','))  # Tuple
available_colors = list(input("Available Colors (comma-separated): ").split(','))  # List
features = set(input("Key Features (comma-separated): ").split(','))  # Set
stock_info = eval(input("Stock Info (Dictionary Format {'Amazon': 50, 'Seller A': 30}): "))  # Dictionary
is_available = bool(int(input("Is it available? (1 for Yes, 0 for No): ")))  # Boolean

# Displaying product details using different print statements
print("\n--- Amazon Product Details ---\n")
print("Product Name:", product_name)
print(f"Price: ₹{product_price:.2f}")
print("Best Seller Rank:", best_seller_rank)
print("Categories:", ', '.join(categories))
print("Available Colors:", available_colors)
print(f"Features: {features}")
print("Stock Info:", stock_info)
print("Availability:", "In Stock" if is_available else "Out of Stock")

# Using a formatted multi-line print
print("""
------ Summary ------
Product: {}
Price: ₹{}
Categories: {}
Best Seller Rank: {}
Available Colors: {}
Features: {}
Stock Availability: {}
""".format(product_name, product_price, categories, best_seller_rank, available_colors, features, stock_info))

# Using *args to unpack and print tuple
print("Product Categories:", *categories, sep=", ")

# Using a loop for a better display format
print("\nStock Details:")
for seller, stock in stock_info.items():
    print(f"{seller}: {stock} units available")

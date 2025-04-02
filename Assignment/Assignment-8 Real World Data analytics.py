import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta


productprices = pd.Series(
    [29999, 35999, 52999, 14999, 19999],  
    index=["Wireless Earbuds", "Smartphone", "Laptop", "Smartwatch", "Bluetooth Speaker"]
)
print("Product Prices:\n", productprices)

# Generate Sales Data
products = list(productprices.index) 
startdate = datetime(2024, 10, 10)  
salesdata = []  

for i in range(100):  
    saledate = startdate + timedelta(days=random.randint(0, 100)) 
    product = random.choice(products) 
    salesprice = productprices[product] * random.randint(1, 5)  
    salesdata.append([saledate, product, salesprice])  


df = pd.DataFrame(salesdata, columns=["Date", "Product", "Sales"])
df["Date"] = pd.to_datetime(df["Date"])  # converting to date format
df["Month"] = df["Date"].dt.strftime("%B") 

# Total Sales,Best-Selling
totalsales = df["Sales"].sum() 
bestproduct = df.groupby("Product")["Sales"].sum() 
monthlysales = df.groupby("Month")["Sales"].sum()  


# Step 4: Print Results
print(f"Total Revenue: {totalsales: }")  
print(f"Best-Selling Product: {bestproduct}")


# Line Graph
plt.figure(figsize=(8, 5))
plt.plot(monthlysales.index, monthlysales.values, marker='o', linestyle='-', color='red')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

#Bar Graph
product_sales = df.groupby("Product")["Sales"].sum()
plt.figure(figsize=(8, 5))
plt.bar(product_sales.index, product_sales.values, color=['red', 'green', 'blue', 'purple', 'orange'])
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

import matplotlib.pyplot as plt

# Pie Chart
plt.figure(figsize=(8, 5))
plt.pie(product_sales.values, labels=product_sales.index, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'purple', 'orange'])
plt.title("Sales Distribution by Product")
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Sales"], bins=10, color='blue', edgecolor='black')
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid()
plt.show()


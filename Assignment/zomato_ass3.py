print("Welcome to \n Zomato Food Delivery App") 

#user login

d={'uttej':'1234','ravi':'1111'}
a=input("enter user name:")
if a in d.keys():
    print("correct user name ")
b=input("enter password:")
if d[a] == b :
    print("login successful")

#application details
    restaurants = ["Domino's", "KFC", "McDonald's", "Pizza Hut"] #list
    print("Available Restaurants:", restaurants)
    delivery_areas = {"Hyderabad", "Mumbai", "Bangalore", "Delhi"} #set
    print("Our delivery_areas are:",delivery_areas)
    food_items= {"Pizza": 250,"Burger": 150,"Pasta": 200,"Fries": 100,"Coke": 50}
    print(f"at present,available stocks are:{food_items}")

#ordering food

    order = input("\nEnter the food item you want to order: ")
    units = int(input("\n enter the items do you need:"))
    if order in food_items and (units>=1):
        print(f"\nyour {order} of {units} pieces are booked")
        print("\nThank you for ordering with Zomato!")
    else:
        print("sorry,we don't have stock")
#wrong password
else:
    print("wrong password,try again")
#goodbye wishes
print("\nThank you for choosing Zomato,,visit again")

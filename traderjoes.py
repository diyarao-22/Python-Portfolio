#TraderJoes

#init
import pandas as pd
data = pd.read_csv("tjsnacks.csv")
import webbrowser
id = data["Row"].tolist()
name = data["Snack Name"].tolist()
flavor = data["Flavor"].tolist()
orientation = data["Orientation"].tolist()
price = data["Price"].tolist()
image = data["Image"].tolist()

filter = []

#functions
def price_search(snack): #this function is used for users to input a snack and find out the price of that snack
    tracker = "x"
    for i in range(len(name)):
        if snack in name[i]:
            print(" *** Love Those! ***")
            filter.append(id[i])
            filter.append(name[i])
            filter.append(price[i])
            tracker = "y"
    if tracker == "x":
        print("No results found. Try a different snack")
    print(filter)
    filter.clear()
def orientationsearch(type): #This functions asks the user for a certain orientation of snack they would like and they will receive various options to choose from
    othertracker = "x"
    for i in range(len(name)):
        if type in orientation[i]:
            filter.append(name[i])
            othertracker = "y"
    if othertracker == "x":
        print("No type of snack found. Try a different type. For example: chip, popcorn, pretzel, rice cake, candy, cluster")
    print(filter)
    filter.clear()
def snack_search(profile):#this function is used for users to insert a flavor of a snack they would like to choose and it will recommend various options of that flavor to choose from
    tracker = "x"
    for i in range(len(name)):
        if profile in flavor[i]:
            filter.append(name[i])
            tracker = "y"
    if tracker == "x":
        print("No flavor profile found. Try a different flavor. For example: salty, sweet, spicy, sour")
    print(filter)
    filter.clear()
def snack_img_search(title): #this function is used for users to input a snack name they would like to see the look of and the function will display a picture of that snack
    thirdtracker = "x"
    for i in range(len(name)):
        if title in name[i]:
            webbrowser.open(image[i])
            thirdtracker = "y"
    if thirdtracker == "x":
        print ("No snack found. Try a different snack")
def menu():# this menu is used for users to pick an
    print("---------------------------------------------------------------------------------------------------------")
    print("Welcome to your Trader Joe's snack search! We are at your service to help you pick your future favorite!")
    print("---------------------------------------------------------------------------------------------------------")
    while True:
        print(""" *** MENU ***
    Option 1: Search your favorite snacks to find the prices!
    Option 2: Find the names of snacks based off of its orientation (i.e. chips, popcorn, pretzels, etc.)
    Option 3: Find the names of snacks based off of its flavor (i.e. salty, sweet, sour, etc.)
    Option 4: Search your favorite snacks to find the images!
    Option 5: Leave the snack search"""
            )
        print("---------------------------------------------------------------------------------------------------------")
        option = input("Please indicate which option you would like [1, 2, 3, 4, 5] :  ").strip()
        if option == "1":
            print("--------------------------------------------------------------------")
            snack = input(f"""What snack would you like to search the price for?

{name}:  """).title()
            print("--------------------------------------------------------------------")
            print(f"Check out to see if price of {snack} sounds good")
            price_search(snack)
            print("--------------------------------------------------------------------")
            continue
        elif option == "2":
            print("--------------------------------------------------------------------")
            type = input(f"What orientation of snack would you like to get recommendations for (Chip, Pretzel, Popcorn, Rice cake, Cluster, Candy, Dried)? ").lower()
            print("--------------------------------------------------------------------")
            print("Love that, Here are some good recommendations!:")
            orientationsearch(type)
            print("--------------------------------------------------------------------")
            continue
        elif option == "3":
            print("--------------------------------------------------------------------")
            profile = input("What flavor are you looking for in your snack (Sweet, Salty, Sour, Spicy)? ").lower()
            print("--------------------------------------------------------------------")
            print(" Yummy!,How do these sound!:")
            snack_search(profile)
            print("--------------------------------------------------------------------")
            continue
        elif option == "4":
            print("--------------------------------------------------------------------")
            title = input(f"""What snack would you like to see a picture of?

{name}: """).title()
            print("--------------------------------------------------------------------")
            snack_img_search(title)
            print("--------------------------------------------------------------------")
            continue
        elif option == "5":
            print("--------------------------------------------------------------------")
            print("You have exited the snack search. You are now in home. I hope you found something you liked!")
            print("--------------------------------------------------------------------")
            break
        else:
            print("--------------------------------------------------------------------")
            print("Please enter the correct input.")
            print("--------------------------------------------------------------------")

#main
menu()

# Dog breed (create task)
# The purpose of my program is to help users find a dog breed that meets their needs

#initialize
import pandas as pd
data = pd.read_csv("dog.csv")
import webbrowser
id = data["id"].tolist()
name = data["Name"].tolist()
breedgroup = data["Breed Group"].tolist()
bredfor = data["BredFor"].tolist()
minlifespan = data["Minimum Life Span"].tolist()
maxlifespan = data["Maximum Life Span"].tolist()
minheight = data["Minimum Height"].tolist()
maxheight = data["Maximum Height"].tolist()
minweight = data["Minimum Weight"].tolist()
maxweight = data["Maximum Weight"].tolist()
temperament = data["Temperament"].tolist()
image = data["Image"].tolist()

filter = []

#functions
def getDogSize(size):
    if size == "tiny":
        for i in range (len(name)):
            if minweight[i] <= 10:
                filter.append(name[i])
        print(filter)
        filter.clear()
    elif size == "small":
         for i in range (len(name)):
            if minweight[i] >= 11 and minweight[i]<= 25:
                filter.append(name[i])
         print(filter)
         filter.clear()
    elif size == "medium":
         for i in range (len(name)):
            if minweight[i] >= 26 and minweight[i]<= 60:
                filter.append(name[i])
         print(filter)
         filter.clear()
    elif size == "large":
         for i in range (len(name)):
            if minweight[i] > 60:
                filter.append(name[i])
         print(filter)
         filter.clear()

def tempingsearch(breed_name):
    tracker = "x"
    for i in range(len(name)):
        if breed_name in name[i]:
            filter.append(id[i])
            filter.append(name[i])
            filter.append(temperament[i])
            filter.append(image[i])
            webbrowser.open(image[i])
            tracker = "y"
    if tracker == "x":
        print("No results found. Try a different breed")
    print(filter)
    filter.clear()

def bredfortraits(purpose):
    othertracker = "x"
    for i in range(len(name)):
        if purpose in bredfor[i]:
            filter.append(name[i])
            othertracker = "y"
    if othertracker == "x":
        print("No purpose of breeding found. Try a different purpose")
    print(filter)
    filter.clear()
def menu():
    while True:
        print("Welcome to your Dog search let us know what we can do for you today")
        print(""" MENU
    1. Find your dog based off of size in weight
    2. Find the temperament and picture of a breed you are interested in
    3. Find the names of breeds based off of what they were bred for
    4. Leave the dog search site """)
        option = input("please choose an option from the menu [1,2,3,4]: ").strip()
        if option == "1":
            size = input("what size would you like your dog?: tiny, small, medium, or large?: ")
            getDogSize(size)
            continue
        elif option == "2":
            breed_name = input("What dog breed would you like to search for today?: ")
            tempingsearch(breed_name)
            continue
        elif option == "3":
            purpose = input("What purpose are you looking for in a dog?: ")
            bredfortraits(purpose)
        elif option == "4":
            print("You have now exited the dog breed search")
            break
        else:
            print("please enter the correct input")



#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

#main

menu()







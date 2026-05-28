#Madlibs
#Diya

#init
import random
#functions
namess = ["Alexia", "Diya", "frank ocean", "principal dolan", "parsa shoots", "caleb williams"]
foods = ["Beef Bulgogi Fries from En Hakkore", "vodka paste", "crunchwrap supreme", "starbucks grilled cheese"]
apps = ["Doordash", "Tea", "Clash Royale", "Roblox", "spotify"]
items = ["ladder", "record player", "dandelion", "needoh"]


def madlibs():
    name = input("please give a name or enter RANDOM for a randomly generated name: ").upper()
    if name == "RANDOM":
        name = random.choice(namess)
    names = input("please give another name: ").upper()
    verb = input("please enter a past tense verb: ").upper()
    noun = input("please enter a noun: ").upper()
    adjective = input("please enter an adjective: ").upper()
    app = input("please enter a phone app or enter RANDOM for a randomly generated app: ").upper()
    if app == "RANDOM":
        app = random.choice(apps)
    food = input("please enter a food or enter RANDOM for a randomly generated food: ").upper()
    if food == "RANDOM":
        food = random.choice(foods)
    person = input("please enter a person: ").upper()
    adjectives = input("please enter an adjective: ").upper()
    item = input("Please enter an item or enter RANDOM for a randomly generated item: ").upper()
    if item == "RANDOM":
       item = random.choice(items)





    print(f"""\033[1m{name}\033[0m and \033[1m{names}\033[0m went to six flags and \033[1m{verb}\033[0m the biggest \033[1m{noun}\033[0m in the whole wide world. Except, after a while the \033[1m{noun}\033[0m broke down, leaving them upside down in the loop.
           They were very \033[1m{adjective}\033[0m. So, they took their phones out and opened \033[1m{app}\033[0m and ordered \033[1m{food}\033[0m.The door dasher was \033[1m{person}\033[0m! What a surprise.
          \033[1m{person}\033[0m also got \033[1m{adjective}\033[0m and then said "Do not worry I am going to help and then we can eat this \033[1m{food}\033[0m. She got a \033[1m{item}\033[0m, saved the day, and they ate {food} happily ever after.""")
#main
madlibs()

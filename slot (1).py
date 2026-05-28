#Slotmachine
#Diya
#spins the slotmachine and determines results and money

#init
import random

#Functions
list =['✾', '✿', '❁', 7]
weights = [35 ,25 ,15 ,10]
credits = 0
money = 10000
def simulation(): # spins the wheel 1000 times and calculates the final balance of the player
    for i in range (1000):
        output = []
        global money
        money = money - 10
        for i in range(3):
            output.append(random.choices(list, weights = weights, k=1)[0])
        print(output)
        if output == ["✾","✾","✾"] or output == ["✿","✿","✿"] or output == ["❁","❁","❁"]:
            print("WINNERRR!!, 100 CREDITS HAVE BEEN ADDED")
            money = money + 175
        elif output == [7,7,7]:
            print("JACKPOT!!!, 500 CREDITS FOR U")
            money = money + 400
        else:
            print("you lost,spin again")
            money = money - 10
    print(f" you have a balance of {money} credits")



def slotmachine(): #asks the player fi they went to spin the slot machine, then provides the results and their credits
    global credits
    while True:
        spin = input("welcome to the slot machine, would you like to spin the machine, it takes 10 credits: ")
        if spin == "yes":
            credits = credits - 10
            funds()
            deposit()
            print(f"you are now using 10 credits to play, you now have {credits} credits")
            result = [random.choice(list), random.choice(list), random.choice(list)]
            print(result)
            if result == ["✾","✾","✾"] or result == ["✿","✿","✿"] or result == ["❁","❁","❁"]:
                print("WINNERRR!!, 100 CREDITS HAVE BEEN ADDED")
                credits = credits + 100
                continue
            elif result == [7,7,7]:
                print("JACKPOT!!!, 500 CREDITS FOR U")
                credits = credits + 500
                continue
            else:
                print("you lost,spin again")
                continue
        elif spin == "no":
            print("you are now leaving the slot machine")
            break



def deposit(): # calculates the credits based on how many credits the player deposits
    global credits
    deps = input("How many credits would you like to deposit [0,50,100,500]?: ")
    if deps == "0":
        credits = credits + 0
        print(f"You have {credits} credits")
    elif deps == "50":
        credits = credits + 50
        print(f"you now have {credits} credits")
    elif deps == "100":
        credits = credits + 100
        print(f"you now have {credits} credits")
    elif deps == "500":
        credits = credits + 500
        print(f"you now have {credits} credits")
    else:
        print("enter a valid deposit value")
def funds(): # Makes sure the player has sufficient amount of funds to spin the slot machine.
    if credits >= 10:
        print ("Test your luck at this slot machine")
        slotmachine()
    else:
        print("insufficient funds")






#main
simulation()

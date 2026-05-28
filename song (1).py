#Songrecommend

#init
import webbrowser
#album cover of Never Enough by Daniel Caesar
#Website name: Amazon
#author name:
#URL: https://www.amazon.com/NEVER-ENOUGH-Daniel-Caesar/dp/B0BVJ493D6
#Article title: NEVER ENOUGH Explicit Lyrics
#date: February 15th 2023

#album cover of Octane by Don Toliver
#Website name: Genius
#author name:
#URL: https://genius.com/albums/Don-toliver/Octane-physical-version
#Article title:OCTANE (Physical Version)
#date:January 30th 2026

#album cover of Immunity by Clairo
#Website name: Amazon
#author name:
#URL: https://www.amazon.com/Immunity-Clairo/dp/B07T6L6NVC
#Article title: Immunity
#date: July 4 2019

#album cover of channel ORANGE
#Website name: Amazon
#author name:
#URL: https://www.amazon.com/channel-ORANGE-Explicit-Frank-Ocean/dp/B008CJ0KI8
#Article title: channel ORANGE Explicit Lyrics
#date:

#functions
def song_rec():
    print("welcome to your album recommender")
    mood = input ("are you in a happy or calm mood today: ")
    if mood == "calm":
        time = input("daytime or nighttime vibes?: ")
        if time == "daytime":
            print(descriptions[1])
            webbrowser.open(url[1])
        elif time == "nighttime":
            print(descriptions[0])
            webbrowser.open(url[0])
        else:
            print("please type the correct input")
    if mood == "happy":
        season = input("are you in a summer or winter mood?: ")
        if season == "summer":
            print(descriptions[2])
            webbrowser.open(url[2])
        elif season == "winter":
             print(descriptions[3])
             webbrowser.open(url[3])



#main
url = ["https://m.media-amazon.com/images/I/A1CM0Qla82L._SX425_.jpg",#Neverenough
       "https://m.media-amazon.com/images/I/51n8-SmkIXL._UF1000,1000_QL80_.jpg",#Immunity
       "https://m.media-amazon.com/images/I/51Mp2uc8UFL._UF1000,1000_QL80_.jpg",#channelorange
       "https://images.genius.com/e17ac2a733016283ce8c62569a052bcb.1000x1000x1.png"]#octane
descriptions = ["Never Enough by Daniel Caesar is an angelic album perfect for a calm night or when you are in your feels. I recommend it for all music lovers looking for a great album",
                "Immunity by Clairo is a perfect album for the day where you feel a mix of happy, nostalgic, and at peae. Clairo does a great job of making your nerves settle",
                "Channel Orange by Frank Ocean is an intricate album with some songs that are perfect for a summer bike ride or a happy walk. I recommend this album for those looking for great beats."
                "Octane by Don TOliver is a very hype, newer album that is great for a hype winter day. It will get you motivated to push through those cold days."]

song_rec()



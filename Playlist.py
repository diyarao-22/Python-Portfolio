#Diya
#Todo List

#init

#functions
def playlist():
    songs = [""]
    Downloaded = [""]
    while True:
        print("""1. Add a song to your playlist
2. Download a song from your playlist
3. remove a song from your playlist
4. Exit playlist""")
        option = input("please choose an option from the menu [1,2,3,4]: ").strip()
        if option == "1":
            while True:
                add=input("What song would you like to add?: ").strip()
                if add == "":
                    print("please enter a song")
                    continue
                else:
                    songs.append(add)
                    print(f" You have successfully added {add} to your playlist")
                    print(f"Your Playlist: {songs}")
                    break
            continue
        elif option == "2":
            while True:
                download = input("What song would you like to download from your playlist?: ").strip()
                if download == "":
                    print("please enter a song")
                    continue
                else:
                    while True:
                        try:
                            songs.remove(download)
                        except:
                            print("This song is not in your playlist")
                            break
                    Downloaded.append(download)
                    print(f" You have successfully downloaded {download} to your playlist")
                    print(f"Your Playlist: {songs}")
                    print(f"Your downloaded songs: {Downloaded}")
                    break
            continue
        elif option == "3":
            while True:
                delete = input("What song would you like to delete from your playlist?: ").strip()
                if delete == "":
                    print("please enter a song")
                    continue
                else:
                    while True:
                        try:
                            songs.remove(delete)
                        except:
                            print("This song is not in your playlist")
                            break
                        print(f" You have successfully deleted {delete} from your playlist")
                        print(f"Your Playlist: {songs}")
                    break
            continue
        elif option == "4":
            print("you are now leaving your playlist")
            break
        else:
            print("please enter the correct input")

#main
playlist()




songs = []
while True:
    print("\n", "-"*10)
    print("0|Quit Manager\n1|View Songs\n2|Add Songs\n3|Delete Songs")
    choice = input("Enter your choice: ")
    if choice == "0":
        print("exiting...")
        break
    elif choice == "1":
        for i in range(len(songs)):
            print(i+1, ".", songs[i])
        input("Enter to continue...")
    elif choice == "2":
        song = input("Enter the song you want to add: ")
        songs.append(song)
    elif choice == "3":
        song = input("Enter the song you want to remove: ")
        songs.remove(song)
    else:
        print("Try again.")

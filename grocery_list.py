grocery_list = []
while True:
    choice = input("(1) See your list\n(2) Add to your list\n(3) Remove from list\n(4) Stop the program\nEnter your choice:")
    if choice == "1":
        #see the list
        print("Your list:",grocery_list)
    elif choice == "2":
        #add item
        item = input("What item to add?: ")
        grocery_list.append(item)
    elif choice == "3":
        #remove an item of their choice
        #HINT: use grocery_list.remove()
        item = input("What item to remove?: ")
        grocery_list.remove(item)
    elif choice == "4":
        break
    print(grocery_list)

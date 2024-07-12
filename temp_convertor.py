print("If you want to convert celsius to fahrenheit enter a. If you want to convert fahrenheit to celsius enter b: ", end="")
choice = input() #save the input from before into choice
temp = int(input("What temperature?: ")) #take the temperature entered and turn it into an integer, then save it as temp

if choice == "a":
    #celsus to fahrenheit
    new_temp = (temp*1.8)+32
    print("The temperature in fahrenheit is", new_temp)

elif choice == "b":
    #fahrenheit to celsius
    new_temp = (temp - 32)/1.8
    print("The temperature in celsius is", new_temp)
grocery_list = ["plain bread", "butter", "lettuce", "cheese", "tomatoes"]

grocery_list.remove("cheese")
if "cheese" in grocery_list:
	print("you need to buy cheese")
else: 
	print("no need to buy cheese")

friends = ["Robert", "Jackson", "Matthew"]
user = input("Name: ")
if user in friends:
	print("Hello friend!")
else:
	want_to_be_friend = input("want to be friends? y/n: ")
	if want_to_be_friend == "n":
		print("I hate you!")
	else:
		print("Hi friend!")
		friends.append(user)
	
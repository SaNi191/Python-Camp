all_ingredients = ['rice', 'soy sauce','eggs','oil','sausage','green onion','onion', 'tomato','salt','vinegar', 'garlic', 'green peas', 'corn', 'pepper','lettuce']
fried_rice = []
print("WELCOME TO THE RICEMAKER!")
for ingredient in all_ingredients:
    print("Do you want", ingredient, "in your fried rice? Enter 0 if you want to skip to the end!")
    yes_or_no = input("y/n:").lower()
    if yes_or_no == 'y':
        fried_rice.append(ingredient)
    elif yes_or_no == "0":
        break

if "rice" not in fried_rice:
    print("This fried rice is invalid!")
elif "sausage" in fried_rice and "corn" in fried_rice:
    print("This fried rice is invalid!")
else:
    print("This is your fried rice:", fried_rice)

'''
1. list  all your ingredients in a list
2. loop through ingredients, y/n do you add it to your fried_rice
3. print out all your ingredients
4. add invalid fried rice conditions (no rice in your fried rice)
'''
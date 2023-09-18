# Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade
lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_cups = float(input("Enter amount of agave nectar (in cups):\n"))
how_many_servings = int(input("How many servings does this make?\n"))

# Calculate the total ingredient amounts
total_lemon_juice_cups = lemon_juice_cups
total_water_cups = water_cups
total_agave_cups = agave_cups

# Print the ingredients and serving size with two decimal places
print()
print(f"Lemonade ingredients - yields {how_many_servings:.2f} servings")
print(f"{total_lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{total_water_cups:.2f} cup(s) water")
print(f"{total_agave_cups:.2f} cup(s) agave nectar\n")

# Prompt the user to specify the desired number of servings
how_many_servings = int(input("How many servings would you like to make?\n"))
print()
# Adjust the ingredient amounts based on the new serving size
total_lemon_juice_cups *= how_many_servings / 6
total_water_cups *= how_many_servings / 6
total_agave_cups *= how_many_servings / 6

# Print the adjusted ingredients and serving size with two decimal places
print(f"Lemonade ingredients - yields {how_many_servings:.2f} servings")
print(f"{total_lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{total_water_cups:.2f} cup(s) water")
print(f"{total_agave_cups:.2f} cup(s) agave nectar\n")

# Convert the ingredient measurements to gallons (1 gallon = 16 cups)
total_lemon_juice_gallons = total_lemon_juice_cups / 16
total_water_gallons = total_water_cups / 16
total_agave_gallons = total_agave_cups / 16

# Print the ingredients in gallons with two decimal places
print(f"Lemonade ingredients - yields {how_many_servings:.2f} servings")
print(f"{total_lemon_juice_gallons:.2f} gallon(s) lemon juice")
print(f"{total_water_gallons:.2f} gallon(s) water")
print(f"{total_agave_gallons:.2f} gallon(s) agave nectar")

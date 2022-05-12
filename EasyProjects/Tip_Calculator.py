print("Welcome to the tip calculator.")
bill = int(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
number_people = int(input("How many people is paying for the bill?\n"))
tot = round((bill * (1+tip/100))/number_people,2)

print(f"Each person should pay ${tot}")



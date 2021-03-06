from CoffeeMachine_Data import MENU
from CoffeeMachine_Data import resources

# TODO: 0. Initialization of variables
# resources in CoffeMachine_Data.py



# TODO: 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​” 
# a. Check the user’s input to decide what to do next.  
wish = input("What would you like? (espresso/latte/cappuccino): ​").lower()


# b. The prompt should show every time action has completed, e.g. once the drink is 
# dispensed. The prompt should show again to serve the next customer.
end_of_drink = True
if not end_of_drink:
  wish = input("What would you like? (espresso/latte/cappuccino): ​").lower()
  end_of_drink = False

# TODO: 2. Turn off the Coffee Machine by entering “​off​” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off 
# the machine. Your code should end execution when this happens.
if wish == "off":
  exit
 
# TODO: 3. Print report. 
# a. When the user enters “report” to the prompt, a report should be generated that shows 
# the current resource values. e.g.  
# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# Money: $2.5
water = resources['water']
milk = resources['milk']
coffee = resources['coffee'] 
money = 0
if wish == 'report':
  print(f"\nCurrent resources of the coffee machine:\nWater: {water}\nMilk: {milk}\nCoffee: {coffee}\nmoney: {money}")

 
# TODO: 4. Check resources sufficient? 
# a. When the user chooses a drink, the program should check if there are enough 
# resources to make that drink.  
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should 
# not continue to make the drink but print: “​Sorry there is not enough water.​” 
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def returningredientofdrink(drink_name):
  """ Return drink's ingredients """
  return MENU[drink_name]["ingredients"]

if not (returningredientofdrink(wish)["water"] < water or returningredientofdrink(wish)["milk"] < milk or returningredientofdrink(wish)["coffee"] < coffee):
  print("Sorry, there is not enough ingredient")
  exit

# TODO: 5. Process coins. 
# a. If there are sufficient resources to make the drink selected, then the program should 
# prompt the user to insert coins.  
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52 
else:
  inserted_pennies = int(input("Insert pennies: "))
  inserted_nickles = int(input("Insert nickles: "))
  inserted_dimes = int(input("Insert dimes: "))
  inserted_quarters = int(input("Insert quarters: "))
  total_money = round(inserted_pennies * 0.01 + inserted_dimes * 0.10 + inserted_nickles * 0.05 + inserted_quarters * 0.25,2)
  print(f"Total inserted money = {total_money}")

# TODO: 6. Check transaction successful? 
# a. Check that the user has inserted enough money to purchase the drink they selected. 
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the 
# program should say “​Sorry that's not enough money. Money refunded.​”. 
if total_money < MENU[wish]["cost"]:
  print("​Sorry that's not enough money. Money refunded.")
  exit
# b. But if the user has inserted enough money, then the cost of the drink gets added to the 
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.  
# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# Money: $2.5
else:
  resources["money"] = resources["money"] + MENU[wish]["cost"]

# c. If the user has inserted too much money, the machine should offer change.  
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal 
# places. 
  refund = total_money - MENU[wish]["cost"]
  print(f"Here is your change of ${refund}")
 
 
# TODO: 7. Make Coffee. 
# a. If the transaction is successful and there are enough resources to make the drink the 
# user selected, then the ingredients to make the drink should be deducted from the 
# coffee machine resources.  

# E.g. report before purchasing latte: 
# Water: 300ml 
# Milk: 200ml 
# Coffee: 100g 
# Report after purchasing latte: 
# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# Money: $2.5 
# Money: $0 
  water -= returningredientofdrink(wish)["water"]
  coffee -= returningredientofdrink(wish)["coffee"]
  milk -= returningredientofdrink(wish)["milk"]
 
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If 
# latte was their choice of drink. 
  print(f"Enjoy your {wish}!")
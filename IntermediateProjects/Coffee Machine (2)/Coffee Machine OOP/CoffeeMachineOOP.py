from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
machine_is_on = True


while machine_is_on:  
  drink = input(f"​What would you like? {menu.get_items()}\n--> ")

  if drink == "off":
    print("The machine will shut down.")
    machine_is_on = False    
  elif drink == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    o_drink = menu.find_drink(drink)
    if coffee_maker.is_resource_sufficient(o_drink) and money_machine.make_payment(o_drink.cost):
      coffee_maker.make_coffee(o_drink)
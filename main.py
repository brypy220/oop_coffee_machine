from menu import Menu
from coffee_machine import CoffeeMaker
from money_dispenser import MoneyDispenser

money_dispenser = MoneyDispenser()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    selection = input(f"What would you like?({options}):")
    if selection == "off":
        is_on = False
    elif selection == "report":
        coffee_maker.report()
        money_dispenser.report()
    else:
        drink = menu.find_drink(selection)

        if coffee_maker.is_resource_available(drink) and money_dispenser.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

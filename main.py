import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    on = True
    while on:
        size = input("Select sandwich size: (small, medium, large)")

        if size in recipes:
            sandwich = recipes[size]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(size, sandwich["ingredients"])
            else:
                print("Cannot make sandwich")
        else:
            print("Invalid size")


if __name__=="__main__":
    main()

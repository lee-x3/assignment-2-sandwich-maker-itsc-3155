
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] < amount:
                print("Not enough ingredients to make the sandwich.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print("Making your sandwich...")


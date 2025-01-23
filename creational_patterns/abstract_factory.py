# Abstract Factory Pattern

# Classification happens on three levels:
# Factory Level: Defines an interface for creating an object.
# Product family Level: Defines a family of related products.
# Concrete family Level: Defines a family of related concrete products.


from abc import abstractmethod


class Burger:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __repr__(self):
        pass


class Drink:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __repr__(self):
        pass


class CheeseBurger(Burger):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"CheeseBurger({self.name})"


class VeggieBurger(Burger):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"VeggieBurger({self.name})"


class ChickenBurger(Burger):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"ChickenBurger({self.name})"


class CheeseDrink(Drink):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"CheeseDrink({self.name})"


class BeerDrink(Drink):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"BeerDrink({self.name})"


class Restaurant:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_burger(self, name: str):
        pass

    @abstractmethod
    def create_drink(self, name: str):
        pass

    def order(self, food: str):
        print(f"Ordering {food} from {self.name}")

    def __repr__(self):
        return f"Restaurant({self.name})"


class FastFoodRestaurant(Restaurant):
    def __init__(self, name: str = "Burger King"):
        super().__init__(name)

    def create_burger(self, name: str):
        if name == "VeggieBurger":
            return VeggieBurger(name)
        elif name == "CheeseBurger":
            return CheeseBurger(name)
        elif name == "ChickenBurger":
            return ChickenBurger(name)
        else:
            raise ValueError(f"Invalid burger type: {name}")

    def create_drink(self, name: str):
        if name == "CheeseDrink":
            return CheeseDrink(name)
        elif name == "BeerDrink":
            return BeerDrink(name)
        else:
            raise ValueError(f"Invalid drink type: {name}")


class NonWegnerRestaurant(Restaurant):
    def __init__(self, name: str = "McDonald's"):
        super().__init__(name)

    def create_burger(self, name: str):
        if name == "CheeseBurger":
            return CheeseBurger(name)
        elif name == "ChickenBurger":
            return ChickenBurger(name)
        else:
            raise ValueError(f"Invalid burger type: {name}")

    def create_drink(self, name: str):
        if name == "CheeseDrink":
            return CheeseDrink(name)
        elif name == "BeerDrink":
            return BeerDrink(name)
        else:
            raise ValueError(f"Invalid drink type: {name}")


class WegnerRestaurant(Restaurant):
    def __init__(self, name: str = "Wegner's"):
        super().__init__(name)

    def create_burger(self, name: str):
        if name == "VeggieBurger":
            return VeggieBurger(name)
        elif name == "ChickenBurger":
            return ChickenBurger(name)
        else:
            raise ValueError(f"Invalid burger type: {name}")

    def create_drink(self, name: str):
        if name == "BeerDrink":
            return BeerDrink(name)
        elif name == "CheeseDrink":
            return CheeseDrink(name)
        else:
            raise ValueError(f"Invalid drink type: {name}")


class MealPlan:
    def __init__(self, restaurant: Restaurant):
        self.restaurant = restaurant
        self.burger_type = "VeggieBurger"
        self.drink_type = "BeerDrink"

    def create_meal(self):
        burger = self.restaurant.create_burger(self.burger_type)
        drink = self.restaurant.create_drink(self.drink_type)
        self.restaurant.order(burger)
        self.restaurant.order(drink)


if __name__ == "__main__":
    restaurant = FastFoodRestaurant()
    meal_plan = MealPlan(restaurant)
    meal_plan.burger_type = "VeggieBurger"
    meal_plan.drink_type = "BeerDrink"
    meal_plan.create_meal()
    print("")

    restaurant = NonWegnerRestaurant()
    meal_plan = MealPlan(restaurant)
    meal_plan.burger_type = "CheeseBurger"
    meal_plan.drink_type = "CheeseDrink"
    meal_plan.create_meal()
    print("")

    restaurant = WegnerRestaurant()
    meal_plan = MealPlan(restaurant)
    meal_plan.burger_type = "VeggieBurger"
    meal_plan.drink_type = "BeerDrink"
    meal_plan.create_meal()

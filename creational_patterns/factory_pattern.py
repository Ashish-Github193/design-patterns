# Factory Method Pattern

# Classification Level: Two levels
# Product Level: Defines a single method for creating an object.
# Subclass Level: Subclasses implement the factory method to
# create objects of the appropriate type.


class VeggieBurger:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"VeggieBurger({self.name})"


class CheeseBurger:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"CheeseBurger({self.name})"


class ChickenBurger:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"ChickenBurger({self.name})"


class Restaurant:
    def __init__(self, name: str):
        self.name = name

    def create_burger(self, name: str):
        if name == "VeggieBurger":
            return VeggieBurger(name)
        elif name == "CheeseBurger":
            return CheeseBurger(name)
        elif name == "ChickenBurger":
            return ChickenBurger(name)
        else:
            raise ValueError(f"Invalid burger type: {name}")

    def order(self, food: str):
        print(f"Ordering {food} from {self.name}")

    def __repr__(self):
        return f"Restaurant({self.name})"


if __name__ == "__main__":
    restaurant = Restaurant("Burger King")
    burger1 = restaurant.create_burger("VeggieBurger")
    burger2 = restaurant.create_burger("CheeseBurger")
    burger3 = restaurant.create_burger("ChickenBurger")

    print(burger1)
    print(burger2)
    print(burger3)

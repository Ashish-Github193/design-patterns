class Circle(object):
    def __init__(self, color: str) -> None:
        self.color = color

    def draw(self, pos_x: int, pos_y: int, radius: float) -> None:
        print(f"""Drawing Circle({dict(x=pos_x, y=pos_y, r=radius)})""")


class DrawerFlyweight(object):
    def __init__(self) -> None:
        self._flyweights = {}

    def add_circle(self, color: str) -> Circle:
        if not color in self._flyweights:
            print("Color not present in _flyweights")
            self._flyweights[color] = Circle(color)
        else:
            print("Color already present in _flyweights, Reusing it")

        return self._flyweights[color]


if __name__ == "__main__":
    drawer = DrawerFlyweight()

    circle1 = drawer.add_circle(color="Red")
    circle1.draw(pos_x=10, pos_y=50, radius=10)

    circle2 = drawer.add_circle(color="Blue")
    circle2.draw(pos_x=30, pos_y=89, radius=30)

    circle3 = drawer.add_circle("Red")
    circle3.draw(pos_x=80, pos_y=56, radius=8)

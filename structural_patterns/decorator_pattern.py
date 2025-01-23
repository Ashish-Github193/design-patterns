from abc import ABC, abstractmethod


class BasicShape(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        return "BasicShape()"


class Circle(BasicShape):
    def __repr__(self) -> str:
        parent_repr = super().__repr__()[:-1]
        return f"{parent_repr}name=circle)"


class BasicShapeDecorator(BasicShape):
    def __init__(self, shape: BasicShape) -> None:
        self.shape = shape

    def __repr__(self) -> str:
        return self.shape.__repr__()


class AddBorder(BasicShapeDecorator):
    def __init__(self, shape: BasicShape, border_width: int) -> None:
        super().__init__(shape)
        self.border: int = border_width

    def __repr__(self) -> str:
        parent_repr = super().__repr__()[:-1]
        return f"{parent_repr}, border={self.border}px)"


class AddShadow(BasicShapeDecorator):
    def __init__(self, shape: BasicShape, shadow_width: int) -> None:
        super().__init__(shape)
        self.shadow: int = shadow_width

    def __repr__(self) -> str:
        parent_repr = super().__repr__()[:-1]
        return f"{parent_repr}, shadow={self.shadow}px)"


class FillColor(BasicShapeDecorator):
    def __init__(self, shape: BasicShape, color: str) -> None:
        super().__init__(shape)
        self.color = color

    def __repr__(self) -> str:
        parent_repr = super().__repr__()[:-1]
        return f"{parent_repr}, color={self.color})"


if __name__ == "__main__":
    circle = Circle()
    print(circle)

    circle = AddBorder(circle, border_width=5)
    print(circle)

    circle = AddShadow(circle, shadow_width=3)
    print(circle)

    circle = FillColor(circle, color="Red")
    print(circle)

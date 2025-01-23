from abc import ABC, abstractmethod
from random import randint, choice
from uuid import uuid4


class Entity(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._size: int = None

    @property
    def size(self) -> int:
        return self._size

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def show_details(self, prefix="") -> None:
        pass


class File(Entity):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._size = randint(1, 100)

    def __repr__(self) -> str:
        return f"File({self.name=}, {self.size=})"

    def show_details(self, prefix="") -> None:
        print(f"{prefix}{self.__repr__()}")


class Directory(Entity):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.childs: list[Entity] = []

    @property
    def size(self) -> int:
        total_size = sum([child.size for child in self.childs])
        return total_size

    @property
    def total_childs(self) -> int:
        return len(self.childs)

    def add_child(self, file: Entity) -> None:
        if not isinstance(file, Entity):
            raise TypeError("Only object of class Entity is allowed")  # noqa
        self.childs.append(file)

    def __repr__(self) -> str:
        return f"Directory({self.name=}, {self.total_childs=}, {self.size=})"

    def show_details(self, prefix="") -> None:
        print(f"{prefix}{self.__repr__()}")
        prefix = prefix + (" " * 2)
        for child in self.childs:
            child.show_details(prefix)


def random_filename_generator():
    extensions = ("pdf", "xlsx", "txt", "pptx")
    return f"{uuid4()}.{choice(extensions)}"


if __name__ == "__main__":
    root = Directory("root")
    file1 = File(random_filename_generator())
    root.add_child(file1)
    file2 = File(random_filename_generator())
    root.add_child(file2)

    home = Directory("home")
    file3 = File(random_filename_generator())
    home.add_child(file3)
    file4 = File(random_filename_generator())
    home.add_child(file4)

    root.add_child(home)
    root.show_details()

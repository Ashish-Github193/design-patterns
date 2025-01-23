from abc import ABC


class Computer(object):
    motherboard: str
    cpu: str
    ram: str
    gpu: str
    storage: str
    power: str
    cooling: str
    case: str

    def __repr__(self) -> str:
        return (
            f"Computer:\n"
            f"  Motherboard: {self.motherboard}\n"
            f"  CPU: {self.cpu}\n"
            f"  RAM: {self.ram}\n"
            f"  GPU: {self.gpu}\n"
            f"  Storage: {self.storage}\n"
            f"  Power Supply: {self.power}\n"
            f"  Cooling: {self.cooling}\n"
            f"  Case: {self.case}\n"
        )


class ComputerBuilder(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.computer = Computer()

    def add_motherboard(self):
        pass

    def add_cpu(self):
        pass

    def add_ram(self):
        pass

    def add_gpu(self):
        pass

    def add_storage(self):
        pass

    def add_power(self):
        pass

    def add_cooling(self):
        pass

    def add_case(self):
        pass

    def fetch_output(self):
        return self.computer


class GamingPcBuilder(ComputerBuilder):
    def __init__(self) -> None:
        super().__init__()

    def add_motherboard(self):
        self.computer.motherboard = "eye opening motherboard"

    def add_cpu(self):
        self.computer.cpu = "eye opening cpu"

    def add_ram(self):
        self.computer.ram = "10000MHz ram"

    def add_gpu(self):
        self.computer.gpu = "eye opening gpu"

    def add_storage(self):
        self.computer.storage = "eye opening storage"

    def add_power(self):
        self.computer.power = "eye opening power supply"

    def add_cooling(self):
        self.computer.cooling = "eye opening cooling system"

    def add_case(self):
        self.computer.case = "eye opening case"


class BudgetPcBuilder(ComputerBuilder):
    def __init__(self) -> None:
        super().__init__()

    def add_motherboard(self):
        self.computer.motherboard = "budget motherboard"

    def add_cpu(self):
        self.computer.cpu = "budget cpu"

    def add_ram(self):
        self.computer.ram = "budget ram"

    def add_gpu(self):
        self.computer.gpu = "budget gpu"

    def add_storage(self):
        self.computer.storage = "budget storage"

    def add_power(self):
        self.computer.power = "budget power supply"

    def add_cooling(self):
        self.computer.cooling = "budget cooling system"

    def add_case(self):
        self.computer.case = "budget case"


class PotatoPcBuilder(ComputerBuilder):
    def __init__(self) -> None:
        super().__init__()

    def add_motherboard(self):
        self.computer.motherboard = "potato motherboard"

    def add_cpu(self):
        self.computer.cpu = "potato cpu"

    def add_ram(self):
        self.computer.ram = "potato ram"

    def add_gpu(self):
        self.computer.gpu = "potato gpu"

    def add_storage(self):
        self.computer.storage = "potato storage"

    def add_power(self):
        self.computer.power = "potato power supply"

    def add_cooling(self):
        self.computer.cooling = "potato cooling system"

    def add_case(self):
        self.computer.case = "potato case"


class ShopManager(object):
    def __init__(self) -> None:
        super().__init__()
        self.computer_builders = {
            "gaming_pc": GamingPcBuilder(),
            "budget_pc": BudgetPcBuilder(),
            "potato_pc": PotatoPcBuilder(),
        }

    def build_computer(self, computer_type: str) -> Computer:
        builder = self.computer_builders[computer_type]
        builder.add_motherboard()
        builder.add_cpu()
        builder.add_ram()
        builder.add_gpu()
        builder.add_storage()
        builder.add_power()
        builder.add_cooling()
        builder.add_case()
        return builder.fetch_output()


if __name__ == "__main__":
    shop_manager = ShopManager()
    computer = shop_manager.build_computer("gaming_pc")
    print(computer, end="\n\n")

    computer = shop_manager.build_computer("budget_pc")
    print(computer, end="\n\n")

    computer = shop_manager.build_computer("potato_pc")
    print(computer, end="\n\n")

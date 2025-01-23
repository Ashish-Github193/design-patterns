class Lights(object):

    def __init__(self) -> None:
        self.on = False

    def __repr__(self) -> str:
        status = "OFF" if not self.on else "ON"
        return f"Lights are {status}"


class Thermostat(object):

    def __init__(self) -> None:
        self.temprature = 18

    def __repr__(self) -> str:
        return f"Thermostat at {self.temprature}deg"


class SecuritySystem(object):

    def __init__(self) -> None:
        self.arm = True

    def __repr__(self) -> str:
        status = "DISARMED" if not self.arm else "ARMED"
        return f"Security System {status}"


class Speakers(object):

    def __init__(self) -> None:
        self.play: bool = False
        self.volume: int = 30

    def __repr__(self) -> str:
        if self.play:
            return f"Speaker is playing at volume {self.volume}"

        return "Speaker is not playing"


class SmartHomeFacade(object):

    def __init__(
        self,
        lights: Lights,
        thermostat: Thermostat,
        security_system: SecuritySystem,
        speakers: Speakers,
    ) -> None:
        self.lights = lights
        self.thermostat = thermostat
        self.security_system = security_system
        self.speakers = speakers

    def start_morning_routine(self) -> None:
        self.lights.on = True
        self.thermostat.temprature = 22
        self.speakers.play = True

    def leave_home(self) -> None:
        self.lights.on = False
        self.thermostat.temprature = 18
        self.security_system.arm = True
        self.speakers.play = False

    def arrive_home(self) -> None:
        self.lights.on = True
        self.thermostat.temprature = 22
        self.speakers.play = True


if __name__ == "__main__":
    smart_home = SmartHomeFacade(
        lights=Lights(),
        thermostat=Thermostat(),
        security_system=SecuritySystem(),
        speakers=Speakers(),
    )

    smart_home.start_morning_routine()
    print(smart_home.lights)
    print(smart_home.thermostat)
    print(smart_home.speakers)
    print("")

    smart_home.leave_home()
    print(smart_home.lights)
    print(smart_home.thermostat)
    print(smart_home.security_system)
    print(smart_home.speakers)
    print("")

    smart_home.arrive_home()
    print(smart_home.lights)
    print(smart_home.thermostat)
    print(smart_home.speakers)

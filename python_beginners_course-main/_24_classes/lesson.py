class Ork:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 10 * level

    def attack(self):
        print(f"Ork attack with power {self.attack_power}")

    def __str__(self):
        return f"Ork level: {self.level}  HP: {self.attack_power}"


class Elf:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = 50 * level
        self.attack_power = 15 * level

    def attack(self):
        print(f"Elf attack with power {self.attack_power}")

    def __str__(self):
        return f"Elf level: {self.level}  HP: {self.attack_power}"


ork = Ork(level=1)
print(ork.health_points)
print(ork)

class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        print(
            f"{self.character_name} attack {target.character_name} with power {self.attack_power}"
        )

    def __str__(self):
        return f"{self.character_name} level: {self.level}  HP: {self.attack_power}"


class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"


class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"


ork = Ork(level=1)
elf = Elf(level=1)

ork.attack(target=elf)

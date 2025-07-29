from abc import ABC, abstractmethod

class Enemy(ABC):
    @abstractmethod
    def attack(self) -> str:
        """Return a string describing the enemy's attack."""
        pass

class Orc(Enemy):
    def attack(self) -> str:
        return "Orc swings a crude axe!"

class Elf(Enemy):
    def attack(self) -> str:
        return "Elf fires an arrow with precision!"

class Dragon(Enemy):
    def attack(self) -> str:
        return "Dragon breathes fire!"

class EnemySpawner(ABC):
    @abstractmethod
    def create_enemy(self) -> Enemy:
        """Factory method to create an Enemy."""
        pass

    def simulate_encounter(self) -> str:
        """Simulate a game encounter with an enemy."""
        enemy = self.create_enemy()
        return f"An encounter begins! [{enemy.attack()}]"

class OrcSpawner(EnemySpawner):
    def create_enemy(self) -> Enemy:
        return Orc()

class ElfSpawner(EnemySpawner):
    def create_enemy(self) -> Enemy:
        return Elf()

class DragonSpawner(EnemySpawner):
    def create_enemy(self) -> Enemy:
        return Dragon()

# Extensibility: Add new enemy types easily
class Goblin(Enemy):
    def attack(self) -> str:
        return "Goblin stabs with a rusty dagger!"

class GoblinSpawner(EnemySpawner):
    def create_enemy(self) -> Enemy:
        return Goblin()

# --- Usage Example ---
def demo_encounters():
    spawners = [
        OrcSpawner(),
        ElfSpawner(),
        DragonSpawner(),
        GoblinSpawner()  # New enemy type
    ]
    print("--- Simulating Encounters ---")
    for spawner in spawners:
        print(spawner.simulate_encounter())

if __name__ == "__main__":
    demo_encounters()

# Output:
# --- Simulating Encounters ---
# An encounter begins! [Orc swings a crude axe!]
# An encounter begins! [Elf fires an arrow with precision!]
# An encounter begins! [Dragon breathes fire!]
# An encounter begins! [Goblin stabs with a rusty dagger!]
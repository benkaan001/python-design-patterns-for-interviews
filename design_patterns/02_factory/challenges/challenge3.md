# Challenge: Game Enemy Spawner

## 📝 Scenario

You are developing a fantasy role-playing game where players encounter various types of enemies. As the game progresses, or based on the player's location, different kinds of enemies (e.g., Orcs, Elves, Dragons) need to be spawned. The game's core combat or encounter logic should be flexible enough to work with any type of enemy without needing to know the specific class of the enemy it's fighting.

Your task is to design a system that allows different types of enemies to be created and introduced into the game, while keeping the game's main logic decoupled from the concrete enemy classes. This system should be easily extensible to add new enemy types (e.g., Goblins, Trolls, Golems) in the future without modifying the existing game logic.

## 🚀 Your Task

Implement this game enemy spawning system using the  **Factory Method Pattern** .

### Requirements:

1. **Product (Abstract):**
   * Define an abstract class `Enemy` with an abstract method `attack() -> str`. This method should return a string describing the enemy's attack.
2. **Concrete Products:**
   * `Orc`: Implements `attack()`, returning `"Orc swings a crude axe!"`.
   * `Elf`: Implements `attack()`, returning `"Elf fires an arrow with precision!"`.
   * `Dragon`: Implements `attack()`, returning `"Dragon breathes fire!"`.
3. **Creator (Abstract):**
   * Define an abstract class `EnemySpawner` with:
     * An abstract **factory method** `create_enemy() -> Enemy`. This method will be overridden by subclasses to create specific enemy types.
     * A concrete (non-abstract) method `simulate_encounter() -> str`. This method should represent the game's core encounter logic: it calls `create_enemy()` to get an `Enemy` object and then calls `attack()` on that enemy. This method should return a string like `"An encounter begins! [Enemy Attack Output]"`.
4. **Concrete Creators:**
   * `OrcSpawner`: Overrides `create_enemy()` to return an `Orc`.
   * `ElfSpawner`: Overrides `create_enemy()` to return an `Elf`.
   * `DragonSpawner`: Overrides `create_enemy()` to return a `Dragon`.

## 💡 Hints:

* Focus on how the `simulate_encounter()` method in the abstract `EnemySpawner` uses the `create_enemy()` factory method without knowing the concrete enemy type. This is the essence of the pattern's decoupling.
* Use `abc.ABC` and `@abstractmethod` for your abstract classes and methods.

Good luck, and may your code be bug-free!

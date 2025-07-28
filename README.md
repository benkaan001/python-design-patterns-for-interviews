# Python Design Patterns for Interviews

Welcome to the `python-design-patterns-for-interviews` repository! This **comprehensive educational resource** is designed to help developers master software design patterns in Python, with a focus on **technical interview preparation and practical application**.

## 🎯 Purpose

Understanding design patterns is crucial for building maintainable software and excelling in technical interviews. This repository provides:

- **Clear Explanations:** Understand the "Why" (problem solved) and "What" (structure and benefits) for each pattern.
- **Multiple Practical Challenges:** Specific scenarios designed to test your implementation skills.
- **Reference Solutions:** Well-commented Python code (both `.py` and `.ipynb` notebooks) demonstrating effective pattern implementation.
- **Interactive Learning:** (Backend-focused for now) Tools for quizzes and progressive difficulty levels.
- **Self-Study Aid:** Structured practice allowing you to attempt challenges without seeing solutions.
- **Interview-Focused:** Patterns ordered by interview frequency with real-world scenarios.

## 🚀 Quick Start

To get started quickly, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/benkaan001/python-design-patterns-for-interviews.git
   cd python-design-patterns-for-interviews
   ```
2. **Set up your virtual environment and install dependencies:**
   (See detailed instructions in the "Installation & Setup" section below.)
   ```bash
   python3 -m venv venv
   source venv/bin/activate # macOS/Linux
   # venv\Scripts\activate.bat # Windows Command Prompt
   # .\venv\Scripts\Activate.ps1 # Windows PowerShell
   pip install -r requirements.txt
   python -m ipykernel install --user --name=design_patterns_env --display-name "Python 3 (Design Patterns Env)"
   ```
3. **Start learning!** Navigate to a pattern's directory or explore the interactive tools (once implemented).

## 📚 How to Use This Repository

This repository is structured to support various learning styles and goals:

### 🎯 For Beginners

- **Read Pattern Explanations:** Navigate to pattern directories (e.g., `design_patterns/01_singleton/`) and read the `README.md` files to grasp core concepts.
- **Attempt Simple Challenges:** Start with `challenge_01.md` in each pattern's `challenges/` subdirectory.
- **Review Solutions:** Compare your code with `solution_01.py` (or `.ipynb`) in the `solutions/` subdirectory.

### 🔥 For Interview Preparation

- **Focus on Top Patterns:** Prioritize patterns listed under "Most Frequently Asked" below.
- **Practice Challenges:** Work through all challenges for each pattern, focusing on efficient and robust solutions.
- **Review Interview Scenarios:** (Planned) Each pattern's `challenges/` directory may include `interview_questions.md` with common interview scenarios.

### 🏆 For Advanced Users

- **Complex Scenarios:** Tackle advanced challenges that might combine multiple patterns.
- **Code Review Mode:** Analyze and improve existing implementations in the `solutions/` directory.
- **Contribute:** Help expand the repository by adding new challenges, solutions, or documentation.

## 📂 Repository Structure

```
python-design-patterns-for-interviews/
├── .gitignore                    # Standard Python ignore rules
├── LICENSE                       # MIT License
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── setup.py                      # (Planned) Package setup for interactive tools
├── design_patterns/              # Core pattern implementations
│   ├── 01_singleton/
│   │   ├── README.md            # Pattern explanation with examples
│   │   ├── challenges/          # Multiple challenge problems
│   │   │   ├── challenge_01.md  # Basic implementation
│   │   │   ├── challenge_02.md  # Thread-safe version (example)
│   │   │   ├── challenge_03.md  # Advanced scenarios (example)
│   │   │   └── interview_questions.md # (Planned) Real interview questions
│   │   ├── solutions/           # Reference solutions
│   │   │   ├── solution_01.py   # Python solution for challenge 01
│   │   │   ├── solution_01.ipynb # Jupyter Notebook solution for challenge 01
│   │   │   ├── solution_02.py
│   │   │   ├── solution_02.ipynb
│   │   │   └── solution_03.py
│   │   │   └── solution_03.ipynb
│   │   ├── tests/               # (Planned) Unit tests for solutions
│   │   │   └── test_singleton.py
│   │   └── visual/              # (Planned) UML diagrams and flowcharts
│   │       └── singleton_diagram.png
│   ├── 02_factory_method/       # Renamed for consistency
│   │   ├── README.md
│   │   ├── challenges/
│   │   │   ├── challenge_01.md
│   │   │   └── ...
│   │   └── solutions/
│   │       ├── solution_01.py
│   │       │   └── ...
│   │   ├── tests/
│   │   └── visual/
│   └── ... (more patterns, following similar structure)
├── anki_flashcards/              # (Planned) Spaced repetition learning resources
│   ├── README.md                # Import and usage instructions
│   ├── complete_deck.apkg       # All patterns combined (example)
│   └── individual_patterns/     # Separate decks per pattern (example)
│       ├── singleton.apkg
│       └── ...
├── interactive_practice/         # (Planned) Interactive learning tools (Python scripts)
│   ├── quiz.py                  # Pattern concept quizzes
│   ├── timed_challenge.py       # Interview simulation
│   ├── progress_tracker.py      # Learning progress tracking
│   └── ...
├── docs/                        # (Planned) Additional documentation
│   ├── interview_guide.md       # General interview preparation guide
│   ├── pattern_comparison.md    # When to use which pattern
│   └── contributing.md          # Detailed contribution guidelines
└── examples/                    # (Planned) Real-world application examples
    ├── web_framework_patterns/
    ├── game_development/
    └── data_processing/
```

## ✨ Design Patterns Covered (Ordered by Interview Frequency)

*This section will be updated as more patterns are added and solutions are completed.*

### 🔥 Most Frequently Asked (Master These First!)

1. **Singleton Pattern** - Ensure a class has only one instance and provide a global access point.
2. **Factory Method Pattern** - Define an interface for creating an object, but let subclasses decide which class to instantiate.
3. **Observer Pattern** *(Coming Soon!)* - Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
4. **Strategy Pattern** *(Coming Soon!)* - Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
5. **Decorator Pattern** *(Coming Soon!)* - Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
6. **Builder Pattern** *(Coming Soon!)* - Separate the construction of a complex object from its representation so that the same construction process can create different representations.
7. **Adapter Pattern** *(Coming Soon!)* - Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
8. **Command Pattern** *(Coming Soon!)* - Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

### 📚 Moderately Asked

9. **Abstract Factory Pattern** *(Coming Soon!)* - Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
10. **Facade Pattern** *(Coming Soon!)* - Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
11. **Proxy Pattern** *(Coming Soon!)* - Provide a surrogate or placeholder for another object to control access to it.
12. **State Pattern** *(Coming Soon!)* - Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
13. **Iterator Pattern** *(Coming Soon!)* - Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
14. **Prototype Pattern** *(Coming Soon!)* - Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

**Legend:** ✅ Complete | 🚧 Coming Soon | 📋 Planned

## 🎮 Interactive Features (Backend Focused)

These features will be implemented as Python scripts to enhance your learning experience.

- **Quiz Mode:**
  ```bash
  # Test your knowledge with interactive quizzes
  python interactive_practice/quiz.py
  # Focus on specific patterns
  python interactive_practice/quiz.py --pattern singleton
  ```
- **Progress Tracking:**
  ```bash
  # View your learning progress
  python interactive_practice/progress_tracker.py
  # Set learning goals
  python interactive_practice/progress_tracker.py --set-goal "Master top 5 patterns"
  ```
- **Pattern Matcher Game:**
  ```bash
  # Play the pattern identification game
  python interactive_practice/pattern_matcher.py
  ```

## 🎴 Anki Flashcard Integration (Planned)

- **Quick Setup:**
  1. Download and install Anki.
  2. Import `anki_flashcards/complete_deck.apkg` (or individual pattern decks).
  3. Start studying with optimized spaced repetition!
- **Card Types Available:** Concept Cards, Implementation Cards, Interview Scenario Cards, Code Completion Cards, Diagram Cards.
- **Custom Flashcard Generation:**
  ```bash
  # Generate custom flashcards based on your progress
  python anki_flashcards/deck_sources/generate_cards.py --pattern singleton --difficulty intermediate
  ```

## 📈 Learning Paths

- **Beginner Path (2-3 weeks):** Focus on core concepts and basic challenges.
- **Interview Ready Path (4-6 weeks):** Master top patterns, timed challenges, and interview scenarios.
- **Advanced Path (Ongoing):** Tackle complex scenarios, code review, and contributions.

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- `pip` package manager
- Git

### Full Installation

```bash
# Clone the repository
git clone https://github.com/benkaan001/python-design-patterns-for-interviews.git
cd python-design-patterns-for-interviews

# 1. Create and activate a virtual environment
python3 -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
# venv\Scripts\activate.bat
# On Windows (PowerShell):
# .\venv\Scripts\Activate.ps1

# 2. Install dependencies from requirements.txt
pip install -r requirements.txt

# 3. Install the kernel for Jupyter Notebook (if using .ipynb files)
python -m ipykernel install --user --name=design_patterns_env --display-name "Python 3 (Design Patterns Env)"

# 4. To start Jupyter Notebook
# jupyter notebook

# 5. To deactivate the virtual environment when done
# deactivate
```

### Development Setup (Planned)

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
python -m flake8 design_patterns/
```

## 🎯 Usage Examples

- **Basic Pattern Study:**
  ```python
  # Example usage (assuming patterns are importable)
  from design_patterns.singleton.solutions.solution_01 import Logger
  logger = Logger()
  logger.info("Hello from Singleton!")
  ```
- **Interactive Quiz:**
  ```bash
  # Start a pattern quiz (once interactive_practice is implemented)
  python interactive_practice/quiz.py --pattern singleton --difficulty intermediate
  ```
- **Progress Tracking:**
  ```bash
  # Track your learning progress (once interactive_practice is implemented)
  python interactive_practice/progress_tracker.py log_completion singleton challenge_01
  python interactive_practice/progress_tracker.py show_progress
  ```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🌟 Ways to Contribute

- **Add New Challenges:** Create interesting scenarios for existing patterns.
- **Improve Solutions:** Enhance existing code with better practices, alternative solutions.
- **Create Flashcards:** Add new Anki cards for better learning.
- **Write Documentation:** Improve explanations and examples.
- **Report Issues:** Help us fix bugs and improve the experience.

### 📝 Contribution Process

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Make your changes.
4. Add tests for new functionality (if applicable).
5. Commit your changes (`git commit -m 'Add amazing feature'`).
6. Push to the branch (`git push origin feature/amazing-feature`).
7. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License.

Happy coding and good luck with your interviews! 🚀

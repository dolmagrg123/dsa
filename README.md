# Number Guessing Game 🎯

A sophisticated number guessing game built in Python that challenges players to guess a randomly generated combination with intelligent feedback and scoring system.

## Table of Contents
- [PURPOSE](#purpose)
- [OBJECTIVES](#objectives)
- [INSTALLATION](#installation)
- [CONCLUSION](#conclusion)

---


## PURPOSE

The Number Guessing Game is designed to provide an engaging, scalable gaming experience that demonstrates advanced programming concepts including:
- Object-oriented design principles
- External API integration with fallback mechanisms
- Persistent data storage and leaderboard management
- Input validation and error handling
- Modular architecture for maintainability

---

## OBJECTIVES

### Core Game Mechanics
- **10 attempts** maximum per game session
- **Configurable difficulty levels** (Easy: 4 digits, Medium: 8 digits, Difficult: custom length)
- **Dynamic digit range** based on difficulty (0-7 for easy/medium, 0-9 for difficult)
- **Multiplayer Option** Can play single player/two players
- **Intelligent feedback system** providing:
  - Count of correct numbers (regardless of position)
  - Count of numbers in correct positions
  - Descriptive feedback messages
-**Smart Hints** provide new hints when needed

### Example Gameplay
```
Game initializes and selects "0 1 3 5"
Player guesses "2 2 4 6" → "All digits input are incorrect"
Player guesses "0 2 4 6" → "1 correct number and 1 correct location"
Player guesses "2 2 1 1" → "1 correct number and 0 correct location"
Player guesses "0 1 5 6" → "3 correct numbers and 2 correct location"
```

### User Interface Features
- Intuitive command-line interface(Flask Integration Future)
- Real-time feedback on each guess
- Score tracking and display
- Remaining guesses counter
- Persistent leaderboard system
- Input validation with helpful error messages
- Single Player or Two player Option
- Chance to take a hint every round

---

## INSTALLATION

### Prerequisites
- Python 3.7 or higher
- Git (for cloning the repository)
- Internet connection (for external API, optional)

### Install Python

#### Windows
**Download Python:**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Download the latest Python 3.x version (3.7 or higher)

**Verify Installation:**
   ```cmd
   python --version
   pip --version
   ```

---

## CONCLUSION



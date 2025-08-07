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

### Step 1: Install Python

#### Windows
1. **Download Python:**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Download the latest Python 3.x version (3.7 or higher)

2. **Install Python:**
   - Run the downloaded installer
   - ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
   - Choose "Install Now" or customize installation as needed

3. **Verify Installation:**
   ```cmd
   python --version
   pip --version
   ```

#### macOS
1. **Option A - Using Homebrew (Recommended):**
   ```bash
   # Install Homebrew if not already installed
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python
   brew install python
   ```

2. **Option B - Direct Download:**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Download and install the macOS installer

3. **Verify Installation:**
   ```bash
   python3 --version
   pip3 --version
   ```

#### Linux (Ubuntu/Debian)
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

#### Linux (CentOS/RHEL/Fedora)
```bash
# For CentOS/RHEL
sudo yum install python3 python3-pip

# For Fedora
sudo dnf install python3 python3-pip

# Verify installation
python3 --version
pip3 --version
```

### Step 2: Install Git

#### Windows
1. Download Git from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer with default settings
3. Verify: `git --version` in Command Prompt

#### macOS
```bash
# Using Homebrew
brew install git

# Or use Xcode Command Line Tools
xcode-select --install
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt install git

# CentOS/RHEL
sudo yum install git

# Fedora
sudo dnf install git
```

### Step 3: Clone the Repository

```bash
https://github.com/dolmagrg123/dsa.git
cd dsa
```

### Step 4: Create Virtual Environment (Recommended)

A virtual environment keeps your project dependencies isolated from system Python packages.

#### Windows

**Option 1: Using Command Prompt (Recommended for beginners)**
```cmd
# Create virtual environment
python -m venv game_env

# Activate virtual environment
game_env\Scripts\activate.bat

# You should see (game_env) in your prompt
```

**Option 2: Using PowerShell**
```powershell
# Create virtual environment
python -m venv game_env

# If you get execution policy error, run ONE of these solutions:

# SOLUTION A: Change execution policy for current session (Temporary)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# SOLUTION B: Bypass execution policy for this command only
PowerShell -ExecutionPolicy Bypass -File "game_env\Scripts\Activate.ps1"

# SOLUTION C: Use the batch file instead
game_env\Scripts\activate.bat

# Then activate normally
game_env\Scripts\activate

# You should see (game_env) in your prompt
```

#### macOS/Linux
```bash
# Create virtual environment
python3 -m venv game_env

# Activate virtual environment
source game_env/bin/activate

# You should see (game_env) in your prompt
```

### Step 5: Install Project Dependencies

With your virtual environment activated:

#### Option A: Skip pip upgrade (Recommended for Windows)
```bash
# Install project dependencies directly
pip install -r requirements.txt
```

#### Option B: Upgrade pip (if needed)
```bash
# Windows - Use one of these if you get permission errors:
python -m pip install --upgrade pip --user
# OR
python -m pip install --upgrade pip --force-reinstall --no-deps

# macOS/Linux
pip install --upgrade pip

# Then install project dependencies
pip install -r requirements.txt
```

**If requirements.txt doesn't exist, manually install:**
```bash
pip install requests
```

---

## CONCLUSION



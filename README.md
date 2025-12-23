   # **SNAKE GAME**🐍

A classic Snake game developed using **Python** and **Pygame**.  
The project is built with a **modular and object-oriented (OOP)** design, making it easy to read, maintain, and extend.

## 🕹️ How to Play

- Use the **arrow keys** to move the snake in four directions.
- Eat the fruits to **increase your score** and grow the snake.
- Avoid hitting the **walls** or the **snake’s own body**.
- Each time you eat a fruit, a **new random fruit** appears on the map.
- The game ends when the snake crashes.
- Press **R** to retry after losing.
- Press **ESC** at any time to exit the game.

## ✔️ **Features:**
- **Score system**
  - Displays the current score during gameplay
  - Shows the highest score and the last score
  - Automatically saves the high score

- **Random fruits**
  - Fruits spawn at random locations on the map
  - Different fruit types supported

- **Sound effects** 🔊
  - Eating food sound
  - Game over sound

- **Game UI**
  - Main menu before starting the game
  - Retry key after losing
  - Exit key available at any moment
  - Score displayed during gameplay

- **Grid-based map**
  - The game map is divided into square cells (grid-based movement)


## 🔧 Project Architecture

The project is structured in a modular way and consists of three main files:

- **Classes file  (`snake.py`)**  
  Contains all core game classes and logic, such as the snake behavior, food system, and game rules.

- **Handle file (`handle.py`)**  
  Responsible for handling **Pygame**, rendering graphics, drawing game elements, and playing sounds.

- **Main file (`main.py`)**  
  Acts as the entry point of the game.  
  It initializes the game, sets the screen size, and connects all modules together.

## 🎮 **Controls:** 

- **Arrow Keys** → (↑, ↓, ←, →) to move the snake  
- **R** → Retry the game  
- **ESC** → Exit the game  

## 📥 Installation (From GitHub)

  Use command line in windows and terminal in linux to add this code to your IDE

### windows: ###
1. Download python 
   - Download Python from: https://www.python.org/downloads/
   - Make sure to check **"Add Python to PATH"** during installation
2. Clone the repository in cmd line:
   ```bash
   git clone https://github.com/sanamasghari/snake_game.git
3. Create and activate a virtual environment (recommended)
   ```bash 
   cd snake_game
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
4. Run the game
   ```bash
   python main.py
### linux: ###
1. Install python 
   ```bash 
   sudo apt update
   sudo apt install python3 python3-pip python3-venv

2. Clone the repository in cmd line:
   ```bash
   git clone https://github.com/sanamasghari/snake_game.git
3. Create and activate a virtual environment (recommended)
   ```bash 
   cd snake_game
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
4. Run the game
   ```bash
   python main.py
# TicTacToe (pygame)

This small TicTacToe project uses Pygame 2.6.1 and requires a Python 3.11 interpreter.

Why Python 3.11?
- Pygame 2.6.1 was built and tested against Python 3.11 in many environments. To avoid binary and compatibility issues (wheel availability, ABI changes), use Python 3.11 for the virtual environment.

Recommended setup (macOS / bash)

1. Install Python 3.11 if you don't have it. 
https://www.python.org/downloads/release/python-3111/

2. Create and activate a virtual environment using the Python 3.11 interpreter:


# create venv
python3.11 -m venv .venv

# activate venv (bash)
source .venv/bin/activate


3. Upgrade pip and install dependencies (Pygame 2.6.1):


python -m pip install --upgrade pip
python -m pip install pygame==2.6.1


4. Run the game:


python tictactoe.py


Notes
- If `python3.11` is not in your PATH, replace `python3.11` with the full path to the Python 3.11 binary (for example: `/usr/local/opt/python@3.11/bin/python3.11`).
- On some systems Pygame installs a binary wheel; if you see a build-from-source step, make sure you have Xcode command line tools and the SDL dependencies installed (Homebrew can help).

Troubleshooting
- "ModuleNotFoundError: No module named 'pygame'": Ensure the venv is activated and `pygame==2.6.1` is installed into it.
- If you need to recreate the venv, delete `.venv/` and repeat steps above.

License
- This project is provided as-is for demonstration and learning.

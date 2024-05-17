# Mouse Tracker

Mouse Tracker is a simple Python application that tracks the mouse position on the screen and records the positions when the left mouse button is clicked. It uses `tkinter` for the GUI and `pynput` for tracking the mouse events. The application can be packaged into an executable using `pyinstaller`.

## Features

- Display the current mouse position.
- Record and display the positions where the left mouse button is clicked.
- Always stay on top of other windows.
- Resizable window.
- Custom application icon.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `pynput`
- `pyinstaller` (for creating an executable)

## Installation

### Using pip

1. Install the required packages:
    ````shell
   pip install pynput
2. If tkinter is not installed, install it using:
    ````shell
   conda install tk

3. Install pyinstaller to create an executable:
    ````shell
   conda install pyinstaller
   
## Project Structure

```
MouseTracker/
├── src/
│   └── mouse_tracker.py
├── dist/
│   └── (where the executable will be created)
├── build/
│   └── (build artifacts will be placed here)
├── assets/
│   └── icon.ico
└── README.md
```
## Running the Application
1. Navigate to the src directory:
    ````shell
   cd src
2. Run the application:
    ````shell
   python mouse_tracker.py

## Creating an Executable
1. Navigate to the project directory:
    ````shell
    cd path\to\MouseTracker
2. Run pyinstaller to create the executable:
    ````shell
    pyinstaller --onefile --windowed src\mouse_tracker.py
3. The executable will be found in the dist directory:
    ````shell
    cd dist
4. Run the executable:
    ````shell
    .\mouse_tracker.exe
## Custom Icon

To use a custom icon, place your icon.ico file in the assets directory and ensure the path in the script points to this file:
```` python
icon_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icon.ico')
self.root.iconbitmap(icon_path)
````
## License
This project is licensed under the MIT License. See the LICENSE file for details.

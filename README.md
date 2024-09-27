Task Automation App is a desktop application that allows users to record and replay mouse and keyboard actions. This is useful for automating repetitive tasks. The application is built with Python and uses tkinter for the GUI, pyinstaller for building the .exe, and pickle for storing recorded actions.

Features
Record Actions: Capture mouse movements, clicks, and keyboard actions.
Stop Recording: Stop the recording process with a button in the GUI.
Replay Actions: Replay the recorded actions to automate tasks.
Graphical User Interface (GUI): Easy-to-use interface built with tkinter.
Standalone Executable: Build the app into an .exe for Windows without requiring Python installation.
Getting Started
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x
tkinter (usually comes with Python)
mouse and keyboard modules
pyinstaller (for building the .exe)
You can install the necessary dependencies with the following commands:
pip install pyinstaller
pip install mouse
pip install keyboard

Installation
Clone the Repository:

git clone https://github.com/obtranzat/TaskAutomation.git
cd task-automation-app
Run the Application:

python app.py
This will start the GUI, allowing you to record, stop, and replay actions.

Build the Executable (Optional):
If you want to create a standalone Windows .exe, you can use pyinstaller:

pyinstaller --onefile --noconsole app.py
pyinstaller --onefile --noconsole record.py
pyinstaller --onefile --noconsole replay.py
This will create an app.exe, record.exe, replay.exe files in the dist/ folder.

Usage
Recording Actions
Open the application and click "Start Recording."
Perform the actions you want to record (mouse clicks, movements, and keyboard input).
Click "Stop Recording" to end the session. The recorded actions will be saved automatically.
Replaying Actions
Click "Replay Actions" in the GUI to replay the previously recorded actions.

How It Works
Recording: The app uses the mouse and keyboard Python libraries to track user input and saves the actions with timestamps.
Replay: The recorded actions are read from a file and replayed with the same timing using time.sleep() to simulate delays between actions.
GUI: The user interface is created with tkinter, allowing users to start/stop recordings and replay actions easily.
Customization
You can modify the behavior of the recording and replay functions by editing record.py and replay.py. For example, you could add more complex automation behavior or adjust the timing between actions.

Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue. All contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or suggestions, feel free to contact me:

Email: obtrazat@gmail.com
GitHub: obtranzat

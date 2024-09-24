# MyJiggler

**MyJiggler** is a lightweight Python application that detects inactivity on Windows and automatically "jiggles" the mouse to prevent the system from going idle. This is useful in scenarios where you don't want the system to enter sleep mode or lock due to inactivity.

## Features
- Detects system inactivity based on user input.
- Jiggles the mouse to simulate activity if the system has been idle for a specified duration.
- Configurable idle threshold.
- Countdown notification before the mouse jiggle.

## Requirements
- Python 3.x
- Windows OS
- Python packages:
  - `MouseInfo`
  - `PyAutoGUI`
  - `PyGetWindow`
  - `PyMsgBox`
  - `pyperclip`
  - `PyRect`
  - `PyScreeze`
  - `pytweening`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gibbids/MyJiggler.git
    ```

2. Navigate to the project directory:
    ```bash
    cd MyJiggler
    ```

3. Create and activate a virtual environment (optional but recommended):
    - **Windows**:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

4. Install the required packages from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open a terminal in the project directory.
2. Run the application:
    ```bash
    python main.py
    ```
3. The program will monitor the system for inactivity. If the system is idle for more than the configured threshold, the mouse will be slightly moved to simulate activity.

### Customizing Idle Threshold and Countdown
You can customize the idle threshold, countdown time, and messages by editing the `config.json` file.

## How it Works

The application uses Windows system calls to monitor the time since the last user input (keyboard or mouse). When the idle time exceeds the threshold, the `pyautogui` library is used to move the mouse slightly to keep the system active. A countdown notification is shown before the mouse jiggle.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## Author

Gabriel Osmo  
[github/gibbids](https://github.com/gibbids)  
[gabeosmo@outlook.com](mailto:gabeosmo@outlook.com)

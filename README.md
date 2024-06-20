# HandGestureVolumeControl

HandGestureVolumeControl is a Python project that uses computer vision and machine learning to control the system volume through hand gestures. By leveraging OpenCV and MediaPipe for hand detection and tracking, and pycaw for volume control on Windows, this project allows users to adjust the system volume by moving their thumb and index finger.

## Features

- Real-time hand detection and tracking using MediaPipe.
- Adjust system volume based on hand gestures.
- Intuitive and touch-free control of audio levels.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/HandGestureVolumeControl.git
    cd HandGestureVolumeControl
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Install additional dependencies:
    ```sh
    pip install opencv-python mediapipe pycaw comtypes
    ```

## Usage

Run the main script to start the hand gesture volume control:
```sh
python gesture_volume_control.py


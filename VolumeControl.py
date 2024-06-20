import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import numpy as np

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Function to calculate the distance between two landmarks
def calculate_distance(landmark1, landmark2):
    return np.sqrt((landmark1.x - landmark2.x) ** 2 + (landmark1.y - landmark2.y) ** 2 + (landmark1.z - landmark2.z) ** 2)

# Function to set system volume
def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get the current volume level and set the new volume level
    volume.SetMasterVolumeLevelScalar(level / 100.0, None)

# Open a connection to the default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks and identify gestures
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate the distance between the tip of the thumb and the tip of the index finger
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            distance = calculate_distance(thumb_tip, index_finger_tip)

            # Normalize the distance to a range from 0 to 100
            max_distance = 0.2  # Adjust this value based on your camera setup and hand size
            volume_level = np.clip((1 - (distance / max_distance)) * 100, 0, 100)

            # Set the system volume based on the calculated volume level
            set_volume(volume_level)

            # Display the volume level on the frame
            cv2.putText(frame, f'Volume: {int(volume_level)}%', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Wait for a short period and capture any key press
    key = cv2.waitKey(1)

    # Exit the loop if 'q' is pressed or window is closed
    if key & 0xFF == ord('q') or cv2.getWindowProperty('Camera Feed', cv2.WND_PROP_AUTOSIZE) == -1:
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()










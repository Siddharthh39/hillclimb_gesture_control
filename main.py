import cv2
import mediapipe as mp
from pynput.keyboard import Controller, Key
import time

# Setup
keyboard = Controller()
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Gesture tracking states
pressing_gas = False
pressing_brake = False

def is_fist(landmarks):
    fingers = []
    tips_ids = [8, 12, 16, 20]
    for tip in tips_ids:
        if landmarks[tip].y > landmarks[tip - 2].y:
            fingers.append(0)  # folded
        else:
            fingers.append(1)  # extended
    return sum(fingers) == 0

def is_open_hand(landmarks):
    fingers = []
    tips_ids = [8, 12, 16, 20]
    for tip in tips_ids:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)  # extended
        else:
            fingers.append(0)  # folded
    return sum(fingers) == 4

while True:
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmark_list = hand_landmarks.landmark

            if is_open_hand(landmark_list):
                if not pressing_gas:
                    keyboard.press(Key.right)
                    pressing_gas = True
                    pressing_brake = False
                    keyboard.release(Key.left)
                    print("Gas")
            elif is_fist(landmark_list):
                if not pressing_brake:
                    keyboard.press(Key.left)
                    pressing_brake = True
                    pressing_gas = False
                    keyboard.release(Key.right)
                    print("Brake")
            else:
                keyboard.release(Key.left)
                keyboard.release(Key.right)
                pressing_brake = False
                pressing_gas = False

    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        pressing_brake = False
        pressing_gas = False

    cv2.imshow("Gesture Controller", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press Esc to quit
        break

cap.release()
cv2.destroyAllWindows()

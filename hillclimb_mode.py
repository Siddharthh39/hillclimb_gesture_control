import cv2
import mediapipe as mp
import pyautogui
import time

def run():
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils

    pressing_gas = False
    pressing_brake = False

    def is_fist(landmarks):
        fingers = []
        tips_ids = [8, 12, 16, 20]
        for tip in tips_ids:
            fingers.append(0 if landmarks[tip].y > landmarks[tip - 2].y else 1)
        return sum(fingers) == 0

    def is_open_hand(landmarks):
        fingers = []
        tips_ids = [8, 12, 16, 20]
        for tip in tips_ids:
            fingers.append(1 if landmarks[tip].y < landmarks[tip - 2].y else 0)
        return sum(fingers) == 4

    while True:
        success, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmark_list = hand_landmarks.landmark

                if is_open_hand(landmark_list):
                    if not pressing_gas:
                        pyautogui.keyDown("right")
                        pressing_gas = True
                        pressing_brake = False
                        pyautogui.keyUp("left")
                        print("Gas")
                    time.sleep(0.1)

                elif is_fist(landmark_list):
                    if not pressing_brake:
                        pyautogui.keyDown("left")
                        pressing_brake = True
                        pressing_gas = False
                        pyautogui.keyUp("right")
                        print("Brake")
                    time.sleep(0.1)

                else:
                    pyautogui.keyUp("left")
                    pyautogui.keyUp("right")
                    pressing_brake = False
                    pressing_gas = False

        else:
            # Debug: When no hand landmarks are detected
            pyautogui.keyUp("left")
            pyautogui.keyUp("right")
            pressing_brake = False
            pressing_gas = False

        cv2.imshow("Gesture Controller", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            print("Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

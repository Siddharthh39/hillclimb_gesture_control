import cv2
import mediapipe as mp
import pyautogui
import time

def run():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    
    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        return

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils

    pressing_gas = False
    pressing_brake = False

    def is_fist(landmarks):
        return all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20])

    def is_open_hand(landmarks):
        return all(landmarks[tip].y < landmarks[tip - 2].y for tip in [8, 12, 16, 20])

    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1) 
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmark_list = hand_landmarks.landmark

                if is_open_hand(landmark_list):
                    if not pressing_gas:
                        pyautogui.keyDown("right")
                        pyautogui.keyUp("left")
                        pressing_gas = True
                        pressing_brake = False
                        print("Gas")
                    time.sleep(0.1)

                elif is_fist(landmark_list):
                    if not pressing_brake:
                        pyautogui.keyDown("left")
                        pyautogui.keyUp("right")
                        pressing_brake = True
                        pressing_gas = False
                        print("Brake")
                    time.sleep(0.1)

                else:
                    pyautogui.keyUp("left")
                    pyautogui.keyUp("right")
                    pressing_brake = False
                    pressing_gas = False

        else:
            pyautogui.keyUp("left")
            pyautogui.keyUp("right")
            pressing_brake = False
            pressing_gas = False

        cv2.imshow("Gesture Controller", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

import cv2
import mediapipe as mp
import pyautogui
import time
import threading

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

pressing_keys = {"a": False, "d": False, "space": False}

last_times = {
    "two_fingers_up": 0,
    "ok_gesture": 0,
    "three_fingers_up": 0,
    "palm_facing_camera": 0,
    "thumb_up": 0,
    "pinch": 0,
    "fist_tilted": 0
}

def is_fist(landmarks):
    return all(landmarks[tip].y > landmarks[tip - 2].y for tip in [8, 12, 16, 20])

def is_open_hand(landmarks):
    return all(landmarks[tip].y < landmarks[tip - 2].y for tip in [8, 12, 16, 20])

def is_index_up(landmarks):
    return landmarks[8].y < landmarks[6].y and all(landmarks[f].y > landmarks[f - 2].y for f in [12, 16, 20])

def is_two_fingers_up(landmarks):
    return (landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y and
            all(landmarks[f].y > landmarks[f - 2].y for f in [16, 20]))

def is_ok_gesture(landmarks):
    return abs(landmarks[4].x - landmarks[8].x) < 0.05 and abs(landmarks[4].y - landmarks[8].y) < 0.05

def is_three_fingers_up(landmarks):
    return all(landmarks[f].y < landmarks[f - 2].y for f in [8, 12, 16])

def is_palm_facing_camera(landmarks):
    return is_open_hand(landmarks) and landmarks[4].x < landmarks[3].x

def is_thumb_up(landmarks):
    return landmarks[4].y < landmarks[3].y and all(landmarks[f].y > landmarks[f - 2].y for f in [8, 12, 16, 20])

def is_pinch(landmarks):
    return abs(landmarks[4].x - landmarks[8].x) < 0.02

def is_fist_tilted(landmarks):
    return is_fist(landmarks) and abs(landmarks[0].x - landmarks[9].x) > 0.02

def process_frame():
    while True:
        success, frame = cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                lm = handLms.landmark
                current_time = time.time()

                cooldown_gesture_triggered = False
                for gesture, key, cooldown in [
                    ("two_fingers_up", "shift", 0.5),
                    ("ok_gesture", "x", 0.5),
                    ("three_fingers_up", "z", 1),
                    ("palm_facing_camera", "tab", 1),
                    ("thumb_up", "c", 1),
                    ("pinch", "v", 1),
                    ("fist_tilted", "f", 1)
                ]:
                    if globals()[f"is_{gesture}"](lm) and (current_time - last_times[gesture] > cooldown):
                        pyautogui.press(key)
                        last_times[gesture] = current_time
                        cooldown_gesture_triggered = True
                        break 

                if not cooldown_gesture_triggered:
                    if is_fist(lm):
                        if not pressing_keys["a"]:
                            pyautogui.keyDown("a")
                            pressing_keys["a"] = True
                    else:
                        if pressing_keys["a"]:
                            pyautogui.keyUp("a")
                            pressing_keys["a"] = False

                    if is_open_hand(lm):
                        if not pressing_keys["d"]:
                            pyautogui.keyDown("d")
                            pressing_keys["d"] = True
                    else:
                        if pressing_keys["d"]:
                            pyautogui.keyUp("d")
                            pressing_keys["d"] = False

                    if is_index_up(lm):
                        if not pressing_keys["space"]:
                            pyautogui.keyDown("space")
                            pressing_keys["space"] = True
                    else:
                        if pressing_keys["space"]:
                            pyautogui.keyUp("space")
                            pressing_keys["space"] = False

        cv2.imshow("Hollow Knight Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print("🎮 Gesture Controller Ready! Press 'q' to quit.")
time.sleep(2)

thread = threading.Thread(target=process_frame)
thread.start()
thread.join()

cap.release()
cv2.destroyAllWindows()

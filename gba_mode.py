import cv2
import mediapipe as mp
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def run():
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils

    cooldown = 0.5
    last_action = {'a': 0, 'b': 0, 'shift': 0, 'right': 0, 'left': 0}

    def is_fist(landmarks):
        tips_ids = [8, 12, 16, 20]
        return all(landmarks[tip].y > landmarks[tip - 2].y for tip in tips_ids)

    def is_open_hand(landmarks):
        tips_ids = [8, 12, 16, 20]
        return all(landmarks[tip].y < landmarks[tip - 2].y for tip in tips_ids)

    def is_index_finger_up(landmarks):
        return (landmarks[8].y < landmarks[6].y and 
                landmarks[12].y > landmarks[10].y and 
                landmarks[16].y > landmarks[14].y and 
                landmarks[20].y > landmarks[18].y)

    def is_two_fingers_up(landmarks):
        return (landmarks[8].y < landmarks[6].y and 
                landmarks[12].y < landmarks[10].y and 
                landmarks[16].y > landmarks[14].y and 
                landmarks[20].y > landmarks[18].y)

    def is_ok_gesture(landmarks):
        dist_x = abs(landmarks[4].x - landmarks[8].x)
        dist_y = abs(landmarks[4].y - landmarks[8].y)
        return dist_x < 0.05 and dist_y < 0.05

    def press_key(k):
        keyboard.press(k)
        keyboard.release(k)

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
                now = time.time()

                if is_index_finger_up(landmark_list):
                    if now - last_action['a'] > cooldown:
                        press_key('z')  # GBA A
                        last_action['a'] = now
                        print("Gesture: Index finger up → A (Z)")
                elif is_two_fingers_up(landmark_list):
                    if now - last_action['b'] > cooldown:
                        press_key('x')  # GBA B
                        last_action['b'] = now
                        print("Gesture: Two fingers up → B (X)")
                elif is_ok_gesture(landmark_list):
                    if now - last_action['shift'] > cooldown:
                        press_key('s')  # GBA R
                        last_action['shift'] = now
                        print("Gesture: OK → R (S)")
                elif is_open_hand(landmark_list):
                    if now - last_action['right'] > cooldown:
                        press_key(Key.right)
                        last_action['right'] = now
                        print("Gesture: Open Hand → Right")
                elif is_fist(landmark_list):
                    if now - last_action['left'] > cooldown:
                        press_key(Key.left)
                        last_action['left'] = now
                        print("Gesture: Fist → Left")

        cv2.imshow("GBA Gesture Controller", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("🎮 Make sure the GBA emulator is in focus!")
    print("⏳ Starting in 3 seconds...")
    time.sleep(3)
    run()

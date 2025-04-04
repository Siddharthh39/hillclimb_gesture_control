import cv2
import mediapipe as mp
import time
import vgamepad as vg

def run():
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils
    gamepad = vg.VX360Gamepad()

    cooldown = 0.4
    last_action = {key: 0 for key in ['jump', 'dash', 'attack', 'left', 'right']}

    print("🎮 Hollow Knight Gesture Controller Ready!")
    print("🕹️  Make sure Hollow Knight is in focus!")
    print("🚀 Starting in 3 seconds...")
    time.sleep(3)

    def is_fist(landmarks):
        tips = [8, 12, 16, 20]
        return all(landmarks[tip].y > landmarks[tip - 2].y for tip in tips)

    def is_open_hand(landmarks):
        tips = [8, 12, 16, 20]
        return all(landmarks[tip].y < landmarks[tip - 2].y for tip in tips)

    def is_index_up(landmarks):
        return (landmarks[8].y < landmarks[6].y and 
                all(landmarks[i].y > landmarks[i - 2].y for i in [12, 16, 20]))

    def is_two_fingers_up(landmarks):
        return (landmarks[8].y < landmarks[6].y and
                landmarks[12].y < landmarks[10].y and
                all(landmarks[i].y > landmarks[i - 2].y for i in [16, 20]))

    def is_ok_gesture(landmarks):
        return abs(landmarks[4].x - landmarks[8].x) < 0.05 and abs(landmarks[4].y - landmarks[8].y) < 0.05

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                lm = handLms.landmark
                now = time.time()

                if is_index_up(lm) and now - last_action['jump'] > cooldown:
                    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # Jump
                    gamepad.update()
                    time.sleep(0.1)
                    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    gamepad.update()
                    print("🟢 Jump (A)")
                    last_action['jump'] = now

                elif is_two_fingers_up(lm) and now - last_action['dash'] > cooldown:
                    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)  # Dash
                    gamepad.update()
                    time.sleep(0.1)
                    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                    gamepad.update()
                    print("🟡 Dash (RT)")
                    last_action['dash'] = now

                elif is_ok_gesture(lm) and now - last_action['attack'] > cooldown:
                    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  # Attack
                    gamepad.update()
                    time.sleep(0.1)
                    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    gamepad.update()
                    print("🟣 Attack (X)")
                    last_action['attack'] = now

                elif is_open_hand(lm) and now - last_action['right'] > cooldown:
                    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)  # Move Right
                    gamepad.update()
                    time.sleep(0.1)
                    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                    gamepad.update()
                    print("🔵 Right")
                    last_action['right'] = now

                elif is_fist(lm) and now - last_action['left'] > cooldown:
                    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # Move Left
                    gamepad.update()
                    time.sleep(0.1)
                    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                    gamepad.update()
                    print("🔴 Left")
                    last_action['left'] = now

        cv2.imshow("🖐️ Hollow Knight Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

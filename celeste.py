import cv2
import mediapipe as mp
import time
import vgamepad as vg

def run():
    # Initialize virtual gamepad (Xbox 360 Controller)
    gamepad = vg.VX360Gamepad()

    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils

    cooldown = 0.4
    last_action = {
        'jump': 0, 'dash': 0, 'climb': 0,
        'left': 0, 'right': 0
    }

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

    print("🎮 Celeste Controller via Virtual Gamepad Ready!")
    print("🕹️  Ensure Celeste is set to use a controller and is in focus!")
    print("🚀 Starting in 3 seconds...")
    time.sleep(3)

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = hand_landmarks.landmark
                now = time.time()

                if is_index_finger_up(landmarks):
                    if now - last_action['jump'] > cooldown:
                        # Map jump to A button
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                        gamepad.update()
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                        gamepad.update()
                        last_action['jump'] = now
                        print("🟢 Jump (A)")
                elif is_two_fingers_up(landmarks):
                    if now - last_action['dash'] > cooldown:
                        # Map dash to B button
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                        gamepad.update()
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                        gamepad.update()
                        last_action['dash'] = now
                        print("🟡 Dash (B)")
                elif is_ok_gesture(landmarks):
                    if now - last_action['climb'] > cooldown:
                        # Map climb to X button
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                        gamepad.update()
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                        gamepad.update()
                        last_action['climb'] = now
                        print("🟣 Climb (X)")
                elif is_open_hand(landmarks):
                    if now - last_action['right'] > cooldown:
                        # Map open hand to D-Pad Right
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                        gamepad.update()
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                        gamepad.update()
                        last_action['right'] = now
                        print("🔵 Right D-Pad")
                elif is_fist(landmarks):
                    if now - last_action['left'] > cooldown:
                        # Map fist to D-Pad Left
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                        gamepad.update()
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                        gamepad.update()
                        last_action['left'] = now
                        print("🔴 Left D-Pad")

        cv2.imshow("🖐️ Celeste Virtual Gamepad Controller", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            print("👋 Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

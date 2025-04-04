# Gesture-Controlled Hill Climb Racing Mod 🎮✋

Control the gas and brake in Hill Climb Racing (or similar games) using **hand gestures** captured by your webcam.  
Open palm = Gas | Fist = Brake.

## 🧠 How it Works

- Uses **MediaPipe** to detect your hand landmarks in real-time.
- Interprets gestures:
  - **Open hand** → Press **Gas**
  - **Fist (closed hand)** → Press **Brake**
- Simulates keyboard input using **pynput** to control the game.

No touch. Just gestures.

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt

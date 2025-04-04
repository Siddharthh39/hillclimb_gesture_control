# Gesture-Controlled Game Mod 🎮✋

Control **Hill Climb Racing** and **GBA Emulator games** using hand gestures via your webcam.  
No controller, no keyboard – just gestures.

---

## 🧠 How it Works

- Uses **MediaPipe** to detect hand landmarks in real-time.
- Interprets your gestures and sends simulated keyboard input via **pynput**.
- Works for:
  - 🏁 Hill Climb Racing (Gas/Brake)
  - 🎮 GBA Emulator games like Pokémon (Move, Jump, Attack, Sprint)

---

## ✋ Available Gesture Controls

### 🏁 Hill Climb Racing Mode
| Gesture        | Action         | Key |
|----------------|----------------|-----|
| 🖐️ Open Hand   | Press Gas       | →   |
| ✊ Fist         | Press Brake     | ←   |

### 🎮 GBA Emulator Mode (e.g., Pokémon)
| Gesture              | Action             | Key       |
|----------------------|--------------------|-----------|
| ☝️ Index Finger Up    | Jump / Select      | `A`       |
| ✌️ Two Fingers Up     | Attack / Special   | `B`       |
| 👌 OK Gesture         | Run / Sprint       | `Shift`   |
| 🖐️ Open Hand          | Move Right         | →         |
| ✊ Fist               | Move Left          | ←         |

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt

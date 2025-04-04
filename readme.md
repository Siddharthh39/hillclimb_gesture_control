# 🎮 Gesture-Controlled Game Mod ✋  

Control **Hill Climb Racing**, **GBA Emulator games**, and **Hollow Knight** using hand gestures via your webcam.  
No controller, no keyboard – just gestures.

---

## 🧠 How it Works  

- Uses **MediaPipe** to detect hand landmarks in real-time.  
- Interprets your gestures and sends simulated **keyboard** or **controller (vgamepad)** input.  
- Works for:
  - 🏁 **Hill Climb Racing** (Gas/Brake)  
  - 🎮 **GBA Emulator** games (Move, Jump, Attack, Sprint)  
  - 🏹 **Hollow Knight** (Move, Jump, Attack, Dash)  

---

## ✋ Available Gesture Controls  

### 🏁 Hill Climb Racing Mode  
| Gesture        | Action         | Key |
|---------------|---------------|-----|
| 🖐️ Open Hand   | Press Gas      | →   |
| ✊ Fist        | Press Brake    | ←   |

### 🎮 GBA Emulator Mode (e.g., Pokémon)  
| Gesture       | Action         | Key       |
|--------------|---------------|-----------|
| ☝️ Index Up   | Jump / Select | `A`       |
| ✌️ Two Fingers Up  | Attack / Special | `B`       |
| 👌 OK Gesture | Run / Sprint  | `Shift`   |
| 🖐️ Open Hand  | Move Right    | →         |
| ✊ Fist       | Move Left     | ←         |

### 🏹 Hollow Knight Mode  
| Gesture       | Action        | Xbox Button (vgamepad) |
|--------------|--------------|-------------------------|
| ☝️ Index Up   | Jump         | `A`                     |
| ✌️ Two Fingers Up  | Dash         | `RT`                    |
| 👌 OK Gesture | Attack       | `X`                     |
| 🖐️ Open Hand  | Move Right   | D-Pad Right             |
| ✊ Fist       | Move Left    | D-Pad Left              |

---

## 📦 Requirements  

Install the required Python packages:  

```bash
pip install -r requirements.txt
```

Make sure you have:  
- **ViGEmBus installed (for virtual gamepad support)**
- **Hollow Knight running in focus**
- **A webcam for hand tracking**

---

## 🚀 Usage  

Run the script and select your game mode:  

```bash
python main.py
```

Press `Q` to exit at any time.  

---


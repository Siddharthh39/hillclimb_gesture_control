# 🎮 Gesture-Controlled Game Mod ✋  

Control **Hill Climb Racing** and **Hollow Knight** using hand gestures via your webcam.  
No controller, no keyboard – just gestures.

---

## 🧠 How it Works  

- Uses **MediaPipe** to detect hand landmarks in real-time.  
- Interprets your gestures and sends simulated **keyboard** or **controller (vgamepad)** input.  
- Works for:
  - 🏁 **Hill Climb Racing** (Gas/Brake)  
  - 🏹 **Hollow Knight** (Move, Jump, Attack, Dash)  

---

## ✋ Available Gesture Controls  

### 🏁 Hill Climb Racing Mode  
| Gesture        | Action         | Key |
|---------------|----------------|-----|
| 🖐️ Open Hand   | Press Gas      | →   |
| ✊ Fist        | Press Brake    | ←   |

### 🏹 Hollow Knight Mode  
| Gesture           | Action        | Keyboard Key |
|------------------|---------------|---------------|
| ☝️ Index Up       | Jump          | `Space`       |
| ✌️ Two Fingers Up | Dash          | `Shift`       |
| 👌 OK Gesture     | Attack        | `X`           |
| 🖐️ Open Hand      | Move Right    | `D`           |
| ✊ Fist           | Move Left     | `A`           |
| 🤟 Three Fingers Up | Special/Spell | `Z`         |
| ✋ Palm Facing Camera | Open Map   | `Tab`         |
| 👍 Thumb Up       | Heal          | `C`           |
| 🤏 Pinch Gesture  | Spell Attack  | `V`           |
| ✊ (Tilted Fist)  | Interact      | `F`           |

---

## 📦 Requirements  

Install the required Python packages:  

```bash
pip install -r requirements.txt
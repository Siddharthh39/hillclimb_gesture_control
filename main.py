import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import winsound
import os

def play_click_sound():
    try:
        winsound.PlaySound("click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    except:
        pass  # Ignore errors silently

def run_hillclimb():
    play_click_sound()
    update_status("Running Hill Climb Racing...")
    import hillclimb_mode
    threading.Thread(target=hillclimb_mode.run).start()

def run_hollowknight():
    play_click_sound()
    update_status("Running Hollow Knight...")
    import hollowKnight
    threading.Thread(target=hollowKnight.run).start()

def show_instructions():
    play_click_sound()
    instructions = (
        "🕹️ Gesture Controls:\n\n"
        "🚗 Hill Climb Racing:\n"
        "  - 🖐️ Open Hand → Gas (Right Arrow)\n"
        "  - ✊ Fist → Brake (Left Arrow)\n\n"
        "🏹 Hollow Knight:\n"
        "  - ☝️ Index Up → Jump (A)\n"
        "  - ✌️ Two Fingers Up → Dash (RT)\n"
        "  - 👌 OK Gesture → Attack (X)\n"
        "  - 🖐️ Open Hand → Move Right (D-Pad Right)\n"
        "  - ✊ Fist → Move Left (D-Pad Left)"
    )
    messagebox.showinfo("Gesture Instructions", instructions)

def update_status(text):
    status_var.set(text)

def main():
    global status_var
    root = tk.Tk()
    root.title("Game Mode Selector")
    root.geometry("400x400")
    root.resizable(False, False)

    # Set background image
    try:
        bg_image = Image.open("background.png")
        bg_image = bg_image.resize((400, 400), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        bg_photo = None  # fallback if image not found

    label = tk.Label(root, text="Choose Game Mode:", font=("Arial", 14), bg="#ffffff")
    label.pack(pady=20)

    tk.Button(root, text="Hill Climb Racing", command=run_hillclimb, width=30, font=("Arial", 12)).pack(pady=10)
    tk.Button(root, text="Hollow Knight", command=run_hollowknight, width=30, font=("Arial", 12)).pack(pady=10)
    tk.Button(root, text="Show Instructions", command=show_instructions, width=30, font=("Arial", 12)).pack(pady=10)
    tk.Button(root, text="Quit", command=root.quit, width=30, font=("Arial", 12), bg="red", fg="white").pack(pady=10)

    status_var = tk.StringVar()
    status_var.set("Select a game to start...")
    status_label = tk.Label(root, textvariable=status_var, font=("Arial", 10), bg="#ffffff", fg="gray")
    status_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
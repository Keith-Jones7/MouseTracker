from pynput import mouse
import tkinter as tk
from tkinter import ttk
import os


class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Tracker")
        self.root.geometry("300x200")
        self.root.attributes('-topmost', True)
        self.root.resizable(True, True)  # Allow the window to be resizable

        # Set the window icon using an ICO file
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icon.ico')
        try:
            self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error loading icon: {e}")

        self.position_label = ttk.Label(self.root, text="Mouse position: ", font=('Arial', 14))
        self.position_label.pack(pady=10, fill=tk.X)

        self.recorded_positions = tk.Text(self.root, height=5, width=35)
        self.recorded_positions.pack(pady=10, expand=True, fill=tk.BOTH)

        self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click)
        self.listener.start()

    def on_move(self, x, y):
        self.position_label.config(text=f"Mouse position: ({x}, {y})")

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self.recorded_positions.insert(tk.END, f"Recorded position: ({x}, {y})\n")
            self.recorded_positions.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MouseTrackerApp(root)
    root.mainloop()

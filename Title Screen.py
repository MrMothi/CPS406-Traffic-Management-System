import tkinter as tk
from tkinter import font



def admin_login():
    print("Admin Login")

def normal_login():
    print("Normal Login")

def create_title_screen():
    title_screen = tk.Tk()
    title_screen.title("Traffic System")
    title_screen.geometry("800x600")

    # Title
    title_label = tk.Label(title_screen, text="MetroFloPro", font=("Khmer UI", 32, "bold"))
    title_label.pack(pady=100)

    # Administrative Login Button
    admin_login_button = tk.Button(title_screen, text="Administrative Login", font=("Times", 14), command=admin_login)
    admin_login_button.pack(pady=20)

    # Normal Login Button
    normal_login_button = tk.Button(title_screen, text="Normal Login", font=("Times", 14), command=normal_login)
    normal_login_button.pack(pady=20)

    # Center the window on the screen
    title_screen.update_idletasks()
    width = title_screen.winfo_width()
    height = title_screen.winfo_height()
    x = (title_screen.winfo_screenwidth() // 2) - (width // 2)
    y = (title_screen.winfo_screenheight() // 2) - (height // 2)
    title_screen.geometry("{}x{}+{}+{}".format(width, height, x, y))

    title_screen.mainloop()

if __name__ == "__main__":
    create_title_screen()

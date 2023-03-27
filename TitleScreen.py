import tkinter as tk
import subprocess
import Normal_login
import Admin_login

def admin_login(root):
    print("Admin Login")
    root.destroy()
    Admin_login.main()
    

def normal_login(root):
    print("Normal Login")
    root.destroy()
    Normal_login.main()
    

def create_title_screen():
    root = tk.Tk()
    root.title("Traffic System")
    root.geometry("800x600")

    # Title
    title_label = tk.Label(root, text="MetroFloPro", font=("Khmer UI", 32, "bold"))
    title_label.pack(pady=100)

    # Administrative Login Button
    admin_login_button = tk.Button(root, text="Administrative Login", font=("Times", 14), command=lambda: admin_login(root))
    admin_login_button.pack(pady=20)

    # Normal Login Button
    normal_login_button = tk.Button(root, text="Normal Login", font=("Times", 14), command=lambda: normal_login(root))
    normal_login_button.pack(pady=20)

    # Center the window on the screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

    root.mainloop()

if __name__ == "__main__":
    create_title_screen()

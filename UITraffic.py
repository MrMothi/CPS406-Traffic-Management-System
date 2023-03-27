import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

def main():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        print("Username:", username)
        print("Password:", password)

    # Create a logo
    def create_arrow_image(size, fill_color):
        img = Image.new('RGBA', size, color=(255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        # Draw logo
        draw.polygon([(0, size[1] / 2), (size[0] / 2, 0), (size[0], size[1] / 2), (size[0] / 2, size[1])], fill=fill_color)

        return img

    # Create background
    def create_gradient_background(width, height, start_color, end_color):
        gradient = Image.new('RGBA', (width, height), color=0)
        draw = ImageDraw.Draw(gradient)

        for i in range(height):
            c = [round((end_color[j] - start_color[j]) * i / height + start_color[j]) for j in range(3)]
            draw.line([(0, i), (width, i)], fill=tuple(c))

        return gradient

    def on_resize(event):
        width = event.width
        height = event.height
        gradient_image = create_gradient_background(width, height, (0, 102, 204), (255, 255, 255))
        gradient = ImageTk.PhotoImage(gradient_image)
        background_label.config(image=gradient)
        background_label.image = gradient

    root = tk.Tk()
    root.title("Login")
    root.bind("<Configure>", on_resize)

    # Set size
    window_width = 800
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    # Calculate the center of the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))

    # Set the window position to the center of the screen
    root.geometry(f"+{x_coordinate}+{y_coordinate}")

    # Create a gradient background
    gradient_image = create_gradient_background(window_width, window_height, (0, 102, 204), (255, 255, 255))
    gradient = ImageTk.PhotoImage(gradient_image)


    # Add a background label
    background_label = tk.Label(root, image=gradient)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add some padding to the main frame
    main_frame = tk.Frame(root, padx=20, pady=10)

    # Create a shadow frame
    shadow_frame = tk.Frame(root, padx=20, pady=10, background='#C0C0C0')

    # Add a title label with some styling
    title_label = ttk.Label(main_frame, text="Login", font=("Helvetica Neue", 24, "bold"))


    arrow_image = create_arrow_image((30, 30), (0, 102, 204))
    arrow = ImageTk.PhotoImage(arrow_image)
    arrow_label = ttk.Label(main_frame, image=arrow, background='')

    # Add labels for the username and password fields
    username_label = ttk.Label(main_frame, text="Username:", font=("Helvetica Neue", 16))
    password_label = ttk.Label(main_frame, text="Password:", font=("Helvetica Neue", 16))


    # Add entry fields for the username and password
    username_entry = ttk.Entry(main_frame, font=("Helvetica Neue", 16))
    password_entry = ttk.Entry(main_frame, show="*", font=("Helvetica Neue", 16))

    # Add a login button with some styling
    login_button = ttk.Button(main_frame, text="Login", command=login)

    # Create a custom ttk style
    style = ttk.Style()
    style.configure('TLabel', font=("Helvetica Neue", 16))
    style.configure('TEntry', font=("Helvetica Neue", 16))
    style.configure('TButton', font=("Helvetica Neue", 16, "bold"), background="black", foreground="black", padding=(10, 5))
    style.map('TButton', background=[('active', 'black')], foreground=[('active', 'black')])

    title_label.grid(row=0, column=1, pady=10)
    username_label.grid(row=1, column=0, pady=5)
    username_entry.grid(row=1, column=1, pady=5)
    password_label.grid(row=2, column=0, pady=5)
    password_entry.grid(row=2, column=1, pady=5)
    login_button.grid(row=3, column=1, pady=10)
    arrow_label.place(x=130, y=15)
    shadow_frame.place(relx=0.505, rely=0.505, anchor="center")


    # Center the main frame in the window
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()
if __name__ == "__main__":
    main()
import tkinter as tk
import math

def create_road(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="dark grey", outline="")

def create_dashed_yellow_line(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill="yellow", dash=(60, 20), width=6)

def create_traffic_light(canvas, x, y, clr, tag):
    canvas.create_oval(x, y, x + 30, y + 30, fill=clr, outline="", tags=tag)

def create_pedestrian_light(canvas, x, y, clr, tag):
    canvas.create_polygon(x, y, x - 10, y + 30, x + 10, y + 30, fill=clr, outline="", tags=tag)




def create_arrow(canvas, road, rotation):
    arrow_length = 100  # You can adjust the length of the arrow

    road_positions = {
        "left": (250, 450),
        "right": (550, 450),
        "top": (400, 300),
        "bottom": (400, 600),
    }



    x1, y1 = road_positions[road]

    if road == "left":
        if rotation == 90:
            x_mid, y_mid = x1 + arrow_length, y1
            x2, y2 = x_mid, y_mid - arrow_length
        elif rotation == 180:
            x_mid, y_mid = x1 + arrow_length + 40, y1
            x2, y2 = x_mid + arrow_length + 40, y_mid
        elif rotation == 270:
            x_mid, y_mid = x1 + arrow_length, y1
            x2, y2 = x_mid, y_mid + arrow_length
    elif road == "right":
        if rotation == 90:
            x_mid, y_mid = x1 - arrow_length, y1
            x2, y2 = x_mid, y_mid - arrow_length
        elif rotation == 180:
            x_mid, y_mid = x1 - arrow_length + 40, y1
            x2, y2 = x_mid - arrow_length + 40, y_mid
        elif rotation == 270:
            x_mid, y_mid = x1 - arrow_length, y1
            x2, y2 = x_mid, y_mid + arrow_length
    elif road == "top":
        if rotation == 90:
            x_mid, y_mid = x1, y1 + arrow_length
            x2, y2 = x_mid + arrow_length, y_mid
        elif rotation == 180:
            x_mid, y_mid = x1, y1 + arrow_length + 40
            x2, y2 = x_mid, y_mid + arrow_length + 40
        elif rotation == 270:
            x_mid, y_mid = x1, y1 + arrow_length
            x2, y2 = x_mid - arrow_length, y_mid
    elif road == "bottom":
        if rotation == 90:
            x_mid, y_mid = x1, y1 - arrow_length
            x2, y2 = x_mid + arrow_length, y_mid
        elif rotation == 180:
            x_mid, y_mid = x1, y1 - arrow_length + 40
            x2, y2 = x_mid, y_mid - arrow_length + 40
        elif rotation == 270:
            x_mid, y_mid = x1, y1 - arrow_length
            x2, y2 = x_mid - arrow_length, y_mid

    # Create the first arrow (horizontal)
    canvas.create_line(x1, y1, x_mid, y_mid, width=5, arrow=tk.LAST, arrowshape=(15, 20, 10))
    canvas.create_line(x_mid, y_mid, x2, y2, width=5, arrow=tk.LAST, arrowshape=(15, 20, 10))





   # if rotation == 90:
   #     canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)
   #     canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)
   # elif rotation == 180:
   #     canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)
   #     canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)
   # elif rotation == 270:
   #     canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)
   #     canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)


   # canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)

def display_pedestrian_count(canvas, x, y, count):
    canvas.create_text(x, y, text=f"Pedestrians: {count}", font=("Arial", 10), tags="ped_count_text")

def display_car_count(canvas, x, y, count):
    canvas.create_text(x, y, text=f"Cars: {count}", font=("Arial", 10), tags="car_count_text")    

def toggle_traffic_light(canvas, light):
    colors = ["red", "yellow", "green"]
    current_color = canvas.itemcget(light, "fill")
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    canvas.itemconfigure(light, fill=next_color)

def toggle_pedestrian_light(canvas, light):
    colors = ["red", "green"]
    current_color = canvas.itemcget(light, "fill")
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    canvas.itemconfigure(light, fill=next_color)

def create_admin_panel(window, canvas):
    admin_panel = tk.Frame(window)
    admin_panel.pack(side=tk.LEFT, padx=10)

def display_pedestrian_count(canvas, x, y, count, tag):
    canvas.create_text(x, y, text=f"Pedestrians: {count}", font=("Arial", 10), tags=tag)

def update_pedestrian_count(canvas, entry, x, y, tag):
    count = int(entry.get())
    canvas.delete(tag)
    display_pedestrian_count(canvas, x, y, count, tag)

def update_car_count(canvas, entry, x, y, tag):
    count = int(entry.get())
    canvas.delete(tag)
    display_car_count(canvas, x, y, count, tag)

def display_car_count(canvas, x, y, count, tag):
    canvas.create_text(x, y, text=f"Cars: {count}", font=("Arial", 10), tags=tag)

def create_legend(canvas):
    # Legend title
    canvas.create_text(50, 20, text="Legend", font=("Arial", 14, "bold"))

    # Traffic light
    canvas.create_oval(10, 40, 40, 70, fill="red", outline="")
    canvas.create_text(90, 55, text="Traffic Light ", font=("Arial", 10))

    # Pedestrian light
    canvas.create_polygon(20, 90, 10, 120, 30, 120, fill="green", outline="")
    canvas.create_text(90, 105, text="Pedestrian Light ", font=("Arial", 10))

    # Pedestrian Walk Direction
    canvas.create_line(20, 140, 40, 140, arrow=tk.BOTH, fill="black")
    canvas.create_text(120, 140, text="Pedestrian Walk Direction", font=("Arial", 10))

    # Vehicle Direction
    canvas.create_line(20, 170, 40, 170, arrow=tk.LAST, fill="black")
    canvas.create_text(90, 170, text="Vehicle Direction ", font=("Arial", 10))


def update_pedestrian_count(canvas, entry, x, y):
    count = int(entry.get())
    canvas.delete("ped_count_text")
    display_pedestrian_count(canvas, x, y, count)


def update_car_count(canvas, entry, x, y):
    count = int(entry.get())
    canvas.delete("car_count_text")
    display_car_count(canvas, x, y, count)


def update_traffic_light(canvas, x, y, clr):
    create_traffic_light(canvas, x, y, clr)


def update_pedestrian_light(canvas, x, y, clr):
    create_pedestrian_light(canvas, x, y, clr)


def create_admin_panel(window, canvas):
    admin_panel = tk.Frame(window, bg="white", width=300, height=500)
    admin_panel.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=1)

    tk.Label(admin_panel, text="Admin Panel", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

    # Change Pedestrian Count
    for i in range(1, 5):
        tk.Label(admin_panel, text=f"Pedestrians {i}:", font=("Arial", 10), bg="white").grid(row=i, column=0)
        pedestrian_entry = tk.Entry(admin_panel, width=5)
        pedestrian_entry.grid(row=i, column=1)
        pedestrian_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_pedestrian_count(canvas, pedestrian_entry, *pedestrian_count_positions[i-1], f"ped_count_text_{i}"))
        pedestrian_button.grid(row=i, column=2)

    tk.Label(admin_panel, text="Pedestrians:", font=("Arial", 10), bg="white").grid(row=1, column=0)
    pedestrian_entry = tk.Entry(admin_panel, width=5)
    pedestrian_entry.grid(row=1, column=1)
    pedestrian_button = tk.Button(admin_panel, text="Update", command=lambda: update_pedestrian_count(canvas, pedestrian_entry, 250, 290))
    pedestrian_button.grid(row=1, column=2)

    # Change Car Count
    for i in range(1, 5):
        tk.Label(admin_panel, text=f"Cars {i}:", font=("Arial", 10), bg="white").grid(row=i+4, column=0)
        car_entry = tk.Entry(admin_panel, width=5)
        car_entry.grid(row=i+4, column=1)
        car_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_car_count(canvas, car_entry, *car_count_positions[i-1], f"car_count_text_{i}"))
        car_button.grid(row=i+4, column=2)

    tk.Label(admin_panel, text="Cars:", font=("Arial", 10), bg="white").grid(row=2, column=0)
    car_entry = tk.Entry(admin_panel, width=5)
    car_entry.grid(row=2, column=1)
    car_button = tk.Button(admin_panel, text="Update", command=lambda: update_car_count(canvas, car_entry, 570, 290))
    car_button.grid(row=2, column=2)

    traffic_light_buttons = [
        tk.Button(admin_panel, text="Traffic Light 1", command=lambda: toggle_traffic_light(canvas, "traffic_light_1")),
        tk.Button(admin_panel, text="Traffic Light 2", command=lambda: toggle_traffic_light(canvas, "traffic_light_2")),
        tk.Button(admin_panel, text="Traffic Light 3", command=lambda: toggle_traffic_light(canvas, "traffic_light_3")),
        tk.Button(admin_panel, text="Traffic Light 4", command=lambda: toggle_traffic_light(canvas, "traffic_light_4")),
    ]

    pedestrian_light_buttons = [
        tk.Button(admin_panel, text="Pedestrian Light 1", command=lambda: toggle_pedestrian_light(canvas, "ped_light_1")),
        tk.Button(admin_panel, text="Pedestrian Light 2", command=lambda: toggle_pedestrian_light(canvas, "ped_light_2")),
        tk.Button(admin_panel, text="Pedestrian Light 3", command=lambda: toggle_pedestrian_light(canvas, "ped_light_3")),
        tk.Button(admin_panel, text="Pedestrian Light 4", command=lambda: toggle_pedestrian_light(canvas, "ped_light_4")),
        tk.Button(admin_panel, text="Pedestrian Light 5", command=lambda: toggle_pedestrian_light(canvas, "ped_light_5")),
        tk.Button(admin_panel, text="Pedestrian Light 6", command=lambda: toggle_pedestrian_light(canvas, "ped_light_6")),
        tk.Button(admin_panel, text="Pedestrian Light 7", command=lambda: toggle_pedestrian_light(canvas, "ped_light_7")),
        tk.Button(admin_panel, text="Pedestrian Light 8", command=lambda: toggle_pedestrian_light(canvas, "ped_light_8")),
    ]
    pedestrian_count_positions = [
    (250, 290),
    (570, 290),
    (250, 610),
    (570, 610)
    ]

    car_count_positions = [
    (50, 450),
    (750, 450),
    (400, 100),
    (400, 800)
    ]   

    for i, (x, y) in enumerate(pedestrian_count_positions, start=1):
        display_pedestrian_count(canvas, x, y, 0, f"ped_count_text_{i}")

    for i, (x, y) in enumerate(car_count_positions, start=1):
        display_car_count(canvas, x, y, 0, f"car_count_text_{i}")

    for i, button in enumerate(traffic_light_buttons, start=1):
        button.grid(row=3, column=i)

    for i, button in enumerate(pedestrian_light_buttons, start=1):
        button.grid(row=4, column=i)

   

def create_intersection():
    window = tk.Tk()
    window.title("Intersection")
    window.geometry("1920x1080")

    canvas = tk.Canvas(window, width=900, height=800)
    canvas.pack()

    # Roads
    create_road(canvas, 250, 50, 550, 850)   # Vertical road
    create_road(canvas, 0, 300, 800, 600)   # Horizontal road

    # Dashed yellow lines
    create_dashed_yellow_line(canvas, 400, 50, 400, 850)     # Top vertical line
    create_dashed_yellow_line(canvas, 0, 450, 800, 450)     # Left horizontal line

    # Traffic lights
    create_traffic_light(canvas, 385, 300, "red", "traffic_light_1")  # Top
    create_traffic_light(canvas, 250, 435, "red", "traffic_light_2")  # Left
    create_traffic_light(canvas, 385, 600, "red", "traffic_light_3")  # Bottom
    create_traffic_light(canvas, 550, 435, "red", "traffic_light_4")  # Right

# Pedestrian lights
    create_pedestrian_light(canvas, 550, 600, "green", "ped_light_1")  # Bottom Right
    create_pedestrian_light(canvas, 250, 300, "green", "ped_light_2")  # Top Left
    create_pedestrian_light(canvas, 250, 600, "green", "ped_light_3")  # Bottom Left
    create_pedestrian_light(canvas, 550, 300, "green", "ped_light_4")  # Top Right

    create_pedestrian_light(canvas, 550, 570, "green", "ped_light_5")  # Bottom Right 2
    create_pedestrian_light(canvas, 250, 270, "green", "ped_light_6")  # Top Left 2
    create_pedestrian_light(canvas, 250, 570, "green", "ped_light_7")  # Bottom Left 2
    create_pedestrian_light(canvas, 550, 270, "green", "ped_light_8")  # Top Right 2

    create_arrow(canvas, "top", 180)
    pedestrian_count = 0
    car_count = 0
 
    # Center the window on the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

    create_legend(canvas)
    create_admin_panel(window, canvas)

    window.mainloop()

if __name__ == "__main__":
    create_intersection()

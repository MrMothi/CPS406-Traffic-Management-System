import tkinter as tk

def create_road(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="dark grey", outline="")

def create_dashed_yellow_line(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill="yellow", dash=(60, 20), width=6)

def create_traffic_light(canvas, x, y, clr):
    canvas.create_oval(x, y, x + 30, y + 30, fill=clr, outline="")

def create_pedestrian_light(canvas, x, y, clr):
    canvas.create_polygon(x, y, x - 10, y + 30, x + 10, y + 30, fill=clr, outline="")


def create_arrow(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=3)


def display_pedestrian_count(canvas, x, y, count):
    canvas.create_text(x, y, text=f"Pedestrians: {count}", font=("Arial", 10))

def display_car_count(canvas, x, y, count):
    canvas.create_text(x, y, text=f"Cars: {count}", font=("Arial", 10))    

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
    create_traffic_light(canvas, 385, 300, "red")  # Top c
    create_traffic_light(canvas, 250, 435, "red")  # Left
    create_traffic_light(canvas, 385, 600, "red")  # Bottom
    create_traffic_light(canvas, 550, 435, "red")  # Right



    create_pedestrian_light(canvas, 550 , 600, "green")  # BOT R
    create_pedestrian_light(canvas, 250 , 300, "green")  # TOP L 
    create_pedestrian_light(canvas, 250 , 600, "green")  # BOT L
    create_pedestrian_light(canvas, 550 , 300, "green")  # TOP R

    pedestrian_count = 10
    car_count = 5

    display_pedestrian_count(canvas, 250, 290, pedestrian_count)
    display_car_count(canvas, 570, 290, car_count)

    create_arrow(canvas, 300, 300, 300, 300)     
                 
    create_arrow(canvas, 100, 450, 200, 450)

    # Center the window on the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

    create_legend(canvas)

    window.mainloop()

if __name__ == "__main__":
    create_intersection()

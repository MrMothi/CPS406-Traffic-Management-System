import tkinter as tk
from tkinter import scrolledtext
from tkinter.scrolledtext import *
from threading import Thread
from TrafficSystem import *
import AdminPanel
import TitleScreen
from tkinter import Tk, Button

#Global variable for the window object and canvas object
global window
global canvas


def create_road(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="dark grey", outline="")

def create_dashed_yellow_line(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill="yellow", dash=(60, 20), width=6)

def create_traffic_light(canvas, x, y, clr, tag):
    canvas.create_oval(x, y, x + 30, y + 30, fill=clr, outline="", tags=tag)

def create_pedestrian_light(canvas, x, y, clr, tag):
    canvas.create_polygon(x, y, x - 10, y + 30, x + 10, y + 30, fill=clr, outline="", tags=tag)



#arrow function for pedestrians
def create_double_sided_arrow(canvas, position, arr1, arr2, arrow_size=10, thickness=3):
    length = 200  # Set the fixed length here
    if position == "top":
        x, y = 300, 300
        orientation = "horizontal"
    elif position == "bottom":
        x, y = 300, 600
        orientation = "horizontal"
    elif position == "left":
        x, y = 270, 350
        orientation = "vertical"
    elif position == "right":
        x, y = 550, 350
        orientation = "vertical"
 
    if orientation == "horizontal":
        # Horizontal arrow
        canvas.create_line(x, y, x + length, y, arrow=tk.LAST, arrowshape=(arrow_size, arrow_size, arrow_size), width=thickness, tags=arr1)
        canvas.create_line(x + length, y, x, y, arrow=tk.LAST, arrowshape=(arrow_size, arrow_size, arrow_size), width=thickness, tags=arr2)
    elif orientation == "vertical":
        # Vertical arrow
        canvas.create_line(x, y, x, y + length, arrow=tk.LAST, arrowshape=(arrow_size, arrow_size, arrow_size), width=thickness, tags=arr1)
        canvas.create_line(x, y + length, x, y, arrow=tk.LAST, arrowshape=(arrow_size, arrow_size, arrow_size), width=thickness, tags=arr2)


#Arrow function for vehicles
def create_arrow(canvas, road, rotation, arr1, arr2):
    arrow_length = 100  # You can adjust the length of the arrow

    road_positions = {
        "left": (250, 550),     
        "right": (550, 350),
        "top": (300, 300),     #400
        "bottom": (500, 600),  #400 x
    }

    x1, y1 = road_positions[road]

    if road == "left":
        if rotation == 90:   
            x_mid, y_mid = x1 + arrow_length + 80, y1
            x2, y2 = x_mid, y_mid - arrow_length #-
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
            x_mid, y_mid = x1 - arrow_length - 40, y1  
            x2, y2 = x_mid - arrow_length - 40, y_mid   
        elif rotation == 270:
            x_mid, y_mid = x1 - arrow_length - 80, y1
            x2, y2 = x_mid, y_mid + arrow_length
    elif road == "top":
        if rotation == 90:
            x_mid, y_mid = x1, y1 + arrow_length + 80 #
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
            x_mid, y_mid = x1, y1 - arrow_length - 40
            x2, y2 = x_mid, y_mid - arrow_length - 40
        elif rotation == 270:
            x_mid, y_mid = x1, y1 - arrow_length - 80 #
            x2, y2 = x_mid - arrow_length, y_mid 

    # Create the first arrow (horizontal)
    canvas.create_line(x1, y1, x_mid, y_mid, width=5, arrow=tk.LAST, arrowshape=(15, 20, 10), tags=arr1)
    # Create the second arrow (vertical)
    canvas.create_line(x_mid, y_mid, x2, y2, width=5, arrow=tk.LAST, arrowshape=(15, 20, 10), tags=arr2)

    # # Return a tuple with the IDs of both arrows
    # return (arrow1_id, arrow2_id)


def delete_arrow(canvas, arrow_ids):
    for arrow_id in arrow_ids:
        canvas.delete(arrow_id)



def display_pedestrian_count(canvas, x, y, count):
    canvas.create_text(x, y, text=f"Pedestrians: {count}", font=("Arial", 10), tags="ped_count_text")

def display_car_count(canvas, x, y, count):
    canvas.create_text(x, y, text=f"Cars: {count}", font=("Arial", 10), tags="car_count_text")    

def toggle_traffic_light(canvas, light):
    colors = ["green", "yellow", "red"]
    current_color = canvas.itemcget(light, "fill")
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    if (light == "traffic_light_1" or light == "traffic_light_3"):
        TrafficSystem.inter.trafficLightObj[0].signalColour = next_color
    else:
        TrafficSystem.inter.trafficLightObj[1].signalColour = next_color
    canvas.itemconfigure(light, fill=next_color)

def toggle_pedestrian_light(canvas, light):
    colors = ["red", "green"]
    current_color = canvas.itemcget(light, "fill")
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    canvas.itemconfigure(light, fill=next_color)
    if(light == "ped_light_1"):
        TrafficSystem.inter.pedLightObj[0].signalColour = next_color
    else: #if "ped_light_2"
        TrafficSystem.inter.pedLightObj[1].signalColour = next_color

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



#FUNCTIONS FOR THE BUTTONS---------------------------------------------------

def switch_to_main_menu():
    window.destroy()
    TitleScreen.create_title_screen()


def closeProgram():
    #end all lights threads
    TrafficSystem.inter.notfinished = False
    #ending main inter.run thread
    TrafficSystem.inter.running = False
    #closing the window and program
    global window
    window.destroy()










def create_intersection():
    global window
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

    # Center the window on the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

    create_legend(canvas)

    verticalRoad = TrafficSystem.inter.trafficLightObj[0]
    horizontalRoad = TrafficSystem.inter.trafficLightObj[1]

    button = Button(window, text="Back to Main Menu", command=switch_to_main_menu)
    button.pack(side="left", padx=10, pady=10)

    button = Button(window, text="Close Program", command=closeProgram)
    button.pack(side="left", padx=10, pady=10)

    while True:
        
        #CREATING ARROWS FOR PEDESTRIAN OCC VARIABLES
        #OCC4
        if (TrafficSystem.inter.occ[3] > 0):   #for occ number 2 in diagram but index 1 in array
            create_double_sided_arrow(canvas, "left", "occ4ar1", "occ4ar2")
        #OCC8
        if (TrafficSystem.inter.occ[7] > 0): 
            create_double_sided_arrow(canvas, "top", "occ8ar1", "occ8ar2")
        #OCC12
        if (TrafficSystem.inter.occ[11] > 0):  
            create_double_sided_arrow(canvas, "right", "occ12ar1", "occ12ar2")
        #OCC16
        if (TrafficSystem.inter.occ[15] > 0):  
            create_double_sided_arrow(canvas, "bottom", "occ16ar1", "occ16ar2")


        #DELETING ARROWS FOR PEDESTRIANS IF NEED BE
        #OCC4
        if(TrafficSystem.inter.occ[3] <= 0):
            # delete_arrow(canvas, ("occ1ar3", "occ1ar2"))
            canvas.delete("occ4ar1")
            canvas.delete("occ4ar2")
        #OCC8
        if(TrafficSystem.inter.occ[7] <= 0):
            canvas.delete("occ8ar1")
            canvas.delete("occ8ar2")
        #OCC12
        if(TrafficSystem.inter.occ[11] <= 0):
            canvas.delete("occ12ar1")
            canvas.delete("occ12ar2")
        #OCC16
        if(TrafficSystem.inter.occ[15] <= 0):
            canvas.delete("occ16ar1")
            canvas.delete("occ16ar2")




        #CREATING ARROWS FOR VEHICLE OCC VARIABLES
        #OCC1
        if (TrafficSystem.inter.occ[0] > 0):   #for occ number 2 in diagram but index 1 in array
            create_arrow(canvas, "top", 270, "occ1ar1", "occ1ar2")
        #OCC2
        if (TrafficSystem.inter.occ[1] > 0): 
            create_arrow(canvas, "top", 180, "occ2ar1", "occ2ar2")
        #OCC3
        if (TrafficSystem.inter.occ[2] > 0):  
            create_arrow(canvas, "top", 90, "occ3ar1", "occ3ar2")

        #OCC9
        if (TrafficSystem.inter.occ[8] > 0):   #for occ number 2 in diagram but index 1 in array
            create_arrow(canvas, "bottom", 90, "occ9ar1", "occ9ar2")
        #OCC10
        if (TrafficSystem.inter.occ[9] > 0): 
            create_arrow(canvas, "bottom", 180, "occ10ar1", "occ10ar2")
        #OCC11
        if (TrafficSystem.inter.occ[10] > 0):  
            create_arrow(canvas, "bottom", 270, "occ11ar1", "occ11ar2")



        #OCC5
        if (TrafficSystem.inter.occ[4] > 0):   #for occ number 2 in diagram but index 1 in array
            create_arrow(canvas, "right", 90, "occ5ar1", "occ5ar2")
        #OCC6
        if (TrafficSystem.inter.occ[5] > 0): 
            create_arrow(canvas, "right", 180, "occ6ar1", "occ6ar2")
        #OCC7
        if (TrafficSystem.inter.occ[6] > 0):  
            create_arrow(canvas, "right", 270, "occ7ar1", "occ7ar2")

        #OCC13
        if (TrafficSystem.inter.occ[12] > 0):   #for occ number 2 in diagram but index 1 in array
            create_arrow(canvas, "left", 270, "occ13ar1", "occ13ar2")
        #OCC14
        if (TrafficSystem.inter.occ[13] > 0): 
            create_arrow(canvas, "left", 180, "occ14ar1", "occ14ar2")
        #OCC15
        if (TrafficSystem.inter.occ[14] > 0):  
            create_arrow(canvas, "left", 90, "occ15ar1", "occ15ar2")






        #DELETING VEHICLE ARROWS IF NEED BE
        if(TrafficSystem.inter.occ[0] <= 0):
            # delete_arrow(canvas, ("occ1ar1", "occ1ar2"))
            canvas.delete("occ1ar1")
            canvas.delete("occ1ar2")
        if(TrafficSystem.inter.occ[1] <= 0):
            canvas.delete("occ2ar1")
            canvas.delete("occ2ar2")
        if(TrafficSystem.inter.occ[2] <= 0):
            canvas.delete("occ3ar1")
            canvas.delete("occ3ar2")


        if(TrafficSystem.inter.occ[8] <= 0):
            # delete_arrow(canvas, ("occ1ar1", "occ1ar2"))
            canvas.delete("occ9ar1")
            canvas.delete("occ9ar2")
        if(TrafficSystem.inter.occ[9] <= 0):
            canvas.delete("occ10ar1")
            canvas.delete("occ10ar2")
        if(TrafficSystem.inter.occ[10] <= 0):
            canvas.delete("occ11ar1")
            canvas.delete("occ11ar2")


        if(TrafficSystem.inter.occ[4] <= 0):
            # delete_arrow(canvas, ("occ1ar1", "occ1ar2"))
            canvas.delete("occ5ar1")
            canvas.delete("occ5ar2")
        if(TrafficSystem.inter.occ[5] <= 0):
            canvas.delete("occ6ar1")
            canvas.delete("occ6ar2")
        if(TrafficSystem.inter.occ[6] <= 0):
            canvas.delete("occ7ar1")
            canvas.delete("occ7ar2")


        if(TrafficSystem.inter.occ[12] <= 0):
            # delete_arrow(canvas, ("occ1ar1", "occ1ar2"))
            canvas.delete("occ13ar1")
            canvas.delete("occ13ar2")
        if(TrafficSystem.inter.occ[13] <= 0):
            canvas.delete("occ14ar1")
            canvas.delete("occ14ar2")
        if(TrafficSystem.inter.occ[14] <= 0):
            canvas.delete("occ15ar1")
            canvas.delete("occ15ar2")



        #Deleting traffic and pedestrian lights
        canvas.delete("traffic_light_1")
        canvas.delete("traffic_light_2")
        canvas.delete("traffic_light_4")
        canvas.delete("traffic_light_5")
        canvas.delete("ped_light_1")
        canvas.delete("ped_light_2")
        canvas.delete("ped_light_3")
        canvas.delete("ped_light_4")
        canvas.delete("ped_light_5")
        canvas.delete("ped_light_6")
        canvas.delete("ped_light_7")
        canvas.delete("ped_light_8")


        # Traffic lights    
        create_traffic_light(canvas, 385, 300, verticalRoad.signalColour, "traffic_light_1")  # Top
        create_traffic_light(canvas, 240, 435, horizontalRoad.signalColour, "traffic_light_2")  # Left
        create_traffic_light(canvas, 385, 600, verticalRoad.signalColour, "traffic_light_3")  # Bottom
        create_traffic_light(canvas, 540, 435, horizontalRoad.signalColour, "traffic_light_4")  # Right


        # Pedestrian lights
        create_pedestrian_light(canvas, 550, 615, TrafficSystem.inter.pedLightObj[0].signalColour, "ped_light_1")  # Bottom Right
        create_pedestrian_light(canvas, 235, 300, TrafficSystem.inter.pedLightObj[1].signalColour, "ped_light_2")  # Top Left
        create_pedestrian_light(canvas, 250, 615, TrafficSystem.inter.pedLightObj[0].signalColour, "ped_light_3")  # Bottom Left
        create_pedestrian_light(canvas, 565, 300, TrafficSystem.inter.pedLightObj[1].signalColour, "ped_light_4")  # Top Right

        create_pedestrian_light(canvas, 565, 570, TrafficSystem.inter.pedLightObj[1].signalColour, "ped_light_5")  # Bottom Right 2
        create_pedestrian_light(canvas, 250, 255, TrafficSystem.inter.pedLightObj[0].signalColour, "ped_light_6")  # Top Left 2
        create_pedestrian_light(canvas, 235, 570, TrafficSystem.inter.pedLightObj[1].signalColour, "ped_light_7")  # Bottom Left 2
        create_pedestrian_light(canvas, 550, 255, TrafficSystem.inter.pedLightObj[0].signalColour, "ped_light_8")  # Top Right 2


        pedestrian_count = 0
        car_count = 0
        

        #DISPLAYING AND UPDATING CAR COUNTS
        canvas.delete("C4")
        canvas.delete("C2")
        canvas.delete("C1")
        canvas.delete("C3")
        display_car_count(canvas, 50, 550, len(TrafficSystem.inter.roadsObj[1].vehiclesInLane2), "C4")
        display_car_count(canvas, 750, 350, len(TrafficSystem.inter.roadsObj[1].vehiclesInLane1), "C2")
        display_car_count(canvas, 325, 100, len(TrafficSystem.inter.roadsObj[0].vehiclesInLane1), "C1")
        display_car_count(canvas, 475, 780, len(TrafficSystem.inter.roadsObj[0].vehiclesInLane2), "C3")

        #DISPLAYING AND UPDATING PEDESTRIAN COUNTS
        canvas.delete("PTL")  #pedestrianTopLeft
        canvas.delete("PTR")
        canvas.delete("PBL")  #pedestrianBottomLeft
        canvas.delete("PBR")
        display_pedestrian_count(canvas, 250, 290, (len(TrafficSystem.inter.sidewalksObj[0].sidewalk1) + len(TrafficSystem.inter.sidewalksObj[3].sidewalk2)), "PTL") #adds sidewalkobj1 arr1 with sidewalkobj4 arr2
        display_pedestrian_count(canvas, 570, 290, (len(TrafficSystem.inter.sidewalksObj[1].sidewalk1) + len(TrafficSystem.inter.sidewalksObj[0].sidewalk2)), "PTR") #adds sidewalkobj1 arr2 with sidewalkobj2 arr1
        display_pedestrian_count(canvas, 250, 610, (len(TrafficSystem.inter.sidewalksObj[3].sidewalk1) + len(TrafficSystem.inter.sidewalksObj[2].sidewalk2)), "PBL") #adds sidewalkobj3 arr2 with sidewalkobj4 arr1
        display_pedestrian_count(canvas, 570, 610, (len(TrafficSystem.inter.sidewalksObj[2].sidewalk1) + len(TrafficSystem.inter.sidewalksObj[1].sidewalk2)), "PBR") #adds sidewalkonj3 arr1 with sidewalkobj2 arr2





        #Updating

    # pedestrian_count_positions = [
    # (250, 290), tlef
    # (570, 290), trigh
    # (250, 610), bleft
    # (570, 610)  brigh
    # ]


    
    # def display_pedestrian_count(canvas, x, y, count):
    # canvas.create_text(x, y, text=f"Pedestrians: {count}", font=("Arial", 10), tags="ped_count_text")

        # create_arrow("left", 90)
        # create_arrow(canvas, "right", 180)    
        # create_arrow(canvas, "bottom", 90)      
                    
        # create_arrow(canvas, 100, 450, 200, 450)

        window.update()

# def create_intersection():
#     pass

if __name__ == "__main__":
    create_intersection()




# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk, ImageDraw
# import UIMain

# def main():
#     def login(root):
#         username = username_entry.get()
#         password = password_entry.get()
#         print("Username:", username)
#         print("Password:", password)
#         UIMain.main()

#     # Create a logo
#     def create_arrow_image(size, fill_color):
#         img = Image.new('RGBA', size, color=(255, 255, 255, 0))
#         draw = ImageDraw.Draw(img)

#         # Draw logo
#         draw.polygon([(0, size[1] / 2), (size[0] / 2, 0), (size[0], size[1] / 2), (size[0] / 2, size[1])], fill=fill_color)

#         return img

#     # Create background
#     def create_gradient_background(width, height, start_color, end_color):
#         gradient = Image.new('RGBA', (width, height), color=0)
#         draw = ImageDraw.Draw(gradient)

#         for i in range(height):
#             c = [round((end_color[j] - start_color[j]) * i / height + start_color[j]) for j in range(3)]
#             draw.line([(0, i), (width, i)], fill=tuple(c))

#         return gradient

#     def on_resize(event):
#         width = event.width
#         height = event.height
#         gradient_image = create_gradient_background(width, height, (0, 102, 204), (255, 255, 255))
#         gradient = ImageTk.PhotoImage(gradient_image)
#         background_label.config(image=gradient)
#         background_label.image = gradient

#     root = tk.Tk()
#     root.title("Login")
#     root.bind("<Configure>", on_resize)

#     # Set size
#     window_width = 800
#     window_height = 600
#     root.geometry(f"{window_width}x{window_height}")

#     # Calculate the center of the window
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     x_coordinate = int((screen_width/2) - (window_width/2))
#     y_coordinate = int((screen_height/2) - (window_height/2))

#     # Set the window position to the center of the screen
#     root.geometry(f"+{x_coordinate}+{y_coordinate}")

#     # Create a gradient background
#     gradient_image = create_gradient_background(window_width, window_height, (0, 102, 204), (255, 255, 255))
#     gradient = ImageTk.PhotoImage(gradient_image)


#     # Add a background label
#     background_label = tk.Label(root, image=gradient)
#     background_label.place(x=0, y=0, relwidth=1, relheight=1)

#     # Add some padding to the main frame
#     main_frame = tk.Frame(root, padx=20, pady=10)

#     # Create a shadow frame
#     shadow_frame = tk.Frame(root, padx=20, pady=10, background='#C0C0C0')

#     # Add a title label with some styling
#     title_label = ttk.Label(main_frame, text="Login", font=("Helvetica Neue", 24, "bold"))


#     arrow_image = create_arrow_image((30, 30), (0, 102, 204))
#     arrow = ImageTk.PhotoImage(arrow_image)
#     arrow_label = ttk.Label(main_frame, image=arrow, background='')

#     # Add labels for the username and password fields
#     username_label = ttk.Label(main_frame, text="Username:", font=("Helvetica Neue", 16))
#     password_label = ttk.Label(main_frame, text="Password:", font=("Helvetica Neue", 16))


#     # Add entry fields for the username and password
#     username_entry = ttk.Entry(main_frame, font=("Helvetica Neue", 16))
#     password_entry = ttk.Entry(main_frame, show="*", font=("Helvetica Neue", 16))

#     # Add a login button with some styling
#     login_button = ttk.Button(main_frame, text="Login", command=lambda:login(root))

#     # Create a custom ttk style
#     style = ttk.Style()
#     style.configure('TLabel', font=("Helvetica Neue", 16))
#     style.configure('TEntry', font=("Helvetica Neue", 16))
#     style.configure('TButton', font=("Helvetica Neue", 16, "bold"), background="black", foreground="black", padding=(10, 5))
#     style.map('TButton', background=[('active', 'black')], foreground=[('active', 'black')])

#     title_label.grid(row=0, column=1, pady=10)
#     username_label.grid(row=1, column=0, pady=5)
#     username_entry.grid(row=1, column=1, pady=5)
#     password_label.grid(row=2, column=0, pady=5)
#     password_entry.grid(row=2, column=1, pady=5)
#     login_button.grid(row=3, column=1, pady=10)
#     arrow_label.place(x=130, y=15)
#     shadow_frame.place(relx=0.505, rely=0.505, anchor="center")


#     # Center the main frame in the window
#     main_frame.place(relx=0.5, rely=0.5, anchor="center")

#     root.mainloop()
# if __name__ == "__main__":
#     main()
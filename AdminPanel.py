import tkinter as tk
from tkinter import scrolledtext
from tkinter.scrolledtext import *
from threading import Thread
from TrafficSystem import *

#Creating the thread variable for the run function of intersection
TrafficSystem.initializeIntersection()
#Global variable for log object
global log
#Variables for main loop threads
global indTraffic
global interloop
interloop = []
interloop.append(threading.Thread(target=TrafficSystem.inter.run))
indTraffic = 0

#Creating signal light threads
TrafficSystem.inter.createTrafficLightThreads()
TrafficSystem.inter.createPedestrianLightThreads()



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

#---------FUNCTIONS FOR THE BUTTONS------------------------------------------------------------------------
def toggleTraffic():
    global indTraffic
    if(interloop[indTraffic].is_alive()):
        TrafficSystem.inter.running = False
        indTraffic = indTraffic + 1
        interloop.append(threading.Thread(target=TrafficSystem.inter.run))
        log_message(log, "Stopped Traffic")
    else:     
        TrafficSystem.inter.running = True
        interloop[indTraffic].start()
        log_message(log, "Started Traffic")

def toggleTrafficLight():
    if(TrafficSystem.inter.trafficLightObj[0].operational):
        TrafficSystem.inter.trafficLightObj[0].operational = False
        TrafficSystem.inter.trafficLightObj[1].operational = False
        log_message(log, "Stopped TrafficLight Cycling")
        log_message(log, "--Will Finish Current Colour Change--")
    else:
        TrafficSystem.inter.trafficLightObj[0].operational = True
        TrafficSystem.inter.trafficLightObj[1].operational = True
        log_message(log, "Started TrafficLight Cycling")
        log_message(log, "--May Be Out Of Sync--")

def togglePedestrianLight():
    if(TrafficSystem.inter.pedLightObj[0].operational):
        TrafficSystem.inter.pedLightObj[0].operational = False
        TrafficSystem.inter.pedLightObj[1].operational = False
        log_message(log, "Stopped PedestrianLight Cycling")
        log_message(log, "--Will Finish Current Colour Change--")
    else:
        TrafficSystem.inter.pedLightObj[0].operational = True
        TrafficSystem.inter.pedLightObj[1].operational = True
        log_message(log, "Started PedestrianLight Cycling")
        log_message(log, "--May Be Out Of Sync--")

def toggleAutoVeh():
    if(TrafficSystem.inter.autoVehicles):
        TrafficSystem.inter.autoVehicles = False
        log_message(log, "Stopped Auto Vehicles")
    else:
        TrafficSystem.inter.autoVehicles = True
        log_message(log, "Started Auto Vehicles")

def toggleAutoPed():
    if(TrafficSystem.inter.autoPedestrians):
        TrafficSystem.inter.autoPedestrians = False
        log_message(log, "Stopped Auto Pedestrians")
    else:
        TrafficSystem.inter.autoPedestrians = True
        log_message(log, "Started Auto Pedestrians")




# def create_admin_panel(window, canvas):
#     admin_panel = tk.Frame(window, bg="", width=300)
#     admin_panel.place(x=0, y=0, relheight=1)

#     tk.Label(admin_panel, text="Admin Panel", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, columnspan=4, pady=10)

#     #TOGGLING TRAFFIC, TRAFFIC LIGHTS, AND PEDESTRIAN LIGHTS  #---------------------------------------------------------
#     toggleTraffic_button = tk.Button(admin_panel, text="Toggle Traffic", command=lambda: toggleTraffic())  
#     toggleTraffic_button.grid(row=1, column=1)

#     toggleTrafficLight_button = tk.Button(admin_panel, text="Toggle TrafficLight", command=lambda: toggleTrafficLight()) 
#     toggleTrafficLight_button.grid(row=1, column=2)

#     togglePedestrianLight_button = tk.Button(admin_panel, text="Toggle PedestrianLight", command=lambda: togglePedestrianLight()) 
#     togglePedestrianLight_button.grid(row=2, column=1)




#     pedestrian_count_positions = [
#         (250, 290),
#         (570, 290),
#         (250, 610),
#         (570, 610)
#     ]

#     car_count_positions = [
#         (50, 450),
#         (750, 450),
#         (400, 100),
#         (400, 800)
#     ]

#     # Change Pedestrian Count
#     for i in range(3, 7):
#         tk.Label(admin_panel, text=f"Pedestrians {i}:", font=("Arial", 10), bg="white").grid(row=i, column=0)
#         pedestrian_entry = tk.Entry(admin_panel, width=5)
#         pedestrian_entry.grid(row=i, column=1)
#         pedestrian_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_pedestrian_count(canvas, pedestrian_entry, *pedestrian_count_positions[i-1], f"ped_count_text_{i}"))
#         pedestrian_button.grid(row=i, column=2)

#     # Change Car Count
#     for i in range(3, 7):
#         tk.Label(admin_panel, text=f"Cars {i}:", font=("Arial", 10), bg="white").grid(row=i+4, column=0)
#         car_entry = tk.Entry(admin_panel, width=5)
#         car_entry.grid(row=i+4, column=1)
#         car_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_car_count(canvas, car_entry, *car_count_positions[i-1], f"car_count_text_{i}"))
#         car_button.grid(row=i+4, column=2)

#     traffic_light_buttons = [
#         tk.Button(admin_panel, text="Traffic Light 1", command=lambda: (toggle_traffic_light(canvas, "traffic_light_1"), create_pop_text(canvas, "light_1"))),
#         tk.Button(admin_panel, text="Traffic Light 2", command=lambda: (toggle_traffic_light(canvas, "traffic_light_2"), create_pop_text(canvas, "light_2"))),
#         tk.Button(admin_panel, text="Traffic Light 3", command=lambda: (toggle_traffic_light(canvas, "traffic_light_3"), create_pop_text(canvas, "light_3"))),
#         tk.Button(admin_panel, text="Traffic Light 4", command=lambda: (toggle_traffic_light(canvas, "traffic_light_4"), create_pop_text(canvas, "light_4"))),
#     ]

#         # Pedestrian Light Buttons
#     pedestrian_light_buttons = [
#         tk.Button(admin_panel, text="Pedestrian Light 1", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_1"), create_pop_text(canvas, "ped_light_1"))),
#         tk.Button(admin_panel, text="Pedestrian Light 2", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_2"), create_pop_text(canvas, "ped_light_2"))),
#         tk.Button(admin_panel, text="Pedestrian Light 3", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_3"), create_pop_text(canvas, "ped_light_3"))),
#         tk.Button(admin_panel, text="Pedestrian Light 4", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_4"), create_pop_text(canvas, "ped_light_4"))),
#         tk.Button(admin_panel, text="Pedestrian Light 5", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_5"), create_pop_text(canvas, "ped_light_5"))),
#         tk.Button(admin_panel, text="Pedestrian Light 6", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_6"), create_pop_text(canvas, "ped_light_6"))),
#         tk.Button(admin_panel, text="Pedestrian Light 7", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_7"), create_pop_text(canvas, "ped_light_7"))),
#         tk.Button(admin_panel, text="Pedestrian Light 8", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_8"), create_pop_text(canvas, "ped_light_8"))),
#     ]

#     for i, (x, y) in enumerate(pedestrian_count_positions, start=1):
#         display_pedestrian_count(canvas, x, y, 0, f"ped_count_text_{i}")

#     for i, (x, y) in enumerate(car_count_positions, start=1):
#         display_car_count(canvas, x, y, 0, f"car_count_text_{i}")

#     # # Pedestrian Light Buttons
#     # for i, button in enumerate(traffic_light_buttons, start=1):
#     #     if i <= 2:
#     #         button.grid(row=i + 9, column=0, pady=2, sticky=tk.W)
#     #     else:
#     #         button.grid(row=i + 7, column=2, pady=2, sticky=tk.W)

#     # # Traffic Light Buttons
#     # for i, button in enumerate(pedestrian_light_buttons, start=1):
#     #     if i <= 4:
#     #         button.grid(row=i + 16, column=0, pady=2, sticky=tk.W)
#     #     else:
#     #         button.grid(row=i + 12, column=2, pady=2, sticky=tk.W)







# def create_admin_panel(window, canvas):
#     admin_panel = tk.Frame(window, bg="", width=300)
#     admin_panel.place(x=0, y=0, relheight=1)

#     tk.Label(admin_panel, text="Admin Panel", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, columnspan=4, pady=10)

#     #TOGGLING TRAFFIC, TRAFFIC LIGHTS, AND PEDESTRIAN LIGHTS  #---------------------------------------------------------
#     toggleTraffic_button = tk.Button(admin_panel, text="Toggle Traffic", command=lambda: toggleTraffic())  
#     toggleTraffic_button.grid(row=1, column=1)

#     toggleTrafficLight_button = tk.Button(admin_panel, text="Toggle TrafficLight", command=lambda: toggleTrafficLight()) 
#     toggleTrafficLight_button.grid(row=1, column=2)

#     togglePedestrianLight_button = tk.Button(admin_panel, text="Toggle PedestrianLight", command=lambda: togglePedestrianLight()) 
#     togglePedestrianLight_button.grid(row=2, column=1)




#     pedestrian_count_positions = [
#         (250, 290),
#         (570, 290),
#         (250, 610),
#         (570, 610)
#     ]

#     car_count_positions = [
#         (50, 450),
#         (750, 450),
#         (400, 100),
#         (400, 800)
#     ]

#     # Change Pedestrian Count
#     for i in range(3, 7):
#         tk.Label(admin_panel, text=f"Pedestrians {i}:", font=("Arial", 10), bg="white").grid(row=i, column=0)
#         pedestrian_entry = tk.Entry(admin_panel, width=5)
#         pedestrian_entry.grid(row=i, column=1)
#         pedestrian_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_pedestrian_count(canvas, pedestrian_entry, *pedestrian_count_positions[i-1], f"ped_count_text_{i}"))
#         pedestrian_button.grid(row=i, column=2)

#     # Change Car Count
#     for i in range(3, 7):
#         tk.Label(admin_panel, text=f"Cars {i}:", font=("Arial", 10), bg="white").grid(row=i+4, column=0)
#         car_entry = tk.Entry(admin_panel, width=5)
#         car_entry.grid(row=i+4, column=1)
#         car_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_car_count(canvas, car_entry, *car_count_positions[i-1], f"car_count_text_{i}"))
#         car_button.grid(row=i+4, column=2)

#     traffic_light_buttons = [
#         tk.Button(admin_panel, text="Traffic Light 1", command=lambda: (toggle_traffic_light(canvas, "traffic_light_1"), create_pop_text(canvas, "light_1"))),
#         tk.Button(admin_panel, text="Traffic Light 2", command=lambda: (toggle_traffic_light(canvas, "traffic_light_2"), create_pop_text(canvas, "light_2"))),
#         tk.Button(admin_panel, text="Traffic Light 3", command=lambda: (toggle_traffic_light(canvas, "traffic_light_3"), create_pop_text(canvas, "light_3"))),
#         tk.Button(admin_panel, text="Traffic Light 4", command=lambda: (toggle_traffic_light(canvas, "traffic_light_4"), create_pop_text(canvas, "light_4"))),
#     ]

#         # Pedestrian Light Buttons
#     pedestrian_light_buttons = [
#         tk.Button(admin_panel, text="Pedestrian Light 1", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_1"), create_pop_text(canvas, "ped_light_1"))),
#         tk.Button(admin_panel, text="Pedestrian Light 2", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_2"), create_pop_text(canvas, "ped_light_2"))),
#         tk.Button(admin_panel, text="Pedestrian Light 3", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_3"), create_pop_text(canvas, "ped_light_3"))),
#         tk.Button(admin_panel, text="Pedestrian Light 4", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_4"), create_pop_text(canvas, "ped_light_4"))),
#         tk.Button(admin_panel, text="Pedestrian Light 5", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_5"), create_pop_text(canvas, "ped_light_5"))),
#         tk.Button(admin_panel, text="Pedestrian Light 6", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_6"), create_pop_text(canvas, "ped_light_6"))),
#         tk.Button(admin_panel, text="Pedestrian Light 7", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_7"), create_pop_text(canvas, "ped_light_7"))),
#         tk.Button(admin_panel, text="Pedestrian Light 8", command=lambda: (toggle_pedestrian_light(canvas, "ped_light_8"), create_pop_text(canvas, "ped_light_8"))),
#     ]

#     for i, (x, y) in enumerate(pedestrian_count_positions, start=1):
#         display_pedestrian_count(canvas, x, y, 0, f"ped_count_text_{i}")

#     for i, (x, y) in enumerate(car_count_positions, start=1):
#         display_car_count(canvas, x, y, 0, f"car_count_text_{i}")

#     # # Pedestrian Light Buttons
#     # for i, button in enumerate(traffic_light_buttons, start=1):
#     #     if i <= 2:
#     #         button.grid(row=i + 9, column=0, pady=2, sticky=tk.W)
#     #     else:
#     #         button.grid(row=i + 7, column=2, pady=2, sticky=tk.W)

#     # # Traffic Light Buttons
#     # for i, button in enumerate(pedestrian_light_buttons, start=1):
#     #     if i <= 4:
#     #         button.grid(row=i + 16, column=0, pady=2, sticky=tk.W)
#     #     else:
#     #         button.grid(row=i + 12, column=2, pady=2, sticky=tk.W)





def create_admin_panel(window, canvas):

    admin_panel = tk.Frame(window, bg="white", width=300)
    admin_panel.place(x=0, y=0, relheight=1)

    tk.Label(admin_panel, text="Admin Panel", font=("Arial", 16, "bold"), bg="white").grid(row=0, column=0, columnspan=4, pady=10)


    # admin_panel = tk.Frame(window, bg="white", width=300, height=500)
    # admin_panel.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=1)

    # tk.Label(admin_panel, text="Admin Panel", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

    # # Change Pedestrian Count
    # for i in range(1, 5):
    #     tk.Label(admin_panel, text=f"Pedestrians {i}:", font=("Arial", 10), bg="white").grid(row=i, column=0)
    #     pedestrian_entry = tk.Entry(admin_panel, width=5)
    #     pedestrian_entry.grid(row=i, column=1)
    #     pedestrian_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_pedestrian_count(canvas, pedestrian_entry, *pedestrian_count_positions[i-1], f"ped_count_text_{i}"))
    #     pedestrian_button.grid(row=i, column=2)

    # tk.Label(admin_panel, text="Pedestrians:", font=("Arial", 10), bg="white").grid(row=1, column=0)
    # pedestrian_entry = tk.Entry(admin_panel, width=5)
    # pedestrian_entry.grid(row=1, column=1)
    # pedestrian_button = tk.Button(admin_panel, text="Update", command=lambda: update_pedestrian_count(canvas, pedestrian_entry, 250, 290))
    # pedestrian_button.grid(row=1, column=2)

    # # Change Car Count
    # for i in range(1, 5):
    #     tk.Label(admin_panel, text=f"Cars {i}:", font=("Arial", 10), bg="white").grid(row=i+4, column=0)
    #     car_entry = tk.Entry(admin_panel, width=5)
    #     car_entry.grid(row=i+4, column=1)
    #     car_button = tk.Button(admin_panel, text="Update", command=lambda i=i: update_car_count(canvas, car_entry, *car_count_positions[i-1], f"car_count_text_{i}"))
    #     car_button.grid(row=i+4, column=2)

    # tk.Label(admin_panel, text="Cars:", font=("Arial", 10), bg="white").grid(row=2, column=0)
    # car_entry = tk.Entry(admin_panel, width=5)
    # car_entry.grid(row=2, column=1)
    # car_button = tk.Button(admin_panel, text="Update", command=lambda: update_car_count(canvas, car_entry, 570, 290))
    # car_button.grid(row=2, column=2)



    #TOGGLING TRAFFIC, TRAFFIC LIGHTS, AND PEDESTRIAN LIGHTS  #---------------------------------------------------------
    tk.Label(admin_panel, text=f"Toggle Loop Buttons", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0)
    toggleTraffic_button = tk.Button(admin_panel, text="Toggle Traffic", command=lambda: toggleTraffic(), width=23)  
    toggleTraffic_button.grid(row=2, column=0)

    toggleTrafficLight_button = tk.Button(admin_panel, text="Toggle TrafficLights", command=lambda: toggleTrafficLight(), width=23) 
    toggleTrafficLight_button.grid(row=2, column=1)

    togglePedestrianLight_button = tk.Button(admin_panel, text="Toggle PedestrianLights", command=lambda: togglePedestrianLight(), width=23) 
    togglePedestrianLight_button.grid(row=2, column=2)




    #Buttons for adding vechicles #------------------------------------------------------------------------------------------------
    tk.Label(admin_panel, text=f"Add Vehicle Buttons", font=("Arial", 10, "bold"), bg="white").grid(row=3, column=0)
    #Vehicle top, turning left
    addVehicleC1_1button = tk.Button(admin_panel, width=23, text="Vehicle Top, Left Turn", command=lambda: [TrafficSystem.inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[0], 1, 1)), log_message(log, "Added Vehicle at Top Turning Left")] ) 
    addVehicleC1_1button.grid(row=4, column=0)
    #Vehicle top, going straight
    addVehicleC1_2button = tk.Button(admin_panel, width=23, text="Vehicle Top, Straight", command=lambda: [TrafficSystem.inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[0], 2, 1)), log_message(log, "Added Vehicle at Top Going Straight")] ) 
    addVehicleC1_2button.grid(row=4, column=1)
    #Vehicle top, turning right
    addVehicleC1_3button = tk.Button(admin_panel, width=23, text="Vehicle Top, Right Turn", command=lambda: [TrafficSystem.inter.roadsObj[0].vehiclesInLane1.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[0], 3, 1)), log_message(log, "Added Vehicle at Top Turning Right")] ) 
    addVehicleC1_3button.grid(row=4, column=2)

    #Vehicle right, turning left
    addVehicleC2_1button = tk.Button(admin_panel, width=23, text="Vehicle Right, Left Turn", command=lambda: [TrafficSystem.inter.roadsObj[1].vehiclesInLane1.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[1], 1, 2)), log_message(log, "Added Vehicle at Right Turning Left")] ) 
    addVehicleC2_1button.grid(row=5, column=0)
    #Vehicle right, going straight
    addVehicleC2_2button = tk.Button(admin_panel, width=23, text="Vehicle Right, Straight", command=lambda: [TrafficSystem.inter.roadsObj[1].vehiclesInLane1.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[1], 2, 2)), log_message(log, "Added Vehicle at Right Going Straight")] ) 
    addVehicleC2_2button.grid(row=5, column=1)
    #Vehicle right, turning right
    addVehicleC2_3button = tk.Button(admin_panel, width=23, text="Vehicle Right, Right Turn", command=lambda: [TrafficSystem.inter.roadsObj[1].vehiclesInLane1.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[1], 3, 2)), log_message(log, "Added Vehicle at Right Turning Right")] ) 
    addVehicleC2_3button.grid(row=5, column=2)

    #Vehicle bottom, turning left
    addVehicleC3_1button = tk.Button(admin_panel, width=23, text="Vehicle Bottom, Left Turn", command=lambda: [TrafficSystem.inter.roadsObj[0].vehiclesInLane2.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[0], 1, 3)), log_message(log, "Added Vehicle at Bottom Turning Left")] ) 
    addVehicleC3_1button.grid(row=6, column=0)
    #Vehicle bottom, going straight
    addVehicleC3_2button = tk.Button(admin_panel, width=23, text="Vehicle Bottom, Straight", command=lambda: [TrafficSystem.inter.roadsObj[0].vehiclesInLane2.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[0], 2, 3)), log_message(log, "Added Vehicle at Bottom Going Straight")] ) 
    addVehicleC3_2button.grid(row=6, column=1)
    #Vehicle bottom, turning right
    addVehicleC3_3button = tk.Button(admin_panel, width=23, text="Vehicle Bottom, Right Turn", command=lambda: [TrafficSystem.inter.roadsObj[0].vehiclesInLane2.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[0], 3, 3)), log_message(log, "Added Vehicle at Bottom Turning Right")] ) 
    addVehicleC3_3button.grid(row=6, column=2)

    #Vehicle left, turning left
    addVehicleC4_1button = tk.Button(admin_panel, width=23, text="Vehicle Left, Left Turn", command=lambda: [TrafficSystem.inter.roadsObj[1].vehiclesInLane2.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[1], 1, 4)), log_message(log, "Added Vehicle at Left Turning Left")] ) 
    addVehicleC4_1button.grid(row=7, column=0)
    #Vehicle left, going straight
    addVehicleC4_2button = tk.Button(admin_panel, width=23, text="Vehicle Left, Straight", command=lambda: [TrafficSystem.inter.roadsObj[1].vehiclesInLane2.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[1], 2, 4)), log_message(log, "Added Vehicle at Left Going Straight")] ) 
    addVehicleC4_2button.grid(row=7, column=1)
    #Vehicle left, turning right
    addVehicleC4_3button = tk.Button(admin_panel, width=23, text="Vehicle Left, Right Turn", command=lambda: [TrafficSystem.inter.roadsObj[1].vehiclesInLane2.append(Vehicle(True,False,"Admin",20,"type","ABC",TrafficSystem.inter, TrafficSystem.inter.roadsObj[1], 3, 4)), log_message(log, "Added Vehicle at Left Turning Right")] ) 
    addVehicleC4_3button.grid(row=7, column=2)



    #Buttons for adding pedestrians #------------------------------------------------------------------------------------------------
    tk.Label(admin_panel, text=f"Add Pedestrian Buttons", font=("Arial", 10, "bold"), bg="white").grid(row=8, column=0)
    #Pedestrian Top, crossing from left
        #Naming Sidewalk# Side#
    addPedestrian_s1s1button = tk.Button(admin_panel, width=23, text="Pedestrian Top, From Left", command=lambda: [TrafficSystem.inter.sidewalksObj[0].sidewalk1.append(Pedestrian(-1, TrafficSystem.inter, 0, TrafficSystem.inter.sidewalksObj[0], 1, 8)), log_message(log, "Added Pedestrian at Top Crossing From Left")]  ) 
    addPedestrian_s1s1button.grid(row=9, column=0)
    #Pedestrian Top, crossing from left
    addPedestrian_s1s2button = tk.Button(admin_panel, width=23, text="Pedestrian Top, From Right", command=lambda: [TrafficSystem.inter.sidewalksObj[0].sidewalk2.append(Pedestrian(-1, TrafficSystem.inter, 0, TrafficSystem.inter.sidewalksObj[0], 2, 8)), log_message(log, "Added Pedestrian at Top Crossing From Right")]  ) 
    addPedestrian_s1s2button.grid(row=9, column=1)

    #Pedestrian Right, crossing from top
    addPedestrian_s2s1button = tk.Button(admin_panel, width=23, text="Pedestrian Right, From Top", command=lambda: [TrafficSystem.inter.sidewalksObj[1].sidewalk1.append(Pedestrian(-1, TrafficSystem.inter, 1, TrafficSystem.inter.sidewalksObj[1], 1, 12)), log_message(log, "Added Pedestrian at Right Crossing From Top")]  ) 
    addPedestrian_s2s1button.grid(row=10, column=0)
    #Pedestrian Right, crossing from bottom
    addPedestrian_s2s2button = tk.Button(admin_panel, width=23, text="Pedestrian Right, From Bottom", command=lambda: [TrafficSystem.inter.sidewalksObj[1].sidewalk2.append(Pedestrian(-1, TrafficSystem.inter, 1, TrafficSystem.inter.sidewalksObj[1], 2, 12)), log_message(log, "Added Pedestrian at Right Crossing From Bottom")]  ) 
    addPedestrian_s2s2button.grid(row=10, column=1)

    #Pedestrian Bottom, crossing from left
    addPedestrian_s3s1button = tk.Button(admin_panel, width=23, text="Pedestrian Bottom, From Left", command=lambda: [TrafficSystem.inter.sidewalksObj[2].sidewalk2.append(Pedestrian(-1, TrafficSystem.inter, 0, TrafficSystem.inter.sidewalksObj[2], 2, 16)), log_message(log, "Added Pedestrian at Bottom Crossing From Left")] )
    addPedestrian_s3s1button.grid(row=11, column=0)
    #Pedestrian Bottom, crossing from left
    addPedestrian_s3s2button = tk.Button(admin_panel, width=23, text="Pedestrian Bottom, From Right", command=lambda: [TrafficSystem.inter.sidewalksObj[2].sidewalk1.append(Pedestrian(-1, TrafficSystem.inter, 0, TrafficSystem.inter.sidewalksObj[2], 1, 16)), log_message(log, "Added Pedestrian at Bottom Crossing From Right")]  ) 
    addPedestrian_s3s2button.grid(row=11, column=1)

    #Pedestrian Left, crossing from top
    addPedestrian_s4s1button = tk.Button(admin_panel, width=23, text="Pedestrian Left, From Top", command=lambda: [TrafficSystem.inter.sidewalksObj[3].sidewalk2.append(Pedestrian(-1, TrafficSystem.inter, 1, TrafficSystem.inter.sidewalksObj[3], 2, 4)), log_message(log, "Added Pedestrian at Left Crossing From Top")]  ) 
    addPedestrian_s4s1button.grid(row=12, column=0)
    #Pedestrian Left, crossing from bottom
    addPedestrian_s4s2button = tk.Button(admin_panel, width=23, text="Pedestrian Left, From Bottom", command=lambda: [TrafficSystem.inter.sidewalksObj[3].sidewalk1.append(Pedestrian(-1, TrafficSystem.inter, 1, TrafficSystem.inter.sidewalksObj[3], 1, 4)), log_message(log, "Added Pedestrian at Left Crossing From Bottom")]  ) 
    addPedestrian_s4s2button.grid(row=12, column=1)



    #Change Colour of Traffic Light Buttons------------------------------------------------------------------------------------------------------------------

    traffic_light_buttons = [
        tk.Button(admin_panel, width=23, text="Top & Bottom", command=lambda: [toggle_traffic_light(canvas, "traffic_light_1"), log_message(log, "Changing Top and Bottom Traffic Light to Next Colour")]  ),
        tk.Button(admin_panel, width=23, text="Left & Right", command=lambda: [toggle_traffic_light(canvas, "traffic_light_2"), log_message(log, "Changing Left and Right Traffic Light to Next Colour")]  )
        # tk.Button(admin_panel, text="Traffic Light 3", command=lambda: toggle_traffic_light(canvas, "traffic_light_3")),
        # tk.Button(admin_panel, text="Traffic Light 4", command=lambda: toggle_traffic_light(canvas, "traffic_light_4")),
    ]

    pedestrian_light_buttons = [
        tk.Button(admin_panel, width=23, text="Top & Bottom", command=lambda: [toggle_pedestrian_light(canvas, "ped_light_1"), log_message(log, "Changing Top and Bottom Pedestrian Light to Next Colour")] ),
        tk.Button(admin_panel, width=23, text="Left & Right", command=lambda: [toggle_pedestrian_light(canvas, "ped_light_2"), log_message(log, "Changing Left and Right Pedestrian Light to Next Colour")] )
        # tk.Button(admin_panel, text="Pedestrian Light 3", command=lambda: toggle_pedestrian_light(canvas, "ped_light_3")),
        # tk.Button(admin_panel, text="Pedestrian Light 4", command=lambda: toggle_pedestrian_light(canvas, "ped_light_4")),
        # tk.Button(admin_panel, text="Pedestrian Light 5", command=lambda: toggle_pedestrian_light(canvas, "ped_light_5")),
        # tk.Button(admin_panel, text="Pedestrian Light 6", command=lambda: toggle_pedestrian_light(canvas, "ped_light_6")),
        # tk.Button(admin_panel, text="Pedestrian Light 7", command=lambda: toggle_pedestrian_light(canvas, "ped_light_7")),
        # tk.Button(admin_panel, text="Pedestrian Light 8", command=lambda: toggle_pedestrian_light(canvas, "ped_light_8")),
    ]
    tk.Label(admin_panel, justify='left', text=f"Change Traffic Light Colour", font=("Arial", 10, "bold"), bg="white").grid(row=13, column=0, columnspan = 2, sticky="W")
    for i, button in enumerate(traffic_light_buttons, start=1):
        button.grid(row=14, column=i-1)
    tk.Label(admin_panel, text=f"Change Pedestrian Light Colour", font=("Arial", 10, "bold"), bg="white", anchor="w").grid(row=15, column=0, columnspan = 2, sticky="W")
    for i, button in enumerate(pedestrian_light_buttons, start=1):
        button.grid(row=16, column=i-1)

    
    #Buttons for toggling auto traffic
    tk.Label(admin_panel, text=f"Toggle Auto Traffic", font=("Arial", 10, "bold"), bg="white", anchor="w").grid(row=17, column=0, columnspan = 2, sticky="W")
    toggleAutoVehicle_button = tk.Button(admin_panel, text="Toggle Auto Vehicles", command=lambda:toggleAutoVeh(), width=23) 
    toggleAutoVehicle_button.grid(row=18, column=0)
    toggleAutoPedestrian_button = tk.Button(admin_panel, text="Toggle Auto Pedestrians", command=lambda:toggleAutoPed(), width=23) 
    toggleAutoPedestrian_button.grid(row=18, column=1)






    # toggleAutoPedestrian_button = tk.Button(admin_panel, text="Toggle Auto Pedestrians", command=lambda:[toggleAutoPed(), log_message(log, "Toggle Auto Pedestrians")], width=23) 
    # toggleAutoPedestrian_button.grid(row=18, column=1)




def create_console_window(window, x, y, width, height):
    frame = tk.Frame(master=window, bg='#808080')
    frame.place(x=x, y=y)
    log = ScrolledText(master=frame, wrap=tk.WORD, width=width, height=height, state=tk.DISABLED)
    log.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
    return log

def log_message(console:ScrolledText, text:str):
    console.configure(state="normal")
    console.insert(tk.INSERT, text + "\n")
    console.configure(state="disabled")

    
    #-----------------------------------------------------------------------------------
    # pedestrian_count_positions = [
    # (250, 290),
    # (570, 290),
    # (250, 610),
    # (570, 610)
    # ]

    # car_count_positions = [
    # (50, 450),
    # (750, 450),
    # (400, 100),
    # (400, 800)
    # ]   

    # # for i, (x, y) in enumerate(pedestrian_count_positions, start=1):
    # #     display_pedestrian_count(canvas, x, y, 1, f"ped_count_text_{i}")

    # # for i, (x, y) in enumerate(car_count_positions, start=1):
    # #     display_car_count(canvas, x, y, 0, f"car_count_text_{i}")


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

    # Center the window on the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))

    create_legend(canvas)
    create_admin_panel(window, canvas)
    global log
    log = create_console_window(window, 1440, 0, 55, 60)

    verticalRoad = TrafficSystem.inter.trafficLightObj[0]
    horizontalRoad = TrafficSystem.inter.trafficLightObj[1]

    log_message(log, "Admin View Loaded")
    # log_message(log, "testing")


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

if __name__ == "__main__":
    create_intersection()

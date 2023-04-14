# CPS406-Traffic-Management-System

This is our group project for CPS406, it is called MetroFloPro and is a simple tool for Traffic Administrators to simulate traffic, while also allowing regular/normal users to see the simulation.

The project is created with Python3, and we have used Tkinter, Pillow, Unittest, and Threading.

You are able to control traffic lights, pedestrian lights, pedestrians, and vehicles.

There are several admin tools within the admin view of the intersection.

### Instructions to install and run the program are at the bottom

Default credentials for the admin are: 
    
    Username: admin
    
    Password: pass



## Group # 4 Members:
Mathew P

Mohit S

Joseph Z

Abdullah H

Abdullah I

Aoun H

## Screenshots of the program:

Main Menu

![image](https://user-images.githubusercontent.com/90167278/231909876-d4f42593-2b2b-40ff-96a5-a8e40242d612.png)

Admin Login

![image](https://user-images.githubusercontent.com/90167278/231909900-5a0cade7-cfeb-4867-a21c-ab9adf83ad08.png)

Admin View

![image](https://user-images.githubusercontent.com/90167278/231909848-b3d2773b-2653-4b22-b5c6-0f1e6af2e2e1.png)

![image](https://user-images.githubusercontent.com/90167278/231909675-e953af52-7d4f-4087-8e92-8404960cd736.png)

![image](https://user-images.githubusercontent.com/90167278/231909756-50189bdc-ab51-41ee-964e-29f265afa007.png)

Normal View

![image](https://user-images.githubusercontent.com/90167278/231910029-f5babfe4-311f-4204-8f9a-bbdee6a7b615.png)


## Instructions on how to install and run MetroFloPro:

### NOTE: There is a required screen resolution of 1080p and 100% display text size, for the program to look and run as intended

    -There are two ways to install the program, either:
        -Run the following command within a terminal opened on a new file: 
        “git clone git@github.com:MrMothi/CPS406-Traffic-Management-System.git”
            OR
        -Download zip of main branch on the github repo for this program from “https://github.com/MrMothi/CPS406-Traffic-Management-System”

    -Run the executable within the "Executable TrafficSystem File" folder, OR run the “TrafficSystem.py” file with python
        -If running the python file, then before running install the Python Pillow Library via python PIP on your machine              
        (from "https://pillow.readthedocs.io/en/stable/installation.html")
    -You will now see a simple landing page for the application
    -Proceed to Admin Login to use the full capability of the program
    -Use the following admin credentials:
        User:  Admin2
        Password: traffic
    -You now have the access to the Admin View





## Instructions on how to use the Admin Panel & Other Features:

    Preconditions of the intersection:
        -By default, the intersection does not have any automatic vehicle and pedestrian traffic
        -Traffic movement is also disabled at the start, this is to allow the admin to add any vehicles and pedestrians to the intersection before they start moving
        -All trafficlights and pedestrian lights are running in sync

    How to run a simple instance of the intersection:
        -Add any needed vehicles and pedestrians using the buttons in the “Add Vehicle Buttons” and “Add Pedestrian Buttons” categories. Changes will be shown in various locations on the intersection display
        -If needed, toggle on automatic vehicles and or automatic pedestrians using the “Toggle Auto Traffic” category buttons
        -Finally use the “Toggle Traffic” Button in the “Toggle Loop Buttons” category
        -Now the system will run the simulation with the settings you have set

    Other features: 
        -An emergency event can be triggered which sets all lights to red and stops any traffic
        -You can manually change the light colour of the vertical and horizontal lights of both trafficlights and pedestrian lights (Remains that colour for the remainder of light time slice)
        -Lights can be resynced at any time
        -Traffic can be reset/cleared
        -The intersection can be reset to default conditions
        -Traffic and Pedestrian lights can be disabled (Will show the colour black and will not allow traffic through
        -Normal view is a simple view of the intersection without any admin tools and displays its current state
        -Any changes made by the admin can be seen within normal view

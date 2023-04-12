CPS406 Project: MetroFloPro


→ Instructions on how to install and run MetroFloPro:

    -There are two ways to install the program, either:
        -Run the following command within a terminal opened on a new file: 
        “Git clone git@github.com:MrMothi/CPS406-Traffic-Management-System.git”
        
        -Download zip of main branch on the github repo for the program “https://github.com/MrMothi/CPS406-Traffic-Management-System”
        Before running, Install the Python Pillow Library via PIP on your machine (https://pillow.readthedocs.io/en/stable/installation.html)

    -Run the “TrafficSystem.py” file with python
    -You will now see a simple landing page for the application
    -Proceed to Admin Login to use the full capability of the program
    -Use the following admin credentials:
        User:  Admin2
        Password: traffic
    -You now have the access to the Admin View





→ Instructions on how to use the Admin Panel

    Preconditions of the intersection:
        -By default, the intersection does not have any automatic vehicle and pedestrian traffic
        -Traffic movement is also disabled at the start to allow the admin to add any vehicles and pedestrians to the intersection before they move out of the intersection
        -All trafficlights and pedestrian lights are running in sync

    How to run a simple instance of the intersection:
        -Add any needed vehicles and pedestrians using the buttons in the “Add Vehicle Buttons” and “Add Pedestrian Buttons” categories. Changes will be shown in various locations on the intersection display
        -Toggle on automatic traffic and or automatic pedestrians using the “Toggle Auto Traffic” category buttons
        -Finally use the “Toggle Traffic” Button in the “Toggle Loop Buttons” category
        -Now the system will run the simulation with the settings you have set

    Other features: 
        -An emergency event can be triggered which sets all lights to red and stops any traffic
        -You can manually change the light colour of the vertical and horizontal lights of both trafficlights and pedestrian lights (Remains that colour for the remainder of light time slice)
        -Lights can be resynced at any time
        -Traffic can be reset/cleared
        -The intersection can be reset to default conditions
        -Traffic and Pedestrian lights can be disabled (Will show the colour black and not allow traffic through.


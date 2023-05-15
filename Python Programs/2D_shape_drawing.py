from pyniryo2 import *
import matplotlib.pyplot as plt
import numpy as np

robot=NiryoRobot("169.254.200.200")
robot.arm.calibrate_auto() # Automatic calibration of the robotic arm
robot.tool.update_tool()


def display_menu():
    print("Welcome to Shape Drawing Program!")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Hexagon")
    print("6. Exit")

def option1():
    print("Option 1 selected.")
    trajectory=[]
    radius=0.065 # Radius of the circle in cm
    theta=np.linspace(0, 2*np.pi, 60) # Generate 40 points around the circle
    y=radius*np.cos(theta) # Calculate y-coordinates
    z=radius*np.sin(theta) # Calculate z-coordinates
    znew=[]
    for x in z:
        znew.append(x+0.3)

    plt.plot(y, znew)
    plt.xlabel('y (cm)')
    plt.ylabel('z (cm)')
    plt.axis ('equal') #Set equal scaling for x and y axes
    plt.title('Circle in the yz Plane')
    plt.show()

    for val1, val2 in zip (y, z) :
        trajectory.append([0.3,val1,val2+0.3,0.,0.,0., 1.1])
    robot.trajectories.execute_trajectory_from_poses(trajectory)


def option2():
    print("Option 2 selected.")
    trajectory = [[0.3, 0.1, 0.3, 0.,0.,0., 1.],[0.3,-0.1, 0.3, 0.,0., 0., 1.],[0.3,-0.1, 0.5, 0.,0., 0., 1.],[0.3, 0.1, 0.5, 0.,0.,0., 1.],[0.3, 0.1, 0.3, 0.,0., 0., 1.]]
    robot.trajectories.execute_trajectory_from_poses (trajectory)

def option3():
    print ("Option 3 selected.")
    trajectory=[[0.3, 0.1, 0.3, 0.,0., 0.,1.],[0.3,- 0.1, 0.3, 0., 0.,0., 1.],[0.3,-0.1, 0.4, 0., 0., 0., 1.],[0.3, 0.1, 0.4, 0., 0., 0., 1.],[0.3, 0.1, 0.3, 0., 0., 0., 1.]]
    robot.trajectories.execute_trajectory_from_poses (trajectory)

def option4():
    print ("Option 4 selected.")
    trajectory=[[0.3, 0.1, 0.3, 0., 0., 0.,1.],[0.3,-0.1, 0.3, 0.,0., 0.,1.],[0.3,-0.1,0.4, 0., 0.,0., 1.],[0.3, 0.1,0.3,0.,0.,0.,1.]]
    robot.trajectories.execute_trajectory_from_poses (trajectory)

def option5():
    print("Option 5 selected.")
    trajectory=[[0.3, 0.1, 0.3, 0.,0.,0., 1.],[0.3, 0., 0.2,0.,0.,0., 1.],[0.3,-0.1, 0.3, 0.,0.,0., 1.],[0.3,-0.1, 0.4, 0., 0., 0., 1.],[0.3, 0.0, 0.5, 0.,0., 0., 1.],[0.3, 0.1, 0.4, 0.,0.,0., 1.],[0.3, 0.1, 0.3, 0.,0.,0., 1.]]
    robot.trajectories.execute_trajectory_from_poses (trajectory)

while True:
    display_menu ()
    choice=input("Enter your choice: ")
    if choice =='1':
        option1()
    elif choice =='2':
        option2 ()
    elif choice=='3':
        option3()
    elif choice=='4':
        option4()
    elif choice=='5':
        option5()
    elif choice=='6':
        print("Thank you for using the program. Exiting...")
        break
    else:
        print ("Invalid choice. Please try again.")

robot.arm.move_to_home_pose() #moving the arm to a home position
robot.end() #terminating the connection to the robotic arm
from pyniryo2 import * #importing pyniryo2 module into the current workspace
robot=NiryoRobot("169.254.200.200") # this is the IP address for ethernet connection
i=0
robot.arm.calibrate_auto() # calibrating the arm
robot.tool.update_tool() #equiping the tool/end effector
robot.tool.release_with_tool() #opening the tool/end effector
while i<6:
    robot.pick_place.pick_from_pose ([0.160,0.167,0.083,3.040,1.229,3.080]) #pick position (x, y, z, roll, pitch, yaw), arm will automatically close the gripper
    robot.arm.move_pose ([0.186,0.155,0.145,2.757, 1.166,3.079]) #intermediate position (x, y, z, roll, pitch, yaw)
    robot.pick_place.place_from_pose ([0.000,-0.263,0.018,2.503,1.443,0.987]) #place position (x, y, z, roll, pitch, yaw), arm will automatically open the gripper
    i+=1


robot.arm.go_to_sleep () #arm returns to home position
robot.end() #connection is disabled
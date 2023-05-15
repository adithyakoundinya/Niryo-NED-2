from pyniryo2 import *
import keyboard
robot= NiryoRobot("169.254.200.200")
robot.arm.caliberate_auto()
robot.arm.set_jog_control(True)

while True:

    joint_angles= robot.arm.get_joints()
    if keyboard.is_pressed('a') and joint_angles[0]<=2.7:
        robot.arm.jog_joints([0.1, 0.0, 0.0, 0.0, 0.0, 0.0])
    elif keyboard.is_pressed('d') and joint_angles[0]>=2.7:
        robot.arm.jog_joints([-0.1, 0.0, 0.0, 0.0, 0.0, 0.0])
    elif keyboard.is_pressed('w') and joint_angles[0]<=0.4:
        robot.arm.jog_joints([0.0, 0.1, 0.0, 0.0, 0.0, 0.0])
    elif keyboard.is_pressed('s') and joint_angles[0]>=-1.6:
        robot.arm.jog_joints([0.0, -0.1, 0.0, 0.0, 0.0, 0.0])
    elif keyboard.is_pressed('i') and joint_angles[0]<=1.37:
        robot.arm.jog_joints([0.0, 0.0, 0.1, 0.0, 0.0, 0.0])
    elif keyboard.is_pressed('k') and joint_angles[0]>=-1.14:
        robot.arm.jog_joints([0.0, 0.0, -0.1, 0.0, 0.0, 0.0])
    elif keyboard.is_pressed('j') and joint_angles[0]<=1.89:
        robot.arm.jog_joints([0.0, 0.0, 0.0, 0.1, 0.0, 0.0])
    elif keyboard.is_pressed('l') and joint_angles[0]>=-1.89:
        robot.arm.jog_joints([0.0, 0.0, 0.0, -0.1, 0.0, 0.0])
    elif keyboard.is_pressed('up_arrow') and joint_angles[0]<=1.72:
        robot.arm.jog_joints([0.0, 0.0, 0.0, 0.0, 0.1, 0.0])
    elif keyboard.is_pressed('down_arrow') and joint_angles[0]>=-1.72:
        robot.arm.jog_joints([0.0, 0.0, 0.0, 0.0, -0.1, 0.0])
    elif keyboard.is_pressed('right_arrow') and joint_angles[0]<=2.33:
        robot.arm.jog_joints([0.0, 0.0, 0.0, 0.0, 0.0, 0.1])
    elif keyboard.is_pressed('left_arrow') and joint_angles[0]>=-2.33:
        robot.arm.jog_joints([0.0, 0.0, 0.0, 0.0, 0.0, -0.1])
    elif keyboard.is_pressed('q'):
        break

from pyniryo2 import *
workspace_name="Conveyor_Workspace"
robot=NiryoRobot ("169.254.200.200") #Establishing connection with the robotic arm
robot.arm.calibrate_auto () # Automatic calibration of the robotic arm
robot.tool.setup_electromagnet(PinID.DO4) # Equiping the given tool/end effector
conveyor_id = robot.conveyor.set_conveyor ()


pick=PoseObject(x-0.230,y=-0.185,z=0.072,roll=-2.084,pitch=1.466,yaw=-2.078)
inter=PoseObject(x-0.224,y=-0.171,z=0.200,roll=-1.309,pitch=1.411,yaw=-1.362)
place=PoseObject(x = -0.013,y=-0.257,z=0.024, rol1=-1.863,pitch=1.494,yaw=-3.089)
k=0
robot.io.digital_read(PinID.DI5)

while (k<10):
    robot.conveyor.run_conveyor(conveyor_id, speed=50,direction=ConveyorDirection.FORWARD)
    if(robot.io.digital_read(PinID.DI5)==False):
        robot.conveyor.stop_conveyor(conveyor_id)
        robot.arm.move_pose (pick)
        robot.tool.activate_electromagnet(PinID.DO4)
        robot.arm.move_pose (inter)
        robot.arm.move_pose (place)
        robot.tool.deactivate_electromagnet(PinID.DO4)
        robot.wait (0.2)
        robot.arm.move_pose (inter)
        k+=1

    robot.conveyor.run_conveyor(conveyor_id, speed=50,direction=ConveyorDirection.FORWARD)
    robot.wait (0.7)
    


robot.conveyor.stop_conveyor (conveyor_id) #stopping the conveyor
robot.conveyor.unset_conveyor(conveyor_id) #disconnecting the conveyor
robot.tool.deactivate_electromagnet(PinID.DO4) #de-energizing the electromagnet
robot.arm.move_to_home_pose () #moving the arm to a home position
robot.end() #terminating the connection to the robotic arm
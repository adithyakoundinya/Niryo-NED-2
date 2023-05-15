from pyniryo2 import *
workspace_name="Conveyor_Workspace" 
robot=NiryoRobot("169.254.200.200") #Establishing connection with the robotic arm


observation_pose = PoseObject(x=0.203,y=-0.003,z=0.318,roll=-2.921,pitch=1.282,yaw=-2.950)
place_pose_blue=PoseObject(x=0.043,y=-0.168,z=0.125,roll=2.341,pitch=1.496,yaw=0.854)
place_pose_red=PoseObject(x=0.041,y=-0.334,z=0.137,roll=2.128,pitch=1.534,yaw=0.634)
place_pose_green=PoseObject(x=-0.117,y=-0.325,z=0.142,roll=-1.772,pitch=1.507,yaw=2.967)
intermediate_pose = PoseObject(x=0.207,y=0.003,z=0.267,roll=2.491,pitch=1.529,yaw=2.488)


robot.arm.calibrate_auto() # Automatic calibration of the robotic arm
robot.tool.update_tool() # Equiping the given tool/end effector

max_count=10
count=0
failure_count=0

count_dict={
    ObjectColor.BLUE: 0,
    ObjectColor.RED: 0,
    ObjectColor.GREEN: 0} # dictionary to keep count of the number of objects of differerent colors being picked up

while count<max_count:
    robot.arm.move_pose(observation_pose) #move to observation position
    obj_found, shape, color = robot.vision.vision_pick(workspace_name,height_offset=-0.012) # perfrom vision based pick up

    if not obj_found:
        robot.wait(1) #waits for one second if no object is detected
        if not obj_found:
            failure_count+=1 # imcrementing failure count if still no obejct is detected
            if failure_count==10:
                print("Failed to detect object") 
                break #if failure count reaches 10, the execution will break out of the loop and the arm will enter sleep mode
        continue
    if obj_found:
        failure_count=0 # resetting failure count if and when an object is detected

    if color==ObjectColor.BLUE : 
        robot.arm.move_pose(intermediate_pose) #moving to intermediate position
        robot.pick_place.place_from_pose(place_pose_blue) # placing the object at a pre defined location
        
    elif color == ObjectColor.RED:
        robot.arm.move_pose(intermediate_pose)
        robot.pick_place.place_from_pose(place_pose_red)
    else:
        robot.arm.move_pose(intermediate_pose)
        robot.pick_place.place_from_pose(place_pose_green)
       

    count_dict[color] += 1 #incrementing the count of objects in the dictionary of a particular color
    count+=1
    print(count_dict)
    


robot.wait(0.2)
robot.tool.grasp_with_tool() #close the gripper/end effector
robot.arm.go_to_sleep() #arm enters sleep mode
robot.end() # connection to the arm is closed

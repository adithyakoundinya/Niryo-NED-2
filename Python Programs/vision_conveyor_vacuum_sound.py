from pyniryo2 import *
workspace_name="Conveyor_Workspace"
robot=NiryoRobot("169.254.200.200") #Establishing connection with the robotic arm
robot.sound.set_volume(100) #setting volume of the inbuilt speaker
robot.arm.calibrate_auto() # Automatic calibration of the robotic arm
robot.tool.update_tool() # Equiping the given tool/end effector

observation_pose = PoseObject (x=0.159, y=0.003, z=0.252, roll=2.953, pitch=1.420, yaw=2.938)
place_pose_red=PoseObject (x=0.039, y=-0.258, z=0.032, roll=-1.003, pitch=1.512, yaw=2.490)
intermediate_pose = PoseObject (x=0.210, y=-0.004,z=0.179, roll=1.565, pitch=1.488, yaw=1.537)

red_circle_count=0 #count for red circles picked up
failure_count=0
shape_expected=ObjectShape.CIRCLE
color_expected=ObjectColor.RED
conveyor_id = robot.conveyor.set_conveyor ()

while True:
    robot.arm.move_pose(observation_pose) #move to observation position
    robot.conveyor.run_conveyor (conveyor_id,speed=50,direction=ConveyorDirection.FORWARD) #running the conveyor
    obj_detect,obj_pos,shape,color=robot.vision.detect_object(workspace_name,shape=shape_expected,color=color_expected) #detecting red circles within the given Conveyor Workspace
    
    if not obj_detect:
        robot.wait (1)
        if not obj_detect:
            failure_count+-1
            if failure_count==25:
                print ("Failed to detect object")
                break
        continue


    if obj_detect:
        failure_count=0


    robot.conveyor.stop_conveyor(conveyor_id)
    obj_found, shape, color = robot. vision.vision_pick (workspace_name, height_offset=-0.012, shape=shape_expected,color=color_expected) # perform vision based pick up
    robot.sound.play("red.wav") #playing an audio file through the inbuilt speaker
    robot.arm.move_pose (intermediate_pose) #moving to intermediate position
    robot.pick_place.place_from_pose (place_pose_red) # placing the object at a pre defined location
    red_circle_count+= 1 #incrementing count of red circles
    print ("Number of Red Objects picked up:", red_circle_count)



robot.sound.play("return_home.wav")
robot.wait (0.2)
robot.conveyor.stop_conveyor (conveyor_id) #stopping the conveyor
robot.conveyor.unset_conveyor (conveyor_id) #disconnecting the conveyor
robot.tool.grasp_with_tool () #switching off the vacuum pump
robot.arm.move_to_home_pose () #moving the arm to a home position
robot.end() #terminating the connection to the robotic arm
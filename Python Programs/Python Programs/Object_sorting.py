from pyniryo2 import *
workspace_name="Conveyor_Workspace"
robot=NiryoRobot("169.254.200.200")

observation_pose = PoseObject(x=0.203,y=-0.003,z=0.318,roll=-2.921,pitch=1.282,yaw=-2.950)
place_pose_square=PoseObject(x=0.041,y=-0.334,z=0.137,roll=2.128,pitch=1.534,yaw=0.634)
place_pose_circle=PoseObject(x=-0.117,y=-0.325,z=0.142,roll=-1.772,pitch=1.507,yaw=2.967)

intermediate_pose = PoseObject(x=0.207,y=0.003,z=0.267,roll=2.491,pitch=1.529,yaw=2.488)

robot.arm.calibrate_auto()
robot.tool.update_tool()

max_count=10
count=0
failure_count=0


count_dict={
    ObjectShape.SQUARE: 0,
    ObjectShape.CIRCLE: 0}


while count<max_count:
    robot.arm.move_pose(observation_pose)
    obj_found, shape, color = robot.vision.vision_pick(workspace_name,height_offset=-0.012)

    if not obj_found:
        robot.wait(20)
        if not obj_found:
            print("Failed to detect object")
            break
        continue


    if shape==ObjectShape.SQUARE :
        robot.arm.move_pose(intermediate_pose)
        robot.pick_place.place_from_pose(place_pose_square)
    else:
        robot.arm.move_pose(intermediate_pose)
        robot.pick_place.place_from_pose(place_pose_circle)


    count_dict[shape] += 1
    count+=1


    print(count_dict)

robot.wait(0.2)
robot.tool.grasp_with_tool()
robot.arm.go_to_sleep()
robot.end()

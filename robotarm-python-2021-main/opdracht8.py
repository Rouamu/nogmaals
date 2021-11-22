from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for y in range(7):
    robotArm.grab()
    for x in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(8):
        robotArm.moveLeft()
robotArm.wait()
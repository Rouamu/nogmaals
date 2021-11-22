from pygame import color
from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
color = robotArm.scan()
for x in range(7):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() !="white":
        robotArm.drop()   
    if robotArm.scan() =="white":
      robotArm.grab()
      robotArm.moveRight()
      robotArm.drop()
    robotArm.moveRight()
robotArm.wait()
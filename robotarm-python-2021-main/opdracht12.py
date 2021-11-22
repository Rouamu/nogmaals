from pygame import color
from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
color = robotArm.scan()
move = 10
for i in range(10,1,-1):
    robotArm.grab()
    if robotArm.scan() !="red":
        robotArm.drop()   
    if robotArm.scan() =="red":
      robotArm.grab()
      for x in range(i):
       robotArm.moveRight()
      robotArm.drop()
      for x in range(x):
        robotArm.moveLeft()
    robotArm.moveRight()
    
robotArm.wait()
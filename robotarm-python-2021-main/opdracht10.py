from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for r in range(9,0,-2):
    robotArm.grab()
    for x in range(r):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(r-1):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
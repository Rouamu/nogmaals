from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
for i in range(1,5):
    for o in range(1,5):
        robotArm.grab()
        for u in range(1,6):
            robotArm.moveRight()
        robotArm.drop()
        for r in range(1, 5):
            robotArm.moveLeft()
    for i in range(1, 5):
        robotArm.moveLeft()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    for i in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for y in range(4):
        for x in range(2):
            robotArm.moveRight()
        for i in range(6):
            robotArm.moveRight()
            robotArm.grab()
            robotArm.moveLeft()
            robotArm.drop()
    
            

        
        


# Na jouw code wachten tot het sluiten van de window:
    robotArm.wait()
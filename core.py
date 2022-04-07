#FireDrone Navigation Simulator - Version 7.3 Beta
#Made by Prof. Yael Edan, Mr. Moshe Bardea, Gal Fried
#Algorithems inspierd from Eyal Elazari and Ofir Nagauker's simulator

#Creating the requierd global varibels
x = 0
y = 0
z = 0

#You can add the obsticles here, in this format: [x,y,z]. don't change any other varible exept of obsticles
obsticles = [[-1,0,0],[0,4,0],[2,3,0],[3,0,0],[1,4,0],[0,160,0]]
#obsticles = [[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
#obsticles = [[0,4,0]]

trys = []
zTrys = []

frontObsticle = False
rightObsticle = False
leftObsticle = False
backObsticle = False

direction = 0

temp = 0

originalX = x

howManyToGo = 1

#The flight loop
while True:
    
    #Reset the varibles to their default possition
    frontObsticle = False
    leftObsticle = False
    rightObsticle = False
    backObsticle = False

    #Scaning is there an obsticle infront of the drone 150 units away
    i = 0
    while i < len(obsticles):
        print("scan")
        o = obsticles[i]
        if (o[0] == x) and (y + 150 > o[1] > y) and (o[2] == z):
            frontObsticle = True
        
        i = i + 1
    
    #Scaning is there an obsticle right to the drone 4 units away
    rightObsticle = False
    i = 0
    while i < len(obsticles):
        print("scan - r")
        o = obsticles[i]
        if (x < o[0] < x + 4) and (o[1] == y) and (o[2] == z):
            rightObsticle = True
        
        i = i + 1

    #Scaning is there an obsticle left to the drone 4 units away
    leftObsticle = False
    i = 0
    while i < len(obsticles):
        print("scan - l")
        o = obsticles[i]
        if (x - 4 < o[0] < x) and (o[1] == y) and (o[2] == z):
            leftObsticle = True
        
        i = i + 1
    
    #Scaning is there an obsticle back to the drone 150 units away
    backObsticle = False
    i = 0
    while i < len(obsticles):
        print("scan - b")
        o = obsticles[i]
        if (o[0] == x) and (y - 150 < o[1] < y) and (o[2] == z):
            backObsticle = True
        
        i = i + 1
    
    #If there is no obsticle infront, moving foward and setting the varibles to default stage
    if frontObsticle == False:
        y = y + 1
        trys = []
        howManyToGo = 1
    
    #The operation if there is obsticle infront
    else:
        print("colision")
        
        #If the drone didn't tried move away from the obsticle, by default it will move right and record the movement
        if (trys == []) and (rightObsticle == False):
            print("empty")
            originalX = x
            x = x + howManyToGo
            trys.append("R")
            howManyToGo = howManyToGo + 1
        
        #The operation if the drone already tried to move away from the obsticle
        else:
            print("full")
            print(trys)
            
            #Since the program record every movement to move away fron the obsticle until a succsses, this part count how many times the drone did every movement
            rightCounter = 0
            leftCounter = 0
            
            a = 0
            while a < len(trys):
                if trys[a] == "R":
                    rightCounter = rightCounter + 1
                else:
                    leftCounter = leftCounter + 1
                a = a + 1
            
            #If going right was more succssesful than going left, the drone will move right and record the movement - if there is nothing to the right
            if (rightCounter < leftCounter) and (rightObsticle == False):
                print("going right")
                x = x + howManyToGo
                trys.append("R")
                howManyToGo = howManyToGo + 1
            
            #If going left was more succssesful than going right, the drone will move left and record the movement - if there is nothing to the left
            elif (leftCounter < rightCounter) and (leftObsticle == False):
                print("going left")
                x = x - howManyToGo
                trys.append("L")
                howManyToGo = howManyToGo + 1
            
            #If both movements were succssesful equaly, the drone will check which side have obsticle and move to the opposite. If both sides have obsticles and there is nothing right infront the drone will move one step further.
            else:
                #If there is obsticle to the left and nothing to the right, the drone will move right.
                if (rightObsticle == False) and (leftObsticle == True):
                    print("going right")
                    x = x + howManyToGo
                    trys.append("R")
                    howManyToGo = howManyToGo + 1
                #If there is obsticle to the right and nothing to the left, the drone will move left.
                elif (rightObsticle == True) and (leftObsticle == False):
                    print("going left")
                    x = x - howManyToGo
                    trys.append("L")
                    howManyToGo = howManyToGo + 1
                #If both sides have an obsticle and there is nothing back, the drone will move back.
                elif (rightObsticle == True) and (leftObsticle == True) and (backObsticle == False):
                    print("going back")
                    y = y - howManyToGo
                    howManyToGo = howManyToGo + 1
                    print("moving to the side")
                    #If going right was more succssesful than going left, the drone will move right and record the movement - if there is nothing to the right
                    if (rightCounter < leftCounter) and (rightObsticle == False):
                        print("going right")
                        x = x + howManyToGo
                        trys.append("R")
                        howManyToGo = howManyToGo + 1
            
                    #If going left was more succssesful than going right, the drone will move left and record the movement - if there is nothing to the left
                    elif (leftCounter < rightCounter) and (leftObsticle == False):
                        print("going left")
                        x = x - howManyToGo
                        trys.append("L")
                        howManyToGo = howManyToGo + 1

                #If nothing was succssesful, changing the z
                else:
                    aboveObsticle = False
                    underObsticle = False

                    #Scaning is there an obsticle above the drone 4 units away
                    i = 0
                    while i < len(obsticles):
                        print("scan -a")
                        o = obsticles[i]
                        if (o[0] == x) and (o[1] == y) and (z + 4 > o[2] > z):
                            aboveObsticle = True
        
                        i = i + 1
                    
                    #Scaning is there an obsticle under the drone 4 units away
                    i = 0
                    while i < len(obsticles):
                        print("scan -u")
                        o = obsticles[i]
                        if (o[0] == x) and (o[1] == y) and (z - 4 < o[2] < z):
                            underObsticle = True
        
                        i = i + 1
                    
                    #If the drone can only go up, he will go up and record the movement
                    if (aboveObsticle == False) and (underObsticle == True):
                        print("going up")
                        z = z + howManyToGo
                        howManyToGo = howManyToGo + 1
                        zTrys.append("U")

                    #If the drone can only go down, he will go down and record the movement
                    elif (aboveObsticle == True) and (underObsticle == False):
                        print("going down")
                        z = z - howManyToGo
                        howManyToGo = howManyToGo + 1
                        zTrys.append("D")

                    #If the drone can go both ways, he will choose movement based on what was more succssesful. Then, he will go there and record the movement
                    elif (aboveObsticle == False) and (underObsticle == False):
                        print("selecting direction")

                        #Since the program record every movement to move away fron the obsticle until a succsses, this part count how many times the drone did every movement
                        upCounter = 0
                        downCounter = 0

                        a = 0
                        while a < len(zTrys):
                            if zTrys[a] == "U":
                                upCounter = upCounter + 1
                            else:
                                downCounter = downCounter + 1
                            a = a + 1

                        #If going up was more succssesful than going down and there is nothing above the drone, the drone will move up and record the movement
                        if (upCounter > downCounter) and (aboveObsticle == False):
                            print("going up")
                            z = z + howManyToGo
                            howManyToGo = howManyToGo + 1
                            zTrys.append("U")
                        
                        #If going down was more succssesful than going up and there is nothing under the drone, the drone will move down and record the movement
                        elif (downCounter > upCounter) and (underObsticle == False):
                            print("going down")
                            z = z - howManyToGo
                            howManyToGo = howManyToGo + 1
                            zTrys.append("D")
                        
                        #If both movements were succssesful, the drone will do the default - move up and record the movement
                        elif (upCounter == downCounter) and (aboveObsticle == False):
                            print("going up")
                            z = z + howManyToGo
                            howManyToGo = howManyToGo + 1
                            zTrys.append("U")
                        
                        #the drone can't move and the program quit
                        else:
                            print("drone in too tight situation! please replace the obsticles and try again.")
                            break

                    #The drone can't move and the program quit
                    else:
                        print("drone in too tight situation! please replace the obsticles and try again.")
                        break
    print(x)
    print(y)
    print(z)
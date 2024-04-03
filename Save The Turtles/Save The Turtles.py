##############################################################################
##                                                                          ##
##  Title: Save The Turtles                                                 ##
##                                                                          ##
##  Purpose: A game that uses graphics, user interactionsshows, and score   ##
##           keeping to show people the issues of litering the ocean.       ##
##                                                                          ##
##  Last Modified: 16/06/2019                                               ##
##                                                                          ##
##  Programmer: Thorben Wennemer                                            ##
##                                                                          ##
##############################################################################

from tkinter import *
from math import *  
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=1000, height=800, background="lightblue")
#Sets the initial values of everything in the game
#Gets called at the beginning of the game once a level has been selected
def setInitialValues():
    global numWaves,xWave,yWave,waveSize,waveSpeed,wave,turtlesSaved,xMouse,yMouse,xTurtle,yTurtle,xTurtleSpeed,yTurtleSpeed,redHealthBar,xRedHealthBar,yRedHealthBar,framNum,turtleGIF4
    global greenHealthBar,xGreenHealthBar,yGreenHealthBar,turtleDrawing,turtleSaved,turtleDead,dieRoll,xBoat,yBoat,xBoatSpeed,yBoatSpeed,boatDrawing,userQuit,gameRunning,xGreenHealthBarSize
    global Statistics,DeadTurtles,Dir,DIR,turtleGIF,a,b,c,d,e,f,g,h,j,k,l,turtleGIF1,turtleGIF2,turtleGIF3,frameNum,boatGIFN,boatGIFS,boatGIFE,boatGIFW,boatDirection,directions 
    global boatChargerGIF,boatChargerDrawing,batteryEmpty,RockGIFarray,RockGIF,Rock,xRock,yRock,boatCrash,boatCrashGIF,boatCrashGIFN,boatCrashGIFS,boatCrashGIFW,boatCrashGIFE,level
    global turtleGIF1Dead,turtleGIF2Dead,turtleGIF3Dead,s

    g = 0
    h = 0
    s = 4

    #frame number that the game is at
    frameNum = 0
    framNum = 0
    
    #Wave Values
    numWaves = 100
    xWave = []
    yWave = []
    waveSize = []
    waveSpeed = []
    wave = []

    for i in range(numWaves):
        xWave.append(uniform(0,1000))
        yWave.append(randint(0,800))
        waveSize.append(uniform(10,50))
        waveSpeed.append(uniform(1,3))
        wave.append(0)
    
    #Game Statistics
    Statistics = 0
    DeadTurtles = 0
    turtlesSaved = 0

    #Mouse starting position
    xMouse = 500
    yMouse = 500

    #Rock Values
    xrockMulti = 975/numRocks
    xRockMulti = 50
    m = 1
    
    RockGIF = []
    RockGIFarray = []
    Rock = []
    xRock = []
    yRock = []
    boatCrash = False

    for i in range(4):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "\Rock.gif", format = frameText)
        RockGIFarray.append(image)
        
    for i in range(numRocks):
        RockGIF.append(RockGIFarray[randint(0,3)])
        xRock.append(randint(int(xRockMulti), int(xrockMulti*m)))
        if i % 2 == 0:
            yRock.append(randint(50, 400))

        else:
            yRock.append(randint(400, 750))

        if xRock[i] > 420 and xRock[i] < 580 and yRock[i] > 320 and yRock[i] < 480:
            yRock[i] = yRock[i] + randint(100, 300)
        
        Rock.append(0)
        xRockMulti = xRockMulti + 1000/numRocks
        m = m + 1
        
        
    #Boat Crash Values
    j = 0
    k = 0
    l = 0
    boatCrashGIF = 0

    boatCrashGIFN = []
    for i in range(8):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatCrashN.gif", format = frameText)
        boatCrashGIFN.append(image)

    boatCrashGIFS = []
    for i in range(8):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatCrashS.gif", format = frameText)
        boatCrashGIFS.append(image)

    boatCrashGIFW = []
    for i in range(8):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatCrashW.gif", format = frameText)
        boatCrashGIFW.append(image)

    boatCrashGIFE = []
    for i in range(8):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatCrashE.gif", format = frameText)
        boatCrashGIFE.append(image)
    
    #Boat Charger Values
    e = 0
    boatChargerDrawing = 0
    batteryEmpty = False
    boatChargerGIF = []
    for i in range(2):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatCharger.gif", format = frameText)
        boatChargerGIF.append(image)
    
    #Boat Values
    xBoat = 500
    yBoat = 400
    xBoatSpeed = 0
    yBoatSpeed = 0
    boatDrawing = 0

    d = 0
    boatGIFN = []
    for i in range(4):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatN.gif", format = frameText)
        boatGIFN.append(image)

    boatGIFS = []
    for i in range(4):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatS.gif", format = frameText)
        boatGIFS.append(image)
    
    boatGIFE = []
    for i in range(4):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatE.gif", format = frameText)
        boatGIFE.append(image)

    boatGIFW = []
    for i in range(4):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "boatW.gif", format = frameText)
        boatGIFW.append(image)

    boatDirection = boatGIFN
    directions = []
    
    #Turtle Values
    xTurtle = []
    yTurtle = []
    xTurtleSpeed = []
    yTurtleSpeed = []
    turtleDrawing = []
    turtleSaved = []
    turtleDead = []
    dieRoll = []

    turtleGIF1Dead = PhotoImage(file = "turtle1Dead.gif")
    turtleGIF2Dead = PhotoImage(file = "turtle2Dead.gif")
    turtleGIF3Dead = PhotoImage(file = "turtle3Dead.gif")

    a = 0
    turtleGIF1 = []
    for i in range(6):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "turtle1.gif", format = frameText)
        turtleGIF1.append(image)

    b = 0
    turtleGIF2 = []
    for i in range(6):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "turtle2.gif", format = frameText)
        turtleGIF2.append(image)

    c = 0
    turtleGIF3 = []
    for i in range(6):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "turtle3.gif", format = frameText)
        turtleGIF3.append(image)

    f = 0
    turtleGIF4 = []
    for i in range(6):
        frameText = ("gif -index " + str(i))
        image = PhotoImage(file = "turtle4.gif", format = frameText)
        turtleGIF4.append(image)

    turtleGifArray = [turtleGIF1,turtleGIF2,turtleGIF3]

    turtleGIF = []
    
    redHealthBar = []
    xRedHealthBar = []
    yRedHealthBar = []
    greenHealthBar = []
    xGreenHealthBar = []
    yGreenHealthBar = []
    xGreenHealthBarSize = []
    DIR = []

    for i in range(numTurtles):
        xTurtle.append(uniform(0,940))
        yTurtle.append(uniform(0,740))
        xTurtleSpeed.append(0)
        yTurtleSpeed.append(0)
        turtleDrawing.append(0)
        turtleSaved.append(False)
        turtleDead.append(False)
        dieRoll.append(0)

        turtleGIF.append(choice(turtleGifArray))

        redHealthBar.append(0)
        xRedHealthBar.append(xTurtle[i] - 25)
        yRedHealthBar.append(yTurtle[i] - 30)
        greenHealthBar.append(0)
        xGreenHealthBar.append(xTurtle[i] - 25)
        yGreenHealthBar.append(yTurtle[i] - 30)
        xGreenHealthBarSize.append(50)
        DIR.append(uniform(-2,2))

    #Game Values
    userQuit = False
    gameRunning = True
    level = numTurtles / 2

#Creates an introduction screen with the game title, level selection, instruction, and quit selection
def introScreen():
    global numTurtles, xMouse,yMouse, numRocks
    #Level Selection Check Starting Values
    numTurtles = 0
    numTurtle = []
    x = 115
    y = 325
    x1 = []
    y1 = []

    for i in range(20):
        numTurtles = numTurtles + 2
        if i == 10:
            y = y + 80
            x = 115
        
        x1.append(x)
        y1.append(y)
        numTurtle.append(numTurtles)
        x = x + 80

    numRocks = 4
    numRock = []
    x = 115
    y = 325
    x1 = []
    y1 = []

    for i in range(20):
        if i % 3 == 0:
            numRocks = numRocks + 1
            
        if i == 10:
            y = y + 80
            x = 115
        
        x1.append(x)
        y1.append(y)
        numRock.append(numRocks)
        x = x + 80

    #Boolian starting values
    introScreen = True
    Instructions = False

    #Mouse starting position
    xMouse = 500
    yMouse = 500

    #Level Button starting values
    LevelsButtons = []
    LevelsText = []
    for i in range (20):
        LevelsButtons.append(0)
        LevelsText.append(0)
    
    while introScreen == True:
        #Game Title
        Title = screen.create_text(500, 125, text = "Save The Turtles", font = "ariel 80")


        #LEVELS
        #Level Title
        Levels = screen.create_text(500, 250, text = "Levels", font = "ariel 40")

        #Level Buttons
        x = 115
        y = 325
        levels = 1
        for i in range(20):
            LevelsButtons[i] = screen.create_rectangle(x, y, x+40, y+40, fill = "white", width = 4)
            LevelsText[i] = screen.create_text(x+20, y+20, text = str(levels), font = "ariel 20")
            if i == 9:
                y = y + 80
                x = 115

            else:
                x = x + 80
                
            levels = levels + 1
            
        #Instructions Button
        InstructionsButton = screen.create_rectangle(525, 550, 725, 600, fill = "white", width = 4)
        InstructionsText =  screen.create_text(625, 575, text = "Instructions", font = "ariel 20")

        #Quit Game Button
        quitButton = screen.create_rectangle(275, 550, 475, 600, fill = "white", width = 4)
        quitText = screen.create_text(375, 575, text = "Quit", font = "ariel 20")
        

        #BUTTON DETECTION
        #Checks if user selected a level                     
        for i in range(20):
            if xMouse > x1[i] and xMouse < (x1[i]+40) and yMouse > y1[i] and yMouse < (y1[i]+40):
                introScreen = False
                numTurtles = numTurtle[i]
                numRocks = numRock[i]

            
            
        #Checks if user selected instructions
        if xMouse > 525 and xMouse < 725 and yMouse > 550 and yMouse < 600:
            introScreen = False
            Instructions = True
        
        #Checks if user quit game
        if xMouse > 275 and xMouse < 475 and yMouse > 550 and yMouse < 600:
            root.destroy()
                
        screen.update()
        sleep(0.03)
        for i in range(20):
            screen.delete(LevelsButtons[i], LevelsText[i])
        screen.delete(Title, Levels, InstructionsButton, InstructionsText, quitButton, quitText)    
    if Instructions == True:
        instructions()

    else:
        runGame()
        
#Uses displays 
def instructions():
    global framNum,frameNum,d,e,f,g,j,k
    setInitialValues()
    Instructions = True
    turtleGIF = turtleGIF3
    
    #Arrow Key Values
    arrowKeyGIF = []
    for i in range(4):
        frameText = "gif -index " + str(i)
        image = PhotoImage(file = "arrowKeys.gif", format = frameText)
        arrowKeyGIF.append(image)

    #BoatValues
    x = 600
    y = 525
    X = 150
    Xspeed = 2
    boatDirection = boatGIFE
    boatCrash = False
    boatDrawing1 = 0
    boatDrawing2 = 0

    
    while Instructions == True:
        #Calculates franme number
        framNum = framNum + 1
        frameNum = frameNum + 1
        
        #Title
        instructionsTitle = screen.create_text(500, 100, text = "Instructions", font = "ariel 40")

        #Subtitles
        Movement = screen.create_text(250, 250, text = "Move the boat using the arrow keys", font = "ariel 20")
        TurtleSave = screen.create_text(750, 250, text = "Save the turtles by removing the harmful plastic", font = "ariel 20")
        AvoidRocks = screen.create_text(250, 450, text = "Avoid rocks to prevent the boat from breaking", font = "ariel 20")
        ChargeBoat = screen.create_text(750, 450, text = "Don't forget to recharge the boat's battery", font = "ariel 20")
        
        #Arrow Key Display
        ArrowKeyUp = screen.create_image(250,300, anchor = CENTER, image = arrowKeyGIF[0])
        ArrowKeyDown = screen.create_image(250,350, anchor = CENTER, image = arrowKeyGIF[2])
        ArrowKeyLeft = screen.create_image(200,350, anchor = CENTER, image = arrowKeyGIF[1])
        ArrowKeyRight = screen.create_image(300,350, anchor = CENTER, image = arrowKeyGIF[3])

        #Turtle Display
        TurtleDrawing = screen.create_image(800, 325, anchor = CENTER, image = turtleGIF[f])
        if framNum % 17 == 0:
            if f == 5:
                f = 0
                
            else:
                f = f + 1
                
        #Boat Display
            
        if framNum % 150 == 0:
            d = d + 1

        if framNum % 50 == 25:
            d = d + 1

        if framNum % 50 == 0:
            d = d - 1

        if d > 3:
            d = 0

        if x > 775:
            turtleGIF = turtleGIF4
            
        if x > 875:
            x = 600
            turtleGIF = turtleGIF3 

        x = x + 2
        
        boatDrawing = screen.create_image(x, 325, anchor = CENTER, image = boatDirection[d])

        #Avoid Rocks Display
        Rock = screen.create_image(300,525, anchor = CENTER, image = RockGIFarray[0])
        
        distanceFromRock = CalculateDistance(X,525,300,525)
        if distanceFromRock < 55:
            boatCrash = True

        else:
            boatCrash = False
            j = 0
            k = 0
            Xspeed = 2

        if boatCrash == True:
            if distanceFromRock < 5:
                Xspeed = 0
                if k == 25:
                    X = 150
                    BoatCrash = False

                else:
                    k = k + 1
            else:
                Xspeed = 1

         
        X = X + Xspeed

        if boatCrash == True:
            boatDrawing1 = screen.create_image(X, y, anchor = CENTER, image = boatCrashGIFE[j])

            if framNum % 7 == 0:
                if j == 7:
                    j = 7  
                else:
                    j = j + 1

        elif boatCrash == False:
            boatDrawing1 = screen.create_image(X, 525, anchor = CENTER, image = boatDirection[d])

        #Boat Charging Display
        if (x > 775 and x < 825) and (y > 500 and y < 550):
            e = 0
            frameNum = 0
                    
        if frameNum % 150 == 0:
            e = e + 1

        if frameNum % 50 == 25:
            e = e + 1

        if frameNum % 50 == 0:
            e = e - 1

        if e > 3:
            e = 0

        if framNum % 25 == 0:
            if g == 1:
                g = 0

            else:
                g = g + 1
        boatChargerDrawing = screen.create_image(800, 525, anchor = CENTER, image = boatChargerGIF[g])
        boatDrawing2 = screen.create_image(x, 525, anchor = CENTER, image = boatDirection[e])

        #BUTTONS
        #Back Button
        backButton = screen.create_rectangle(50, 700, 150, 750, fill = "white", width = 4)
        backText = screen.create_text(100, 725, text = "Back", font = "ariel 20")

        #BUTTON DETECTION
        if xMouse > 50 and xMouse < 150 and yMouse > 700 and yMouse < 750:
            Instructions = False

        screen.update()
        sleep(0.03)
        screen.delete(instructionsTitle,backButton,backText,ArrowKeyUp,ArrowKeyDown,ArrowKeyLeft,ArrowKeyRight,Movement,boatDrawing,TurtleDrawing,TurtleSave,AvoidRocks,boatDrawing1,Rock,ChargeBoat)
        screen.delete(boatDrawing2,boatChargerDrawing)

    introScreen()


#Checks for any mouse clicks throughout the game 
def mouseClickHandler(event):
    global xMouse, yMouse

    xMouse = event.x
    yMouse = event.y


#Checks for any key clicks throughout the game
def keyDownHandler(event):
    global userQuit, gameRunning, directions

    #Checks if user pressed q and ends the game
    if event.keysym == "q" or event.keysym == "Q":
        userQuit = True
        gameRunning = False

    #Checks if user pressed arrow keys and adds them to an array
    if event.keysym == "Left":
        directions.append("W")

    elif event.keysym == "Right":
        directions.append("E")
        
    elif event.keysym == "Down":
        directions.append("S")

    elif event.keysym == "Up":
        directions.append("N")


#Checks for any key releases throughout the game
def keyUpHandler(event):
    global directions

    #Checks if user released arrow keys and removes them from the array   
    if event.keysym == "Left":
        directions.remove("W")

    elif event.keysym == "Right":
        directions.remove("E")
        
    elif event.keysym == "Down":
        directions.remove("S")

    elif event.keysym == "Up":
        directions.remove("N")

#Calculates the distance between two given objects
def CalculateDistance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


#Updates the position of objects
def updateObjects():
    global xWave, yWave, xTurtle, yTurtle, xTurtleSpeed, yTurtleSpeed, dieRoll, xBoat, yBoat, xRedHealthBar, yRedHealthBar, xGreenHealthBar, yGreenHealthBar, xGreenHealthBarSize, turtleDead
    global DeadTurtles, boatDirection, xBoatSpeed, yBoatSpeed, gameRunning, h, boatCrashGIF, k, l

    #Updates wave position
    for i in range(numWaves):
        xWave[i] = xWave[i] + waveSpeed[i]

        if xWave[i] > 1002:
            xWave[i] = -11

    
    #UPDATES BOAT POSITION
    #Returns boat to charger once all the turtles are saved or dead
    if turtlesSaved + DeadTurtles == numTurtles:
            
        distanceFromBoatCharger = CalculateDistance(500,400,xBoat,yBoat)
        xBoatSpeed = (500 - xBoat)*4 / distanceFromBoatCharger
        yBoatSpeed = (400 - yBoat)*4 / distanceFromBoatCharger
        if yBoatSpeed > 0:
            boatDirection = boatGIFS
        
        elif yBoatSpeed < 0:
            boatDirection= boatGIFN

        if xBoat > 498 and xBoat < 502 and yBoat > 398 and yBoat < 402:
            xBoatSpeed = 0
            yBoatSpeed = 0
            h = h + 1
            boatDirection= boatGIFN

            if h == 25:
                gameRunning = False

    #Drags boat to the center of the rock it crashed 
    elif boatCrash == True: 
        distanceFromRock = CalculateDistance(xCrashRock, yCrashRock, xBoat,yBoat)
        xBoatSpeed = (xCrashRock - xBoat)*2 / distanceFromRock
        yBoatSpeed = (yCrashRock - yBoat)*2 / distanceFromRock
        if distanceFromRock < 5:
            xBoatSpeed = 0
            yBoatSpeed = 0

            if k == 45:
                gameRunning = False

            else:
                k = k + 1 

    #Changes the direction of the boat based on the directions in an array that come from the arrow keys the user selects
    else:
        if list(directions) == ['W']:
            xBoatSpeed = -s
            yBoatSpeed = 0
            boatDirection = boatGIFW
            boatCrashGIF = boatCrashGIFW

        elif list(directions) == ['E']:
            xBoatSpeed = s
            yBoatSpeed = 0
            boatDirection = boatGIFE
            boatCrashGIF = boatCrashGIFE
            
        elif list(directions) == ['S']:
            xBoatSpeed = 0
            yBoatSpeed = s
            boatDirection = boatGIFS
            boatCrashGIF = boatCrashGIFS

        elif list(directions) == ['N']:
            xBoatSpeed = 0
            yBoatSpeed = -s
            boatDirection = boatGIFN
            boatCrashGIF = boatCrashGIFN

        elif list(directions) == ['N', 'E'] or list(directions) == ['E', 'N']:
            xBoatSpeed = s
            yBoatSpeed = -s

        elif list(directions) == ['N', 'W'] or list(directions) == ['W', 'N']:
            xBoatSpeed = -s
            yBoatSpeed = -s

        elif list(directions) == ['S', 'E'] or list(directions) == ['E', 'S']:
            xBoatSpeed = s
            yBoatSpeed = s

        elif list(directions) == ['S', 'W'] or list(directions) == ['W', 'S']:
            xBoatSpeed = -s
            yBoatSpeed = s

        else:
            xBoatSpeed = 0
            yBoatSpeed = 0

    xBoat = xBoat + xBoatSpeed
    yBoat = yBoat + yBoatSpeed

    #Ensures the boat can not leave the screen
    if xBoat - 25 < 0:
        xBoat = 25

    elif xBoat + 20 > 1000:
        xBoat = 980

    elif yBoat - 25 < 0:
        yBoat = 25

    elif yBoat + 50 > 800:
        yBoat = 750
        


    #UPDATES TURTLES POSITION
    turtleUnderRock = False

    #Sets values for each turtle
    for i in range(numTurtles):
        dieRoll[i] = randint(1, 50)

    for i in range(numTurtles):
        if turtleSaved[i] == False and turtleDead[i] == False:
            #Calculates the turtles distance from the boat
            distanceFromBoat = CalculateDistance(xBoat,yBoat,xTurtle[i],yTurtle[i])

            #Checks if the turtle is under a rock
            for l in range(numRocks):
                distanceFromRock = CalculateDistance(xRock[l],yRock[l],xTurtle[i],yTurtle[i])
                if distanceFromRock < 40:
                    turtleUnderRock = 0
                    break

                elif distanceFromRock < 50 and distanceFromRock > 40:
                    turtleUnderRock = 1
                    break

                else:
                    turtleUnderRock = 2

            #If the turtle is under a rock its speed is increased so that it is visible, savable, and not stuck under a rock
            if turtleUnderRock == 0:
                xTurtleSpeed[i] = (xBoat - xTurtle[i])*4 / distanceFromBoat
                yTurtleSpeed[i] = (yBoat - yTurtle[i])*4 / distanceFromBoat

            #If turtle was under a rock and now is on the other side the speed goes back to normal
            elif turtleUnderRock == 1:
                xTurtleSpeed[i] = (xBoat - xTurtle[i])*0.1 / distanceFromBoat
                yTurtleSpeed[i] = (yBoat - yTurtle[i])*0.1 / distanceFromBoat
            
            elif turtleUnderRock == 2:
                #If the turtle is not under the rock and the number assigned to the turtle is 1 then the turtle moves towards the boat 
                if dieRoll[i] == 1:
                    xTurtleSpeed[i] = (xBoat - xTurtle[i])*0.1 / distanceFromBoat
                    yTurtleSpeed[i] = (yBoat - yTurtle[i])*0.1 / distanceFromBoat

                    #If turtles health is empty the turtle is set to dead
                    if (xGreenHealthBar[i] + xGreenHealthBarSize[i]) <= xGreenHealthBar[i]:
                        turtleDead[i] = True
                        DeadTurtles = DeadTurtles + 1
        
                        xGreenHealthBarSize[i] = 50
                    
                    #If the turtle moves its health goes down by 1.75
                    elif turtleDead[i] == False and turtleSaved[i] == False:
                        xGreenHealthBarSize[i] = xGreenHealthBarSize[i] - 1.75

            #Changes position of the turtle based on if the speed was changed
            xTurtle[i] = xTurtle[i] + xTurtleSpeed[i]
            yTurtle[i] = yTurtle[i] + yTurtleSpeed[i]
            xRedHealthBar[i] = xRedHealthBar[i] + xTurtleSpeed[i]
            yRedHealthBar[i] = yRedHealthBar[i] + yTurtleSpeed[i]
            xGreenHealthBar[i] = xGreenHealthBar[i] + xTurtleSpeed[i]
            yGreenHealthBar[i] = yGreenHealthBar[i] + yTurtleSpeed[i]
                    
        #If turtle is saved the health of the turtle is restored and the turtle swims away
        elif turtleSaved[i] == True:
            xGreenHealthBarSize[i] = 50
            xTurtle[i] = xTurtle[i] + DIR[i]
            yTurtle[i] =  yTurtle[i] + DIR[i]
            xRedHealthBar[i] = xRedHealthBar[i] + DIR[i]
            yRedHealthBar[i] = yRedHealthBar[i] + DIR[i]
            xGreenHealthBar[i] = xGreenHealthBar[i] + DIR[i]
            yGreenHealthBar[i] = yGreenHealthBar[i] + DIR[i]


#Draws the objects in the game
def drawObjects():
    global wave, turtleDrawing, boatDrawing, redHealthBar, greenHealthBar, xGreenHealthBarSize, a, b, c, d, boatChargerDrawing, f, Rock,j

    #Draws the waves
    for i in range(numWaves):
        wave[i] = screen.create_line(xWave[i], yWave[i], xWave[i] + waveSize[i], yWave[i], fill = "black")

    #DRAWS THE TURTLES
    for i in range(numTurtles):
        #If turtle is saved then draws turtle without plastic
        if turtleSaved[i] == True:
            turtleDrawing[i] = screen.create_image(xTurtle[i], yTurtle[i], anchor = CENTER, image = turtleGIF4[f])
            if frameNum % 17 == 0:
                if f == 5:
                    f = 0
                    
                else:
                  f = f + 1

        #Draws the turtle based on what kind of plastic it is harmed by and if they have died or not
        elif turtleGIF[i] == turtleGIF1:
            if turtleDead[i] == True:
                turtleDrawing[i] = screen.create_image(xTurtle[i], yTurtle[i], anchor = CENTER, image = turtleGIF1Dead)
                
            else:
                turtleDrawing[i] = screen.create_image(xTurtle[i], yTurtle[i], anchor = CENTER, image = turtleGIF1[a])

                if frameNum % 17 == 0:
                    if a == 5:
                        a = 0
                        
                    else:
                        a = a + 1

        elif turtleGIF[i] == turtleGIF2:
            if turtleDead[i] == True:
                turtleDrawing[i] = screen.create_image(xTurtle[i], yTurtle[i], anchor = CENTER, image = turtleGIF2Dead)
                
            else:
                turtleDrawing[i] = screen.create_image(xTurtle[i], yTurtle[i], anchor = CENTER, image = turtleGIF2[b])
                if frameNum % 17 == 0:
                    if b == 5:
                        b = 0
                        
                    else:
                        b = b + 1
            
        elif turtleGIF[i] == turtleGIF3:
            if turtleDead[i] == True:
                turtleDrawing[i] = screen.create_image(xTurtle[i], yTurtle[i], anchor = CENTER, image = turtleGIF3Dead)
                
            else:
                turtleDrawing[i] = screen.create_image(xTurtle[i], yTurtle[i], anchor = CENTER, image = turtleGIF3[c])
                if frameNum % 17 == 0:
                    if c == 5:
                        c = 0
                        
                    else:
                        c = c + 1

        if turtleDead[i] == False:
            #Draws the health bar of the turtle 
            redHealthBar[i] = screen.create_rectangle( xRedHealthBar[i], yRedHealthBar[i], xRedHealthBar[i]+ 50, yRedHealthBar[i]-5, fill = "red")                                       
            greenHealthBar[i] = screen.create_rectangle( xGreenHealthBar[i], yGreenHealthBar[i], xGreenHealthBar[i] + xGreenHealthBarSize[i], yGreenHealthBar[i]-5, fill = "lightgreen")

    #Draws the rocks
    for i in range(numRocks):
        Rock[i] = screen.create_image(xRock[i],yRock[i], anchor = CENTER, image = RockGIF[i])

    #Draws boat charger
    boatChargerDrawing = screen.create_image(500, 400, anchor = CENTER, image = boatChargerGIF[e])

    #DRAWS BOAT
    #Draws boat crash
    if boatCrash == True:
        boatDrawing = screen.create_image(xBoat, yBoat, anchor = CENTER, image = boatCrashGIF[j])
        if frameNum % 5 == 0:
            if j == 7:
                j = 7  
            else:
                j = j + 1

    #Draws boat if it has not crashed
    else:
        boatDrawing = screen.create_image(xBoat, yBoat, anchor = CENTER, image = boatDirection[d])

    
#Checks if turtle has been saved by the boat
def turtleDetection():
    global turtleSaved, turtlesSaved, turtleDrawing, gameRunning

    for i in range(numTurtles):
        #Calculates distance fron boat to turtle
        distanceFromBoat = CalculateDistance(xBoat,yBoat,xTurtle[i],yTurtle[i])
        #If the distance from the turtle to the boat is less then 45 and the turtle is not yet dead or saved then the turtle is saved
        if distanceFromBoat < (45) and turtleSaved[i] == False and turtleDead[i] == False:
            turtleSaved[i] = True
            turtlesSaved = turtlesSaved + 1


#Checks if the boat hit a rock
def rockDetection():
    global boatCrash, gameRunning,  xCrashRock, yCrashRock,batteryEmpty

    #Ensures the boat isn't set to crash once it returns to the boat charger at the end of the game
    if (turtlesSaved + DeadTurtles) < numTurtles:
        for i in range(numRocks):
            #Calculates the distance from the boat to the rock
            distanceFromBoat = CalculateDistance(xBoat,yBoat,xRock[i],yRock[i])
            #if the boat hits the rock it sets boat crash to true
            if distanceFromBoat < 55:
                boatCrash = True
                batteryEmpty = False
                xCrashRock = xRock[i]
                yCrashRock = yRock[i]


#Draws game statistics at the top right corner of the screen
def gameStatistics():
    global Statistics 
    Statistics = screen.create_text(870,20, text = "Dead Turtles: " + str(DeadTurtles) + "    Turtles Saved: " + str(turtlesSaved), font = "ariel 15" )
    

#Runs the game using all the functions
def runGame():
    global frameNum, framNum, d, e, gameRunning, batteryEmpty
    #Calls function to set the initial values of the game
    setInitialValues()

    #A while loop that continuously runs until somethign causes the game to end
    while gameRunning == True:
        #Calculates frame number of the game
        frameNum = frameNum + 1
        framNum = framNum + 1

        #If the boat is on the charger it will reload its battery
        if (xBoat > 475 and xBoat < 525) and (yBoat > 375 and yBoat < 425):
            batteryEmpty = False
            d = 0
            framNum = 0

        #Makes battery flash and ends game if the battery dies
        elif batteryEmpty == False:
            if framNum % 150 == 0:
                d = d + 1

            if framNum % 50 == 25:
                d = d + 1

            if framNum % 50 == 0:
                d = d - 1

            if d > 3:
                if ((turtlesSaved + DeadTurtles) < numTurtles):
                    batteryEmpty = True
                    gameRunning = False
                    d = 3

                else:
                    d = 2

        #Makes the red lights on the boat charger blink
        if frameNum % 25 == 0:
            if e == 1:
                e = 0

            else:
                e = e + 1

        #Calls function to draw objects and statistics in the game
        drawObjects()
        gameStatistics()

        #updates the screen, sleeps, and deletes all the previous drawings to create an animated game using graphics
        screen.update()
        sleep(0.03)
        screen.delete(boatDrawing, boatChargerDrawing, Statistics, Rock)

        for i in range(numRocks):
            screen.delete(Rock[i])
        
        for i in range(numWaves):
            screen.delete(wave[i])
            
        for i in range(numTurtles):
            screen.delete(turtleDrawing[i],redHealthBar[i],greenHealthBar[i])

        #checks if any turtles were saved
        turtleDetection()
        
        #updates position of the objects in the game
        updateObjects()

        #Checks if the boat hit a rock
        rockDetection()

    #calls the end game function if the game ends
    endGame()
    

#Function that shows a screen showing the game has ended 
def endGame():
    global gameRunning, numTurtles, Level, numRocks
    endGame = True
    n = 0

    #Deletes all objects before creating the end game screen
    screen.delete(boatDrawing, boatChargerDrawing, Statistics)

    for i in range(numRocks):
        screen.delete(Rock[i])
    
    for i in range(numWaves):
        screen.delete(wave[i])
        
    for i in range(numTurtles):
        screen.delete(turtleDrawing[i],redHealthBar[i],greenHealthBar[i])

    #while loop that end if something causes the program to leave the end game screen
    while endGame == True:

        #TITLES AND SUBTITLES
        #Level title
        LevelText = screen.create_text(500, 125, text = "Level " + str(int(level)), font = "ariel 80")

        #Subtitle based on why the game ended 
        if turtlesSaved == numTurtles:
            text = screen.create_text(500, 300, text = "Congratulations, You saved all the turtles! \u263A", font = "ariel 40")

        elif batteryEmpty == True:
            text = screen.create_text(500, 300, text = "Game Over! Your battery died \u2639", font = "ariel 40")

        elif boatCrash == True:
            text = screen.create_text(500, 300, text = "Game Over! Boat crashed \u2639", font = "ariel 40")
            
        else:
            text = screen.create_text(500, 300, text = "Game Over!", font = "ariel 40")

        #Shows final statistics of the game
        if batteryEmpty == True or userQuit == True or boatCrash == True:
            statistics = screen.create_text(500, 400, text = "Dead Turtles: " + str(DeadTurtles) + "    Turtles Saved: " + str(turtlesSaved) + "    Endangered Turtles: " + str(numTurtles-(turtlesSaved+DeadTurtles)), font = "ariel 20" )
            
        else:
            statistics = screen.create_text(500, 400, text = "Dead Turtles: " + str(DeadTurtles) + "    Turtles Saved: " + str(turtlesSaved), font = "ariel 20")

        #BUTTONS
        #Replay button
        replayButton = screen.create_rectangle(400, 450, 600, 500, fill = "white", width = 4)
        replayText = screen.create_text(500, 475, text = "Replay", font = "ariel 20")

        #Menu button
        MENUButton = screen.create_rectangle(400, 525, 600, 575, fill = "white", width = 4)
        MENUText = screen.create_text(500, 550, text = "Main Menu", font = "ariel 20")

        #Next Button that only appears before level 20
        if level < 20:
            NextButton = screen.create_rectangle(775, 700, 975, 750, fill = "white", width = 4)
            NextText = screen.create_text(875, 725, text = "Next", font = "ariel 20")

        #Back button that only appears after level 1
        if level > 1:
            BackButton = screen.create_rectangle(25, 700, 225, 750, fill = "white", width = 4)
            BackText = screen.create_text(125, 725, text = "Back", font = "ariel 20")

        #Updates the screen and deletes the objects
        screen.update()
        screen.delete(text,replayButton,replayText,statistics,MENUButton,MENUText,LevelText)

        if level < 20:
            screen.delete(NextButton,NextText)

        if level > 1:
            screen.delete(BackButton,BackText)

        #If the user selects the replay button it replays the game that the user last played
        if xMouse > 400 and xMouse < 600 and yMouse > 450 and yMouse < 500:
            gameRunning = True
            endGame = False

        #If user selected the Main menu button it brings them to the intro screen of the game
        if xMouse > 400 and xMouse < 600 and yMouse > 525 and yMouse < 575:
            endGame = False

        #If the user selected next button it plays the next level
        if level < 20:
            if xMouse > 775 and xMouse < 975 and yMouse > 700 and yMouse < 750:
                if level % 3 == 0:
                    numRocks = numRocks + 1
                numTurtles = numTurtles+2
                gameRunning = True
                endGame = False

        #If the user selected the back button it plays the previous level
        if level > 1:
            if xMouse > 25 and xMouse < 225 and yMouse > 700 and yMouse < 750:
                if level % 3 == 0:
                    numRocks = numRocks - 1
                numTurtles = numTurtles-2
                gameRunning = True
                endGame = False

    if gameRunning == True:
        runGame()

    else:
        introScreen()


root.after(0, introScreen)

#Checks for mouse clicks or key presses/releases while the program is running
screen.bind("<Button-1>", mouseClickHandler)
screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)

screen.pack()
screen.focus_set()
root.mainloop()

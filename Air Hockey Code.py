import module_manager
module_manager.review()

# CITATION: from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
from cmu_112_graphics import *

import math, random, time

# CITATION: from https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNoeZ6iQhp0nxH5pNRG6iXjE6-7Uhx9GEEMw&usqp=CAU
# Used for homescreen image; colors are inverted
def appStarted(app):
    url = 'ah.png'
    app.image = app.loadImage(url)        
    app.image2 = app.scaleImage(app.image, 1/3)

    app.homescreen = True
    app.margin = 20
    app.maze = False
    app.regular = False
    app.paused = False

    app.open = []

    app.goal = (9,9)
    app.countdown = 20
    app.seconds = 20

    app.createMode = False
    app.randomMazeMode = False
    app.moveGoalMode = True
    app.customMode = False

    app.level = None

    app.coordinates = []

    app.regularOptions = False
    app.pittMode = False
    app.bouncerMode = False
    app.placePitt = False
    app.placeBouncer = False

def randomMaze(app):
    if app.randomMazeMode == True:
        app.yourScore = 0
        app.margin = 50
        app.puckX = 95
        app.puckY = 65
        app.puckDx = 1
        app.puckDy = 1
        app.puckRadius = 7
        app.controllerX = 65
        app.controllerY = 65
        app.controllerRadius = 10
        app.timerDelay = 10
        app.rows = 10
        app.cols = 10

        app.win = False
        app.lose = False

        app.started = False

        app.open = []

        app.goal = (9,9)
        app.countdown = 20
        app.seconds = 20

        app.createMode = False
        app.randomMazeMode = True
        app.moveGoalMode = True

        app.paused = False

        app.coordinates = []

        app.homescreen = False

        app.maze = False


        app.paused = False
        startRow = 0
        endRow = app.rows - 1
        open = []
        directions = [-1, +1]
        lenWall = [2,3,4,5]
        xy = ["x","y"]
        numWalls = 0
        if app.level == "easy":
            walls = 3
        elif app.level == "medium":
            walls = 5
        elif app.level == "hard":
            walls = 7
        while numWalls<walls:
            selectLen = random.randint(0,3)
            selectLen = lenWall[selectLen]
            col = random.randint(0,app.rows-1)
            row = random.randint(0,app.rows-1)
            wall = [(row,col)]
            selectDir = random.randint(0,1)
            selectDir = directions[selectDir]
            selectxy = random.randint(0,1)
            selectxy = xy[selectxy]
            lenCurWall = len(wall)
            lastx = wall[lenCurWall - 1][0]
            lasty = wall[lenCurWall - 1][1]
            if (row,col) in app.open or (row,col)==(app.rows-1,app.rows-1) or (row,col)==(0,0) or (row,col)==(0,1):
                continue
            for place in range(selectLen-1):
                if selectxy == "x":
                    newx = lastx + selectDir
                    if newx>= 0 and newx<app.rows:
                        if (newx,col) in app.open or (newx,col) in wall: break
                        if (newx,col) != (app.rows-1,app.rows-1) and (newx,col)!=(0,0) and (newx,col)!=(0,1):
                            wall.append((newx,col))
                            lastx = newx
                            continue
                elif selectxy == "y":
                    newy = lasty + selectDir
                    if newy>= 0 and newy<app.rows:
                        if (row,newy) in app.open or (row,newy) in wall: 
                            wall = []
                            break
                        if (row,newy) != (app.rows-1,app.rows-1) and (row,newy)!=(0,0) and (row,newy)!=(0,1):
                            wall.append((row,newy))
                            lasty = newy
                            continue
                else: 
                    wall = []
                    break
            numWalls += 1
            app.open.append(wall)
    
        app.open = oneDList(app.open)
        maze = app.open
        app.coordinates = []
        for box in app.open:
            row, col = box
            coord = getCellBounds(app,row,col)
            app.coordinates.append(coord)
        app.coordinates = coordOneDList(app.coordinates)
        app.startGoal = time.time()
        app.begin = time.time()
        app.started = True
        return app.open


def coordOneDList(L):
    newL = []
    for box in L:
        newL.append((box[:2]))
        newL.append((box[2:]))
    return newL

def oneDList(L):
    newL = []
    for wall in L:
        for elem in wall:
            newL.append((elem))
    return newL


def creativeMaze(app):
    if app.customMode == True:
        app.yourScore = 0
        app.margin = 50
        app.puckX = 95
        app.puckY = 65
        app.puckDx = 1
        app.puckDy = 1
        app.puckRadius = 7
        app.controllerX = 65
        app.controllerY = 65
        app.controllerRadius = 10
        app.timerDelay = 10
        app.rows = 10
        app.cols = 10

        app.win = False
        app.lose = False

        app.started = False

        app.open = []

        app.goal = (9,9)
        app.countdown = 20
        app.seconds = 20

        app.createMode = True
        app.randomMazeMode = False
        app.moveGoalMode = True

        app.paused = True
        app.level = None

        app.coordinates = []

        app.homescreen = False

        app.maze = False

        if app.createMode == False:
            app.paused = True
            app.begin = None
            app.startGoal = None

def regularHockey(app):
    if app.regular == True and app.regularOptions == False:
        if app.placePitt == True or app.placeBouncer == True:
            app.paused = True
        if app.placePitt == False and app.placeBouncer == False:
            app.paused = False
        if app.placePitt == True:
            app.pittX = 120
            app.pittY = 240
            app.pittRadius = 20
        if app.placeBouncer == True:
            app.bouncerX = 120
            app.bouncerY = 140
            app.bouncerRadius = 15
        app.margin = 20
        app.yourScore = 0
        app.computerScore = 0
        app.puckX = app.width//2
        app.puckY = app.height//2
        app.puckDx = 1
        app.puckDy = 1
        app.puckRadius = 10
        app.controllerX = app.width//2
        app.controllerY = app.height-app.height//4
        app.controllerRadius = 15
        app.computerX = app.width//2
        app.computerY = app.height//4
        app.computerDx = 3
        app.computerDy = 1
        app.computerRadius = 15
        app.timerDelay = 10
        app.hits = 0
        app.justhit = False
        app.intercept = 0
        app.wallhits = 0
        app.collides = 0
        app.youWin = False
        app.computerWin = False

def mazeMoveControllerLegally(app, x, y):
    locX, locY = getCell(app,x,y)
    if (locX, locY) not in app.open:
        if moveControllerMaze(app,x,y):
            if x-app.controllerRadius>app.margin:
                if x+app.controllerRadius<=app.width-app.margin:
                    if y+app.controllerRadius<=app.height-app.margin:
                        if y-app.controllerRadius>=app.margin:
                            return True

def moveControllerMaze(app,x,y):
    rightX, rightY = getCell(app,x+app.controllerRadius,y)
    leftX, leftY = getCell(app,x-app.controllerRadius,y)
    upX, upY = getCell(app,x,y-app.controllerRadius)
    downX, downY = getCell(app,x,y+app.controllerRadius)
    if (rightX, rightY) not in app.open:
        if (leftX, leftY) not in app.open:
            if (upX, upY) not in app.open:
                if (downX, downY) not in app.open:
                    return True

def mazeCorner(app):
    for coord in app.coordinates:
        boxX, boxY = coord
        distance = hypotenuse(app,app.puckX - boxX, app.puckY - boxY)
        if app.puckX == boxX:
            if abs(app.puckY - boxY) <= app.puckRadius: 
                return "Hit Up or Down Edge"
        if app.puckY == boxY:
            if abs(app.puckX - boxX) <= app.puckRadius: 
                return "Hit Left or Right Edge"
        if distance <= app.puckRadius:
            print("corner")
            return "Corner"
    return True

def hypotenuse(app, x, y):
    hypotenuse = (x**2 + y**2)**0.5
    return hypotenuse 

def mazeMovePuckLegally(app, x, y):
    rightX, rightY = getCell(app,(app.puckX+app.puckRadius),app.puckY)
    leftX, leftY = getCell(app,(app.puckX-app.puckRadius),app.puckY)
    upX, upY = getCell(app,app.puckX,(app.puckY-app.puckRadius))
    downX, downY = getCell(app,app.puckX,(app.puckY+app.puckRadius))

    if x-app.puckRadius>app.margin:
        if x+app.puckRadius<=app.width-app.margin:
            if y+app.puckRadius<=app.height-app.margin:
                if y-app.puckRadius>app.margin:
                    if (rightX, rightY) in app.open or (leftX, leftY) in app.open:
                        return "Hit Left or Right Edge"
                    if (upX, upY) in app.open or (downX, downY) in app.open:
                        return "Hit Up or Down Edge"
                    return True
    if x-app.puckRadius<app.margin or x+app.puckRadius>app.width-app.margin:
        return "Hit Left or Right Edge"
    if y+app.puckRadius<=app.height-app.margin or y-app.puckRadius>app.margin:
        return "Hit Up or Down Edge"

def mazeWin(app):
    locx, locy = getCell(app,app.puckX,app.puckY)
    if (locx, locy) == app.goal:
        app.win = True
        app.paused = True
    
def goalScored(app):
    if (app.width//2 - 40) < app.puckX < (app.width//2 + 40):
        if app.margin < app.puckY < (app.margin + 40):
            app.yourScore += 1
            return True

def countdown(app):
    now = time.time()
    if now-app.begin >= 1:
        app.seconds -= 1
        app.begin = time.time()
    if app.seconds == 0:
        app.paused = True
        app.lose = True




def moveControllerLegally(app, x, y):
    if x-app.controllerRadius>app.margin:
        if x+app.controllerRadius<=app.width-app.margin:
            if y+app.controllerRadius<=app.height-app.margin:
                if y-app.controllerRadius>app.height//2:
                    return True

def movePuckLegally(app, x, y):
    if x-app.puckRadius>app.margin:
        if x+app.puckRadius<=app.width-app.margin:
            if y+app.puckRadius<=app.height-app.margin:
                if y-app.puckRadius>app.margin:
                    return True
    if x-app.puckRadius<app.margin or x+app.puckRadius>app.width-app.margin:
        if app.puckY < app.height//2:
            app.hits += 1
        return "Hit Left or Right Edge"
    if y+app.puckRadius<=app.height-app.margin or y-app.puckRadius>app.margin:
        if app.puckY < app.height//2:
            app.hits += 1
        return "Hit Up or Down Edge"

def goalScored(app):
    if (app.width//2 - 40) < app.puckX < (app.width//2 + 40):
        if app.margin < app.puckY < (app.margin + 40):
            app.yourScore += 1
            return True
    if (app.width//2 - 40) < app.puckX < (app.width//2 + 40):
        if (app.height-app.margin-40) < app.puckY < (app.height-app.margin):
            app.computerScore += 1
            return True

def computerCanPlay(app):
    if app.puckY < app.height//2 and app.intercept == 0 and app.justhit == False:
        return True

def moveComputerControllerLegally(app, x, y):
    if x-app.computerRadius>app.margin:
        if x+app.computerRadius<=app.width-app.margin:
            if y-app.computerRadius>=app.margin:
                if y-app.computerRadius<app.height//2:
                    if not computerPuckInterception(app, app.puckX, app.puckY, app.computerX, app.computerY):
                        return True

def computerPuckInterception(app, puckX, puckY, computerX, computerY):
    if distanceFormula(app, puckX, puckY, computerX, computerY) <= app.computerRadius + app.puckRadius:
        return True

def computerPlays(app):
    if computerCanPlay(app) and app.justhit == False:
        xDistance = app.computerX - app.puckX
        yDistance = app.computerY - app.puckY
        if xDistance<0:
            if yDistance<0:
                if moveComputerControllerLegally(app, app.computerX + app.computerDx, app.computerY + app.computerDy):
                    app.computerX += app.computerDx
                    app.computerY += app.computerDy
                    movePuck(app, app.computerX, app.computerY)
            elif yDistance>0:
                if moveComputerControllerLegally(app, app.computerX + app.computerDx, app.computerY - app.computerDy):
                    app.computerX += app.computerDx
                    app.computerY -= app.computerDy
                    movePuck(app, app.computerX, app.computerY)
        elif xDistance>0:
            if yDistance<0:
                if moveComputerControllerLegally(app, app.computerX - app.computerDx, app.computerY + app.computerDy):
                    app.computerX -= app.computerDx
                    app.computerY += app.computerDy
                    movePuck(app, app.computerX, app.computerY)
            elif yDistance>0:
                if moveComputerControllerLegally(app, app.computerX - app.computerDx, app.computerY - app.computerDy):
                    app.computerX -= app.computerDx
                    app.computerY -= app.computerDy
                    movePuck(app, app.computerX, app.computerY)


def corner(app):
    if app.puckX-app.puckRadius<app.margin or app.puckX+app.puckRadius>app.width-app.margin:
        if app.puckY < app.height//2:
            app.wallhits += 1
    if app.puckY+app.puckRadius<=app.height-app.margin or app.puckY-app.puckRadius>app.margin:
        if app.puckY < app.height//2:
            app.wallhits += 1
    if app.collides > 5:
        app.justhit = True
        if app.puckX >= app.width//2:
            if moveComputerControllerLegally(app, app.computerX - 4*app.computerDx, app.computerY - 4*app.computerDy):
                app.computerX -= 4*app.computerDx
                app.computerY -= 3*app.computerDy
        elif app.puckX < app.width//2:
            if moveComputerControllerLegally(app, app.computerX + 4*app.computerDx, app.computerY - 4*app.computerDy):
                app.computerX += 4*app.computerDx
                app.computerY -= 4*app.computerDy
        else:
            if moveComputerControllerLegally(app, app.computerX - 4*app.computerDx, app.computerY + 4*app.computerDy):
                app.computerX -= 4*app.computerDx
                app.computerY += 4*app.computerDy
        app.collides = 0
        app.justhit = False

def hits(app):
    if app.puckY > app.height//2:
        app.hits = 0
        app.justhit = False
        app.intercept = 0
        app.wallhits = 0
        app.collides = 0


def moveComp(app):
    if app.intercept >= 1 and app.justhit == True:
        if moveComputerControllerLegally(app, app.computerX - app.computerDx, app.computerY - app.computerDy):
            app.computerX -= 0.1*app.computerDx
            app.computerY -= 0.1*app.computerDy
        elif moveComputerControllerLegally(app, app.computerX - app.computerDx, app.computerY + app.computerDy):
            app.computerX -= 0.1*app.computerDx
            app.computerY += 0.1*app.computerDy
        elif moveComputerControllerLegally(app, app.computerX + app.computerDx, app.computerY - app.computerDy):
            app.computerX += 0.1*app.computerDx
            app.computerY -= 0.1*app.computerDy
        if app.hits == 1:
            app.intercept = 0
            app.justhit = False

def timerFired(app):
    if app.paused == False and app.createMode == False and (app.customMode == True or app.randomMazeMode == True):
        if app.moveGoalMode == True:
            moveGoal(app)

        countdown(app)

        if mazeCheckInterception(app, app.controllerX, app.controllerY):
            mazeMovePuck(app, app.controllerX, app.controllerY)
            mazeWin(app)

        mazeWin(app)

        app.puckX += app.puckDx
        app.puckY += app.puckDy


        if mazeCheckInterception(app, app.controllerX, app.controllerY):
            mazeMovePuck(app, app.controllerX, app.controllerY)
            mazeWin(app)
        puckLegal = mazeMovePuckLegally(app, app.puckX, app.puckY)
        if puckLegal == "Hit Up or Down Edge":
            print("ud")
            app.puckDy = -app.puckDy
            app.puckY += app.puckDy
            app.puckX += app.puckDx
            mazeWin(app)
            return
        elif puckLegal == "Hit Left or Right Edge":
            print("lr")
            app.puckDx = -app.puckDx
            app.puckX += app.puckDx
            app.puckY += app.puckDy
            mazeWin(app)
            return

        isCorner = mazeCorner(app)
        if isCorner != True:
            if isCorner == "Corner":
                app.puckDy = -app.puckDy
                app.puckDx = -app.puckDx
                app.puckY += app.puckDy
                app.puckX += app.puckDx
                mazeWin(app)
                return
            if isCorner == "Hit Up or Down Edge":
                app.puckDy = -app.puckDy
                app.puckY += app.puckDy
                mazeWin(app)
                return
            if isCorner == "Hit Left or Right Edge":
                app.puckDx = -app.puckDx
                app.puckX += app.puckDx
                mazeWin(app)
                return


    if app.paused == False and app.regular == True and app.regularOptions == False:
        app.puckX += app.puckDx
        app.puckY += app.puckDy
        computerPlays(app)
        hits(app)
        corner(app)
        moveComp(app)
        win(app)
        if app.pittMode == True:
            pitt(app)
        if app.bouncerMode == True:
            if bouncer(app, app.puckX, app.puckY, app.bouncerX, app.bouncerY):
                movePuck(app, app.bouncerX, app.bouncerY)
        if computerPuckInterception(app, app.puckX, app.puckY, app.computerX, app.computerY):
            app.collides += 1
            app.justhit = True
            app.hits = 0
            app.intercept += 1
            movePuck(app, app.computerX, app.computerY)
        if checkInterception(app, app.controllerX, app.controllerY):
            movePuck(app, app.controllerX, app.controllerY)
        if goalScored(app):
            app.puckX = app.width//2
            app.puckY = app.height//2
            app.puckDx = 1
            app.puckDy = 1
        puckLegal = movePuckLegally(app, app.puckX, app.puckY)
        if puckLegal == "Hit Up or Down Edge":
            app.puckDy = -app.puckDy
            app.puckY += app.puckDy
        if puckLegal == "Hit Left or Right Edge":
            app.puckDx = -app.puckDx
            app.puckX += app.puckDx

def win(app):
    if app.yourScore == 5:
        app.paused = True
        app.youWin = True
    elif app.computerScore == 5:
        app.paused = True
        app.computerWin = True

def mousePressed(app, event):
    if app.homescreen == True:
        if 250<=event.y and event.y<=300:
            if 50<event.x<175:
                app.regularOptions = True
                app.homescreen = False
                app.maze = False
            if 225<event.x<350:
                app.maze = True
                app.homescreen = False
                app.regular = False                

    if app.regular == True and app.regularOptions == False and app.placePitt == False and app.placeBouncer == False:
        if moveControllerLegally(app, event.x, event.y):
            app.controllerX = event.x
            app.controllerY = event.y
            movePuck(app, app.controllerX, app.controllerY)

    if app.regularOptions == True:
        if app.width//2 - app.margin*3<event.x and app.width//2 + app.margin*3>event.x:
            if 150<event.y<170:
                app.regular = True
                app.regularOptions = False
                regularHockey(app)
            if 180<event.y<200:
                app.pittMode = True
                app.regular = True
                app.regularOptions = False
                app.paused = True
                app.placePitt = True
                regularHockey(app)
            if 210<event.y<230:
                app.bouncerMode = True
                app.regular = True
                app.regularOptions = False
                app.paused = True
                app.placeBouncer = True
                regularHockey(app)

    if app.placeBouncer == True:
        if bouncerLegal(app, event.x, event.y):
            app.bouncerX = event.x
            app.bouncerY = event.y
        if event.x>=app.width//2 - 60 and event.x<=app.width//2 + 60:
            if event.y>=app.height-15 and event.y<= app.height-5:
                app.placeBouncer = False
                regularHockey(app)

    if app.placePitt == True:
        if pittLegal(app, event.x, event.y):
            app.pittX = event.x
            app.pittY = event.y
        if event.x>=app.width//2 - 60 and event.x<=app.width//2 + 60:
            if event.y>=app.height-15 and event.y<= app.height-5:
                app.placePitt = False
                regularHockey(app)

    if app.maze == True:
        if app.width//2 - app.margin*3<event.x and app.width//2 + app.margin*3>event.x:
            if 180<event.y<200:
                app.homescreen = False
                app.maze = False
                app.regular = False
                app.randomMazeMode = True
                app.level = "easy"
                randomMaze(app)
            if 210<event.y<230:
                app.homescreen = False
                app.maze = False
                app.regular = False
                app.randomMazeMode = True
                app.level = "medium"
                randomMaze(app)
            if 240<event.y<260:
                app.homescreen = False
                app.maze = False
                app.regular = False
                app.randomMazeMode = True
                app.level = "hard"
                randomMaze(app)
            if 150<event.y<170:
                app.homescreen = False
                app.regular = False
                app.createMode = True
                app.customMode = True
                creativeMaze(app)

    if app.homescreen == False:
        if 5 <= event.x <= 35:
            if app.height-app.margin+5 <= event.y <= app.height-5:
                app.homescreen = True
                app.margin = 20
                app.regular = False
                app.regularOptions = False
                app.maze = False
                app.createMode = False
                app.customMode = False
                app.randomMazeMode = False
                app.pittMode = False
                app.placePitt = False
                app.placeBouncer = False
                app.bouncerMode = False


    if app.randomMazeMode == True:
        if 100 <= event.x <= 300:
            if event.y>=app.height-30 and event.y<= app.height-15:
                randomMaze(app)

    if app.homescreen == False and app.regular == False and app.customMode == True:
        if app.customMode == True and app.started == True and app.createMode == False:
            if mazeMoveControllerLegally(app, event.x, event.y):
                app.controllerX = event.x
                app.controllerY = event.y
                mazeMovePuck(app, app.controllerX, app.controllerY)

        if app.createMode == True and app.maze == False:
            if event.x>=app.width//2 - 60 and event.x<=app.width//2 + 60:
                if event.y>=app.height-30 and event.y<= app.height-15:
                    app.paused = False
                    app.createMode = False
                    app.startGoal = time.time()
                    app.begin = time.time()

            locX, locY = getCell(app,event.x, event.y)
            if (locX,locY) in app.open:
                app.open.remove((locX,locY))
            elif (locX,locY) not in app.open:
                app.open.append((locX,locY))

        


def mouseDragged(app, event):
    if app.regular == False and app.homescreen == False:
        if mazeMoveControllerLegally(app, event.x, event.y):
            app.controllerX = event.x
            app.controllerY = event.y
            mazeMovePuck(app, app.controllerX, app.controllerY)
    if app.regular == True and app.homescreen == False and app.placePitt == False and app.placeBouncer == False:
        if moveControllerLegally(app, event.x, event.y):
            app.controllerX = event.x
            app.controllerY = event.y
            movePuck(app, app.controllerX, app.controllerY)

def keyPressed(app, event):
    if event.key == 'p':
        app.paused = not app.paused

def bouncerLegal(app, x, y):
    if y - app.height//2<app.bouncerRadius:
        return False
    if distanceFormula(app,x,y,app.controllerX,app.controllerY) <= app.bouncerRadius + app.controllerRadius:
        return False
    if x-app.bouncerRadius>app.margin:
        if x+app.bouncerRadius<=app.width-app.margin:
            if y+app.bouncerRadius<=app.height-app.margin:
                if y-app.bouncerRadius>app.margin:
                    return True

def bouncer(app, puckX, puckY, bouncerX, bouncerY):
    if bouncerLegal(app, bouncerX, bouncerY):
        if (distanceFormula(app, puckX, puckY, bouncerX, bouncerY) <= app.puckRadius + app.bouncerRadius):
            return True

def pittLegal(app, x, y):
    if y - app.height//2<app.pittRadius:
        return False
    if distanceFormula(app,x,y,app.controllerX,app.controllerY) <= app.pittRadius + app.controllerRadius:
        return False
    if x-app.pittRadius>app.margin:
        if x+app.pittRadius<=app.width-app.margin:
            if y+app.pittRadius<=app.height-app.margin:
                if y-app.pittRadius>app.margin:
                    return True

def pitt(app):
    if (distanceFormula(app, app.puckX, app.puckY, app.pittX, app.pittY) <= app.puckRadius + app.pittRadius):
        if app.puckY > app.height//2:
            if app.yourScore > 0:
                app.yourScore -= 1
        elif app.puckY < app.height//2:
            if app.computerScore > 0:
                app.computerScore -= 1
        app.puckX = app.width//2
        app.puckY = app.height//2
        app.puckDx = 1
        app.puckDy = 1

def moveGoal(app):
    now = time.time()
    if app.paused == False and app.createMode == False:
        if now - app.startGoal>= 5:
            row = random.randint(0,9)
            col = random.randint(0,9)
            if (row,col) in app.open:
                moveGoal(app)
            else:
                app.goal = (row,col)
                app.startGoal = time.time()

def movePuck(app, x, y):
    if checkInterception(app, x, y):
        xDist = app.puckX - x
        yDist = app.puckY - y
        if yDist == 0:
            if xDist>0:
                app.puckDx = 1
                app.puckDy = 0
            elif xDist<0:
                app.puckDx = -1
                app.puckDy = 0
        elif xDist == 0:
            if yDist<0:
                app.puckDy = -1
                app.puckDx = 0
            elif yDist>0:
                app.puckDy = 1
                app.puckDx = 0
        else:
            app.puckDx = xDist/6
            app.puckDy = yDist/6
        return True

def mazeMovePuck(app, x, y):
    if mazeCheckInterception(app, x, y):
        xDist = app.puckX - x
        yDist = app.puckY - y
        if yDist == 0:
            if xDist>0:
                app.puckDx = 1
                app.puckDy = 0
            elif xDist<0:
                app.puckDx = -1
                app.puckDy = 0
        elif xDist == 0:
            if yDist<0:
                app.puckDy = -1
                app.puckDx = 0
            elif yDist>0:
                app.puckDy = 1
                app.puckDx = 0
        else:
            app.puckDx = xDist/6
            app.puckDy = yDist/6
        return True

def distanceFormula(app, x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def checkInterception(app, x, y):
    if distanceFormula(app, x, y, app.puckX, 
    app.puckY) <= app.controllerRadius + app.puckRadius:
        return True

def mazeCheckInterception(app, x, y):
    if distanceFormula(app, x, y, app.puckX, 
    app.puckY) <= app.controllerRadius + app.puckRadius:
        return True


# CITATION: From Animations Part 1 Notes
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

# CITATION: From Animations Part 1 Notes
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
def getCell(app, x, y):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)
    return (row, col)

def mazeDrawGrid(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app,row, col)
            if (row,col) in app.open: 
                fill = "yellow"
                canvas.create_rectangle(x0, y0, x1, y1, fill = fill)
            if (row,col)==app.goal:
                fill = "red"
                canvas.create_rectangle(x0, y0, x1, y1, fill = fill)
            else:
                canvas.create_rectangle(x0, y0, x1, y1)

def mazeDrawPuck(app, canvas):
    canvas.create_oval(app.puckX-app.puckRadius, app.puckY-app.puckRadius,
    app.puckX+app.puckRadius,app.puckY+app.puckRadius, fill = 'red')

def mazeDrawHockeyTable(app, canvas):
    canvas.create_rectangle(app.margin, app.margin, app.width-app.margin,
    app.height-app.margin,fill='blue')
    canvas.create_line(app.margin, app.height//2, app.width-app.margin, 
    app.height//2, fill = 'black', width = 3)

def mazeDrawController(app, canvas):
    canvas.create_oval(app.controllerX-app.controllerRadius, app.controllerY-app.controllerRadius,
    app.controllerX+app.controllerRadius,app.controllerY+app.controllerRadius, fill = 'green', width = 2)

def mazeDrawScore(app, canvas):
    if app.createMode == True:
        canvas.create_text(app.width//2,10, text = "Click a box to select/deselect a wall!")
        canvas.create_text(app.width//2, app.height-0.5*app.margin, text = "Click here when done!")
        canvas.create_rectangle(app.width//2 - 60, app.height-30, app.width//2 + 60, app.height-15)
    if app.win == False and app.lose == False and app.createMode == False:
        canvas.create_text(100,30, text = f"Time left: {app.seconds}")
    if app.win == False and app.lose == False and app.randomMazeMode == True:
        canvas.create_text(app.width//2, app.height-0.5*app.margin, text = "Click here to generate new maze!")
        canvas.create_rectangle(app.width//2 - 100, app.height-30, app.width//2 + 100, app.height-15)
    elif app.win == True:
        canvas.create_text(app.width//2, 10, text = "You Win")
    elif app.lose == True:
        canvas.create_text(app.width//2, 10, text = "You Lose")

def drawPuck(app, canvas):
    canvas.create_oval(app.puckX-app.puckRadius, app.puckY-app.puckRadius,
    app.puckX+app.puckRadius,app.puckY+app.puckRadius, fill = 'red')

def drawHockeyTable(app, canvas):
    canvas.create_rectangle(app.margin, app.margin, app.width-app.margin,
    app.height-app.margin,fill='blue')
    canvas.create_line(app.margin, app.height//2, app.width-app.margin, 
    app.height//2, fill = 'black', width = 3)
    canvas.create_rectangle(app.width//2 - 40, app.margin, app.width//2 + 40,
    app.margin+40,fill='blue', width = 2)
    canvas.create_oval(app.width//2 - 40, app.height//2-40, app.width//2 + 40,
    app.height//2+40, width = 2)
    canvas.create_rectangle(app.width//2 - 40, app.height-app.margin-40, app.width//2 + 40,
    app.height-app.margin,fill='blue', width = 2)

def drawController(app, canvas):
    canvas.create_oval(app.controllerX-app.controllerRadius, app.controllerY-app.controllerRadius,
    app.controllerX+app.controllerRadius,app.controllerY+app.controllerRadius, fill = 'green', width = 3)

def drawScore(app, canvas):
    if app.regular == True and app.maze == False and app.youWin == False and app.computerWin == False:
        canvas.create_text(20,10, text = f"You: {app.yourScore}")
        canvas.create_text(app.width-40, 10, text = f"Opponent: {app.computerScore}")
    elif app.regular == True and app.maze == False and app.youWin == True:
        canvas.create_text(app.width//2,10, text = f"You Win")
    elif app.regular == True and app.maze == False and app.computerWin == True:
        canvas.create_text(app.width//2,10, text = f"Computer Win")

def drawComputerController(app, canvas):
    canvas.create_oval(app.computerX-app.computerRadius, app.computerY-app.computerRadius,
    app.computerX+app.computerRadius,app.computerY+app.computerRadius, fill = 'green', width = 3)

def drawHome(app, canvas):
    canvas.create_rectangle(0,0,400,400, fill = 'black')
    canvas.create_text(app.width//2,50, text = f"Air Hockey", fill = 'white', font = "Times 28 bold")
    canvas.create_rectangle(50, 250, app.width//2-25, 300, fill = 'black', outline = 'red')
    canvas.create_rectangle(app.width//2 + 25, 250, app.width-50, 300, fill = 'black', outline = 'red')
    canvas.create_text(110, 275, text = "Regular Mode", font = "Times 10", fill = 'white')
    canvas.create_text(290, 275, text = "Maze Obstacle Mode", font = "Times 10", fill = 'white')
    canvas.create_image(200, 150, image=ImageTk.PhotoImage(app.image2))

def chooseMazeMode(app, canvas):
    if app.maze == True:
        blurb1 = "For maze mode, move your controller to hit the puck into a moving goal."
        blurb2 = "Choose between random maze mode and custom maze mode."
        blurb3 = "Hit the puck into the red goal (which moves every 5 seconds) within 20 seconds."
        
        canvas.create_text(app.width//2, 60, text = f"{blurb1}", font = "Times 9")
        canvas.create_text(app.width//2, 80, text = f"{blurb2}", font = "Times 9")
        canvas.create_text(app.width//2, 100, text = f"{blurb3}", font = "Times 9")

        canvas.create_rectangle(app.width//2 - 3*app.margin, 150, app.width//2 + 3*app.margin, 170)
        canvas.create_rectangle(app.width//2 - 3*app.margin, 180, app.width//2 + 3*app.margin, 200)
        canvas.create_rectangle(app.width//2 - 3*app.margin, 210, app.width//2 + 3*app.margin, 230)
        canvas.create_rectangle(app.width//2 - 3*app.margin, 240, app.width//2 + 3*app.margin, 260)

        canvas.create_text(app.width//2, 160, text = "Custom Maze", font = "Times 8")
        canvas.create_text(app.width//2, 190, text = "Random Maze - Easy", font = "Times 8")
        canvas.create_text(app.width//2, 220, text = "Random Maze - Medium", font = "Times 8")
        canvas.create_text(app.width//2, 250, text = "Random Maze - Hard", font = "Times 8")

def drawRegularOptions(app, canvas):
    if app.regularOptions == True:

        blurb1 = "Choose between regular air hockey, pitt mode, and bouncer mode."
        blurb2 = "Pitt Mode - if the puck enters the pitt, you lose a point."
        blurb3 = "Bouncer Mode - if the puck collides with the bouncer, it will bounce off."
        
        canvas.create_text(app.width//2, 60, text = f"{blurb1}", font = "Times 9")
        canvas.create_text(app.width//2, 80, text = f"{blurb2}", font = "Times 9")
        canvas.create_text(app.width//2, 100, text = f"{blurb3}", font = "Times 9")

        canvas.create_rectangle(app.width//2 - 3*app.margin, 150, app.width//2 + 3*app.margin, 170)
        canvas.create_rectangle(app.width//2 - 3*app.margin, 180, app.width//2 + 3*app.margin, 200)
        canvas.create_rectangle(app.width//2 - 3*app.margin, 210, app.width//2 + 3*app.margin, 230)

        canvas.create_text(app.width//2, 160, text = "Regular Air Hockey", font = "Times 8")
        canvas.create_text(app.width//2, 190, text = "Pitt Mode", font = "Times 8")
        canvas.create_text(app.width//2, 220, text = "Bouncer Mode", font = "Times 8")

def drawPitt(app, canvas):
    if app.placePitt == True:
        canvas.create_text(app.width//2,10, text = "Click on your side to place yellow pitt!")
        canvas.create_text(app.width//2, app.height-0.5*app.margin, text = "Click here when done!")
        canvas.create_rectangle(app.width//2 - 60, app.height-15, app.width//2 + 60, app.height-5)
    canvas.create_oval(app.pittX-app.pittRadius, app.pittY-app.pittRadius,
    app.pittX+app.pittRadius,app.pittY+app.pittRadius, fill = 'yellow')

def drawBouncer(app, canvas):
    if app.placeBouncer == True:
        canvas.create_text(app.width//2,10, text = "Click on your side to place yellow bouncer!")
        canvas.create_text(app.width//2, app.height-0.5*app.margin, text = "Click here when done!")
        canvas.create_rectangle(app.width//2 - 60, app.height-15, app.width//2 + 60, app.height-5)
    canvas.create_oval(app.bouncerX-app.bouncerRadius, app.bouncerY-app.bouncerRadius,
    app.bouncerX+app.bouncerRadius,app.bouncerY+app.bouncerRadius, fill = 'yellow')

def redrawAll(app, canvas):
    if app.homescreen == False and app.maze == False and app.regularOptions == False and app.regular == True:
        drawHockeyTable(app,canvas)
        drawPuck(app, canvas)
        drawController(app, canvas)
        drawComputerController(app, canvas)
        if app.placePitt == False and app.placeBouncer == False:
            drawScore(app,canvas)
    if app.bouncerMode == True:
        drawBouncer(app, canvas)
    if app.pittMode == True:
        drawPitt(app,canvas)
    if app.regularOptions == True:
        drawRegularOptions(app, canvas)
    if app.homescreen == False:
        canvas.create_rectangle(5,app.height-20+5,35,app.height-5)
        canvas.create_text(20, app.height - 20//2, text = "Home", font = "Times 8")
    if app.homescreen == True:
        drawHome(app,canvas)
    if app.maze == True:
        chooseMazeMode(app, canvas)
    if (app.customMode == True or app.randomMazeMode == True) and app.maze == False:
        mazeDrawHockeyTable(app,canvas)
        mazeDrawGrid(app,canvas)
        mazeDrawScore(app,canvas)
        mazeDrawPuck(app, canvas)
        mazeDrawController(app, canvas)

runApp(width=400, height=400)



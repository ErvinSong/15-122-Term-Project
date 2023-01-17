import math, random

from cmu_112_graphics import *

class Zombie():
    def __init__(self, x0, y0, x1, y1, radius, health, damage, diff, color):
        self.radius = radius
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.health = health
        self.damage = damage
        self.diff = diff
        self.color = color

    def assignX0(self, x):
        self.x0 = x

    def assignX1(self, x):
        self.x1 = x

    def assignY0(self, y):
        self.y0 = y

    def assignY1(self, y):
        self.y1 = y

    def getX0(self):
        return self.x0
    
    def getY0(self):
        return self.y0
    
    def getX1(self):
        return self.x1
    
    def getY1(self):
        return self.y1
    
    def changeX(self, val):
        self.x0 = self.x0 + val
        self.x1 = self.x1 + val

    def changeY(self, val):
        self.y1 = self.y1 + val
        self.y0 = self.y0 + val

    def getDiff(self):
        return self.diff
    
    def getColor(self):
        return self.color
    
    def getRadius(self):
        return self.radius
    
    def getHealth(self):
        return self.health
    
    def getDamage(self):
        return self.damage
    
    def takeDamage(self, damage):
        self.health -= damage

    def __repr__(self):
        return self.color + str(self.x0)

#Types of zombies
grunt = Zombie(0, 0, 0, 0, 20, 10, 1, 1, "brown")
tank = Zombie(0, 0, 0, 0, 40, 20, 3, 5, "purple")
goblin = Zombie(0, 0, 0, 0, 10, 5, 1, 3, "green")

class Player():
    def __init__(self, health, totHel):
        self.health = health
        self.totHel = totHel

    def fullHeal(self):
        self.health = self.totHel

    def takeDamage(self, damageTaken):
        self.health -= damageTaken

    def getHealth(self):
        return self.health

    def getTotHel(self):
        return self.totHel
    
class Tree():
    def __init__(self, x, y, list):
        self.x = x
        self.y = y
        self.list = list
    
    def getLeaves(self):
        return self.list
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __repr__(self):
        return str(self.list)
    
#Draws the tree and the leaves according to randomly generated locations
def drawTree(x, y, x0, y0, leaves, canvas):
    canvas.create_oval(x0 + x, y0 + y, x + x0 + 60, y + y0 + 60, 
        fill = "#42692f", outline = "#42692f")
    for i in leaves:
        randx, randy = i
        canvas.create_oval(x0 + x + randx, y + y0 + randy, 
                            x + x0 + randx + 50, y + y0 + randy + 50,
                            fill = "#42692f", outline = "#42692f")
    
class Map():
    def __init__(self, x, y, selection):
        self.x = x
        self.y = y
        self.selection = selection

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def changeX(self, newx):
        self.x += newx

    def changeY(self, newy):
        self.y += newy

    def getSelection(self):
        return self.selection
        
    def __repr__(self):
        return f"{self.selection, self.x, self.y}"

    def drawMap(self, app, canvas):
        if self.selection == 1:
            canvas.create_rectangle(self.x, self.y, self.x + 1470, self.y + 820,
                                fill = "green", outline = "green")
        
allMaps = [1]

class Bullet():
    def __init__(self, x0, y0, x1, y1, damage, xmove, ymove, name, ammo,
                    initialAccel, finalAccel):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.damage = damage
        self.xmove = xmove
        self.ymove = ymove
        self.name = name
        self.maxAmmo = ammo
        self.ammo = ammo
        self.initialAccel = initialAccel
        self.finalAccel = finalAccel

    def getX0(self):
        return self.x0
    
    def getY0(self):
        return self.y0
    
    def getX1(self):
        return self.x1
    
    def getY1(self):
        return self.y1
    
    def getAmmo(self):
        return self.ammo
    
    def getMaxAmmo(self):
        return self.maxAmmo
    
    def shoot(self):
        self.ammo -= 1

    def reload(self):
        self.ammo = self.maxAmmo
    
    def changeX(self, val):
        self.x0 = self.x0 + val
        self.x1 = self.x1 + val

    def changeY(self, val):
        self.y1 = self.y1 + val
        self.y0 = self.y0 + val

    def getXmove(self):
        return self.xmove
    
    def getYmove(self):
        return self.ymove
    
    def getDamage(self):
        return self.damage
    
    def getName(self):
        return self.name
    
    def getAmmo(self):
        return self.ammo
    
    def changeDamage(self, zero):
        self.damage = zero
    
    def getInitialAccel(self):
        return self.initialAccel
    
    #Used to Deaccelerate Bullets
    def changeAccel(self, val):
        self.initialAccel -= val

    def changeFinalAccel(self, val):
        self.finalAccel += val

    def getFinalAccel(self):
        return self.finalAccel
    
#Types of Weapons
pistol = Bullet(0, 0, 0, 0, 5, 0, 0, "PISTOL", 6, 40, 0)
shotgun = Bullet(0, 0, 0, 0, 5, 0, 0, "SHOTGUN", 6, 40, 0)
rifle = Bullet(0, 0, 0, 0, 5, 0, 0, "RIFLE", 30, 80, 0)
sniper = Bullet(0, 0, 0, 0, 50, 0, 0, "SNIPER", 2, 100, 0)
getAnA = Player(100, 100)

class Coin():
    def __init__(self, x0, y0, x1, y1, value):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.value = value

    def getX0(self):
        return self.x0
    
    def getY0(self):
        return self.y0
    
    def getX1(self):
        return self.x1
    
    def getY1(self):
        return self.y1
    
    def changeX(self, val):
        self.x0 += val
        self.x1 += val

    def changeY(self, val):
        self.y0 += val
        self.y1 += val

    #Gets Value from Difficulty of Zombie
    def getValue(self):
        return self.value

def appStarted(app):
    app.x = 0
    app.y = 0
    app.cx = app.width/2
    app.cy = app.height/2
    app.playerR = 20
    app.currWeapon = 0
    app.round = 1
    app.zombies = []
    app.timerDelay = 20
    app.pause = True
    app.healthPerc = getAnA.getHealth() / getAnA.getTotHel()
    app.mousex = 0
    app.mousey = 0
    app.bullet = []
    app.zombiesKilled = 0
    app.zombieIndex = 0
    app.startRound = True
    app.zombList = []
    app.nextRound = False
    app.mapList = []
    app.gunList = [pistol]
    app.coinList = []
    app.bank = 0
    app.rifle = False
    app.sniper = False
    app.shotgun = False
    app.speedCost = 25
    app.speedBuy = False
    app.speed = 5
    app.reload = False
    app.reloadStart = 0
    app.healthBuy = False
    app.healthCost = 0
    app.treesInForest = []
    app.xBound1 = -1470
    app.xBound2 = 2940
    app.yBound1 = -820
    app.yBound2 = 1640
    app.homeScreen = app.loadImage("Untitled_Artwork.png")
    app.start = True

def selectMaps(app):
    list = []
    for i in range(9):
        rand = 0
        map = Map(0, 0, allMaps[rand])
        list.append(map)
    return list

#Randomly generates location of trees and leaves
def selectTrees(app):
        list = []
        for i in range(15):
            leafList = []
            for i in range(6):
                randx = random.randint(-30, 40)
                randy = random.randint(-30, 40)
                leafList.append((randx, randy))
            x = random.randint(1, 2)
            if x == 1:
                randx = random.randint(5, 650)
            else:
                randx = random.randint(810, 1465)
            y = random.randint(1, 2)
            if y == 1:
                randy = random.randint(5, 325)
            else:
                randy = random.randint(495, 815)
            temp = Tree(randx, randy, leafList)
            list.append(temp)
        return list

def drawPlayer(app, canvas):
    canvas.create_oval(app.cx - app.playerR, app.cy - app.playerR,
                        app.cx + app.playerR, app.cy + app.playerR,
                        fill = "yellow", outline = "black", width = 5)

#Randomly generates a location to spawn a zombie
def spawnZombie(radius):
    XorY = random.randint(0, 3)
    if XorY == 1:
        topOrBot = random.randint(0, 3)
        if topOrBot ==1:
            xcoord = random.randint(-1, 1001) + 200
            x0 = xcoord - radius
            y0 = 100 - radius
            x1 = xcoord + radius
            y1 = 100 + radius
            return x0, y0, x1, y1
        else:
            xcoord = random.randint(-1, 1001) + 200
            x0 = xcoord - radius
            y0 = 700 - radius
            x1 = xcoord + radius
            y1 = 700 + radius
            return x0, y0, x1, y1
    else:
        topOrBot = random.randint(0, 3)
        if topOrBot == 1:
            ycoord = random.randint(-1, 601) + 100
            x0 = 200 - radius
            y0 = ycoord - radius
            x1 = 200 + radius
            y1 = ycoord + radius
            return x0, y0, x1, y1
        else:
            ycoord = random.randint(-1, 601) + 200
            x0 = 1200 - radius
            y0 = ycoord - radius
            x1 = 1200 + radius
            y1 = ycoord + radius
            return x0, y0, x1, y1

#List of the type of zombies      
zombos = [grunt, tank, goblin]

#Randomly selects zombies depending on round level
def selectZombies(app):
    max = 0
    list = []
    #Keeps adding zombies until total difficulty of zombies is optimal
    while max < (app.round * 5):
        temp = 0
        rand = random.randint(0, len(zombos) - 1)
        if zombos[rand].getDiff() + max <= (app.round * 5):
            temp = Zombie(0, 0, 0, 0, 
                            zombos[rand].getRadius(),
                            zombos[rand].getHealth(),
                            zombos[rand].getDamage(),
                            zombos[rand].getDiff(),
                            zombos[rand].getColor())
            list.append(temp)
            max += zombos[rand].getDiff()
    return list
    
def drawZombie(app, canvas, x0, y0, x1, y1, color):
    canvas.create_oval(x0, y0, x1, y1,
                        fill = color, outline = "black", width = 5)
    if color == "purple":
        canvas.create_oval(x0 + 20, y0 + 20, x0 + 38, y0 + 38,
                            fill = "white", outline = "white")
        canvas.create_oval(x0 + 42, y0 + 20, x0 + 60, y0 + 38,
                            fill = "white", outline = "white")
        canvas.create_line(x0 + 23, y0 + 11, x0 + 38, y0 + 19,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 41, y0 + 19, x0 + 53, y0 + 10,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 25, y0 + 67, x0 + 32, y0 + 53,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 32, y0 + 53, x0 + 46, y0 + 53,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 46, y0 + 53, x0 + 53, y0 + 67, 
                            fill = "black", width = 3)
        canvas.create_oval(x0 + 29, y0 + 27, x0 + 35, y0 + 33,
                            fill = "black")
        canvas.create_oval(x0 + 45, y0 + 27, x0 + 51, y0 + 33,
                            fill = "black")
    if color == "brown":
        canvas.create_line(x0 + 14, y0 + 7, x0 + 20, y0 + 12,
                            fill = "black", width = 4)
        canvas.create_line(x0 + 20, y0 + 12, x0 + 27, y0 + 6,
                            fill = "black", width = 4)
        canvas.create_oval(x0 + 14, y0 + 14, x0 + 28, y0 + 28,
                            fill = "white")
        canvas.create_oval(x0 + 17, y0 + 17, x0 + 23, y0 + 23,
                            fill = "black")
        canvas.create_polygon(x0 + 16, y0 + 33, x0 + 25, y0 + 33,
                                x0 + 22, y0 + 39, fill = "red")
        canvas.create_line(x0 + 13, y0 + 33, x0 + 28, y0 + 33,
                            fill = "black", width = 2)
    if color == "green":
        canvas.create_line(x0 + 7, y0 + 6, x0 + 7, y0 + 9,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 15, y0 + 6, x0 + 15, y0 + 9,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 7, y0 + 17, x0 + 9, y0 + 14,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 9, y0 + 14, x0 + 13, y0 + 14,
                            fill = "black", width = 3)
        canvas.create_line(x0 + 13, y0 + 14, x0 + 15, y0 + 17,
                            fill = "black", width = 3)
    
def drawCoin(app, canvas, x0, y0, x1, y1):
    canvas.create_oval(x0, y0, x1, y1,
                        fill = "yellow", outline = "black", width = 3)
    
def drawBullet(app, canvas, x0, y0, x1, y1):
    canvas.create_oval(x0, y0, x1, y1,
                        fill = "black", outline = "black")

def assignMap(app):
    list = [[-1470, -820], [0, -820], [1470, -820],
            [-1470, 0], [0, 0], [1470, 0],
            [-1470, 820], [0, 820], [1470, 820]]
    for i in range(len(app.mapList)):
        app.mapList[i].changeX(list[i][0])
        app.mapList[i].changeY(list[i][1])

def drawHealth(app, canvas):
    canvas.create_rectangle(400, 700, 1070, 750, fill = "black", 
                            outline = "black")
    canvas.create_rectangle(410, 710, 410 + (650 * app.healthPerc), 740, 
                            fill = "green", outline = "black")

def drawPause(app, canvas):
    canvas.create_rectangle(0, 0, 1470, 820, fill = "gray")
    canvas.create_text(app.cx, app.cy, text = "PAUSED",
                        font = "Helvetica 100", fill = "black")

def drawGameOver(app, canvas):
    fonta=('Comic Sans MS', 30)
    canvas.create_rectangle(0, 0, 1470, 820, fill = "black")
    canvas.create_text(app.cx, app.cy, text = 'GAME OVER', fill = "red", 
                        font = "Helvetica 100")
    canvas.create_text(app.cx, 555,
                        text = f"You Survived to Round {app.round} :)",
                        fill = "#3EB489", font = fonta)
    canvas.create_text(app.cx, 700,
                        text = "Press \"J\" to Play Again!",
                        fill = "#3EB489", font = fonta)

#Uses the unit circle to find where the gun should point and where bullets go
def findAngle(app, angle):
    xdiff = app.mousex - app.cx
    ydiff = app.mousey - app.cy
    if xdiff < 0:
        xneg = True
    else:
        xneg = False
    if ydiff < 0:
        yneg = True
    else:
        yneg = False
    if xdiff != 0:
        angle = abs(math.atan(ydiff/xdiff)) + angle
    else:
        angle = 1.5708 + angle
    if xneg:
        xmove = (math.cos(angle)) * -1
    else:
        xmove = math.cos(angle)
    if yneg:
        ymove = (math.sin(angle)) * -1
    else:
        ymove = math.sin(angle)
    return xmove, ymove
    
def drawGun(app, canvas):
    xmove, ymove = findAngle(app, 0)
    xmove *= 50
    ymove *= 50
    canvas.create_line(app.cx, app.cy, app.cx + xmove, app.cy + ymove, 
                        fill = "black", width = 5)

#The following are all functions that check for collision
def bulletZombieCollide(bullet, zombie):
    bxstart = bullet.getX1() - 2
    bystart = bullet.getY1() - 2
    interval = bullet.getInitialAccel() // 5
    for i in range(interval):
        bxstart += (1/interval) * bullet.getXmove() * bullet.getInitialAccel()
        bystart += (1/interval) * bullet.getYmove() * bullet.getInitialAccel()
        if bulletZombieCollideHelper(bxstart, bystart, zombie):
            return True
        else:
            continue
        
def bulletTreeCollide(app, bullet):
    bxstart = bullet.getX1() - 2
    bystart = bullet.getY1() - 2
    interval = bullet.getInitialAccel() // 5
    for i in range(interval):
        bxstart += (1/interval) * bullet.getXmove() * bullet.getInitialAccel()
        bystart += (1/interval) * bullet.getYmove() * bullet.getInitialAccel()
        if bulletTreeCollideHelper(app, bxstart, bystart):
            return True
        else:
            continue
    
def bulletTreeCollideHelper(app, bxstart, bystart):
    bcx = bxstart
    bcy = bystart
    for k in app.mapList:
        if k.getSelection() == 1:
            for i in app.treesInForest:
                list = i.getLeaves()
                for j in list:
                    tcx, tcy = j
                    tcx += (i.getX() + k.getX() + 25)
                    tcy += (i.getY() + k.getY() + 25)
                    xdist = bcx - tcx
                    ydist = bcy - tcy
                    sumsq = (ydist ** 2) + (xdist ** 2)
                    distance = math.sqrt(sumsq)
                    tOrF = distance <= (2 + 25)
                    if tOrF:
                        return tOrF
    return False

def bulletZombieCollideHelper(bxstart, bystart, zombie):
    bcx = bxstart
    bcy = bystart
    zcx = zombie.getX1() - zombie.getRadius()
    zcy = zombie.getY1() - zombie.getRadius()
    xdist = bcx - zcx
    ydist = bcy - zcy
    sumsq = (ydist ** 2) + (xdist ** 2)
    distance = math.sqrt(sumsq)
    return distance <= (2 + zombie.getRadius())

def playerZombieCollide(app, zombie):
    pcx = app.cx
    pcy = app.cy
    zcx = zombie.getX1() - zombie.getRadius()
    zcy = zombie.getY1() - zombie.getRadius()
    xdist = pcx - zcx
    ydist = pcy - zcy
    sumsq = (ydist ** 2) + (xdist ** 2)
    distance = math.sqrt(sumsq)
    return distance <= (app.playerR + zombie.getRadius())

def playerTreeCollide(app, xval, yval):
    pcx = app.cx
    pcy = app.cy
    for k in app.mapList:
        if k.getSelection() == 1:
            for i in app.treesInForest:
                list = i.getLeaves()
                for j in list:
                    tcx, tcy = j
                    tcx += (i.getX() + k.getX() + 25 + xval)
                    tcy += (i.getY() + k.getY() + 25 + yval)
                    xdist = pcx - tcx
                    ydist = pcy - tcy
                    sumsq = (ydist ** 2) + (xdist ** 2)
                    distance = math.sqrt(sumsq)
                    tOrF = distance <= (app.playerR + 15)
                    if tOrF:
                        return tOrF
    return False

def zombieTreeCollide(app, zombie, xval, yval):
    zcx = zombie.getX1() - zombie.getRadius() + xval
    zcy = zombie.getY1() - zombie.getRadius() + yval
    if zombie.getColor() == "green":
        return False
    for k in app.mapList:
        if k.getSelection() == 1:
            for i in app.treesInForest:
                list = i.getLeaves()
                for j in list:
                    tcx, tcy = j
                    tcx += (i.getX() + k.getX() + 25 )
                    tcy += (i.getY() + k.getY() + 25)
                    xdist = zcx - tcx
                    ydist = zcy - tcy
                    sumsq = (ydist ** 2) + (xdist ** 2)
                    distance = math.sqrt(sumsq)
                    tOrF = distance <= (app.playerR + 25)
                    if tOrF:
                        return tOrF
    return False

def playerCoinCollide(app, coin):
    pcx = app.cx
    pcy = app.cy
    ccx = coin.getX1() - 4
    ccy = coin.getY1() - 4
    xdist = pcx - ccx
    ydist = pcy - ccy
    sumsq = (ydist ** 2) + (xdist ** 2)
    distance = math.sqrt(sumsq)
    return distance <= (app.playerR + 4)

def playerBoundCollide(app, xval, yval):
    px1 = app.cx - app.playerR
    if px1 <= app.xBound1 + xval:
        return True
    px2 = app.cx + app.playerR
    if px2 >= app.xBound2 + xval:
        return True
    py1 = app.cy - app.playerR
    if py1 <= app.yBound1 + yval:
        return True
    py2 = app.cy + app.playerR
    if py2 >= app.yBound2 + yval:
        return True
    return False

#Removes coin from map and adds the value to the player's bank
def takeCoin(app):
    for i in app.coinList:
        if playerCoinCollide(app, i):
            app.bank += i.getValue()
            app.coinList.remove(i)
            break

#Zombies have different health and each weapon does different damage.
#The function checks which bullet hit the zombie to see how much damage is done
def damageZombie(app):
    for i in app.bullet:
        for j in app.zombies:
            if bulletZombieCollide(i, j):
                j.takeDamage(i.getDamage())
                app.bullet.remove(i)
                if j.getHealth() <= 0:
                    app.zombiesKilled += j.getDiff()
                    temp = Coin(j.getX0() + j.getRadius() - 5,
                                j.getY0() + j.getRadius() - 5,
                                j.getX1() - j.getRadius() + 5,
                                j.getY1() - j.getRadius() + 5,
                                j.getDiff())
                    app.coinList.append(temp)
                    app.zombies.remove(j)
                break

#Zombies also do different damage
def damagePlayer(app):
    if not app.pause:
        for i in app.zombies:
            if playerZombieCollide(app, i):
                damage = i.getDamage()
                getAnA.takeDamage(damage)

def reload(app):
    app.reloadStart += 100
    if app.reloadStart == 2000:
        app.gunList[app.currWeapon].reload()
        app.reload = False
        app.reloadStart = 0

def drawReload(app, canvas):
    percentage = ((app.reloadStart/2000) * 100) // 1
    canvas.create_text(735, 675, text = f"Reloading: {percentage}%",
                        font = "Helvetica 30", fill = "black")

def removeBullet(app):
    for i in app.bullet:
        if i.getX0() < 0 or i.getX0() > 1470:
            app.bullet.remove(i)
            break
        elif i.getY0() < 0 or i.getY0() > 820:
            app.bullet.remove(i)
            break
    #Removes bullet once the bullet slows to a halt according to its deacceleration
    for i in app.bullet:
        if i.getInitialAccel() < 0:
            app.bullet.remove(i)
    for i in app.bullet:
        if bulletTreeCollide(app, i):
            app.bullet.remove(i)
            break

def drawShop(app, canvas):
    canvas.create_rectangle(0, 0, 1470, 820, fill = "yellow")
    canvas.create_text(735, 75, text = "SHOP", 
                        font = "Helvetica 100", fill = "black")
    canvas.create_rectangle(1120, 700, 1420, 770, 
                            fill = "black", outline = "yellow")
    canvas.create_text(1270, 735, text = "Continue", 
                        font = "Times 50", fill = "white")
    canvas.create_text(200, 75, text = f"${int(app.bank)}",
                        font = "Times 100", fill = "black")
    canvas.create_rectangle(75, 175, 275, 275,
                            fill = "black", outline = "yellow")
    canvas.create_text(175, 300, text = "Shotgun",
                        font = "Times 50", fill = "black")
    if not app.shotgun:
        canvas.create_text(175, 210, text = "$25",
                            font = "Calibri 25", fill = "white")
        canvas.create_text(175, 240, text = "To Unlock", 
                            font = "Calibri 25", fill = "white")
    canvas.create_rectangle(355, 175, 555, 275,
                            fill = "black", outline = "yellow")
    canvas.create_text(455, 300, text = "Rifle",
                        font = "Times 50", fill = "black")
    if not app.rifle:
        canvas.create_text(455, 210, text = "$5",
                            font = "Calibri 25", fill = "white")
        canvas.create_text(455, 240, text = "To Unlock",
                            font = "Calibri 25", fill = "white")
    canvas.create_rectangle(635, 175, 835, 275,
                            fill = "black", outline = "yellow")
    canvas.create_text(735, 300, text = "Sniper",
                        font = "Times 50", fill = "black")
    if not app.sniper:
        canvas.create_text(735, 210, text = "$10",
                            font = "Calibri 25", fill = "white")
        canvas.create_text(735, 240, text = "To Unlock",
                            font = "Calibri 25", fill = "white")
    canvas.create_rectangle(915, 175, 1115, 275,
                            fill = "black", outline = "yellow")
    canvas.create_text(1015, 300, text = "Health",
                        font = "Times 50", fill = "black")
    if not app.healthBuy:
        canvas.create_text(1015, 210, text = f"${int(app.healthCost)}",
                            font = "Calibri 25", fill = "white")
        canvas.create_text(1015, 240, text = "To Max Heal",
                            font = "Calibri 25", fill = "white")
    canvas.create_rectangle(1195, 175, 1395, 275,
                            fill = "black", outline = "yellow")
    canvas.create_text(1295, 300, text = "Speed",
                        font = "Times 50", fill = "black")
    if not app.speedBuy:
        canvas.create_text(1295, 210, text = f"${app.speedCost}",
                            font = "Calibri 25", fill = "white")
        canvas.create_text(1295, 240, text = "To Level Up",
                            font = "Calibri 25", fill = "white")

#Randomly generates a viable next move depending on the obstacles around
def nextMove(app, zombie, xneg, yneg):
    x = zombie.getX0() + zombie.getRadius()
    y = zombie.getY0() + zombie.getRadius()
    randomval = random.randint(1, 2)
    if randomval == 1:
        if app.cx - 5 > x or app.cx + 5 < x:
            #Checks for collision before implementing
            if not zombieTreeCollide(app, zombie, -1 * xneg * 25, 0):
                return ("x", -1 * xneg * 5)
            if zombieTreeCollide(app, zombie, -1 * xneg * 25, 0):
                return ("y", xneg * 5)
            if not zombieTreeCollide(app, zombie, 0, -1 * yneg * 25):
                return ("y", -1 * yneg * 5)
            else:
                return ("x", -1 * yneg * 5)
        if app.cy - 5 > y or app.cy + 5 < y:
            if not zombieTreeCollide(app, zombie, 0, -1 * xneg * 25):
                return ("y", -1 * yneg * 5)
            if zombieTreeCollide(app, zombie, 0, -1 * yneg * 25):
                return ("x", -1 * yneg * 5)
            if not zombieTreeCollide(app, zombie, -1 * xneg * 25, 0):
                return ("x", -1 * xneg * 5)
            else:
                return ("y", -1 * xneg * 5)
        else:
            return ("x", 0)
    else:
        if app.cy - 5 > y or app.cy + 5 < y:
            if not zombieTreeCollide(app, zombie, 0, -1 * xneg * 25):
                return ("y", -1 * yneg * 5)
            if zombieTreeCollide(app, zombie, 0, -1 * yneg * 25):
                return ("x", -1 * yneg * 5)
            if not zombieTreeCollide(app, zombie, -1 * xneg * 25, 0):
                return ("x", -1 * xneg * 5)
            else:
                return ("y", -1 * xneg * 5)
        if app.cx - 5 > x or app.cx + 5 < x:
            if not zombieTreeCollide(app, zombie, -1 * xneg * 25, 0):
                return ("x", -1 * xneg * 5)
            if zombieTreeCollide(app, zombie, -1 * xneg * 25, 0):
                return ("y", -1 * xneg * 5)
            if not zombieTreeCollide(app, zombie, 0, -1 * yneg * 25):
                return ("y", -1 * yneg * 5)
            else:
                return ("x", -1 * yneg * 5)
        else:
            return ("x", 0)
        
def mousePressed(app, event):
    #Adds bullet to list according to its weapon type
    if not app.pause:
        xmove, ymove = findAngle(app, 0)
        name = app.gunList[app.currWeapon].getName()
        damage = app.gunList[app.currWeapon].getDamage()
        ammo = app.gunList[app.currWeapon].getAmmo()
        accel = app.gunList[app.currWeapon].getInitialAccel()
        increment = app.gunList[app.currWeapon].getFinalAccel()
        if app.gunList[app.currWeapon].getAmmo() >= 1:
            app.gunList[app.currWeapon].shoot()
            if name == "SHOTGUN":
                for i in range(10):
                    randAngle = (random.random() * 1.4) - 0.7
                    xmove, ymove = findAngle(app, randAngle)
                    bullet = Bullet(app.cx + xmove - 2, app.cy + ymove - 2, app.cx + xmove + 2,
                                app.cy + ymove + 2, damage, xmove, ymove,
                                name, ammo, accel, increment)
                    app.bullet.append(bullet)
            else:
                bullet = Bullet(app.cx + xmove - 2, app.cy + ymove - 2, app.cx + xmove + 2,
                                app.cy + ymove + 2, damage, xmove, ymove,
                                name, ammo, accel, increment)
                app.bullet.append(bullet)
    #Applies when in shop screen
    if app.nextRound:
        if event.x > 355 and event.x < 555:
            if event.y > 175 and event.y < 275:
                if not app.rifle and app.bank >= 5:
                    app.gunList.append(rifle)
                    app.bank -= 5
                    app.rifle = True
        if event.x > 75 and event.x < 275:
            if event.y > 175 and event.y < 275:
                if not app.shotgun and app.bank >= 25:
                    app.gunList.append(shotgun)
                    app.bank -= 25
                    app.shotgun = True
        if event.x > 915 and event.x < 1115:
            if event.y > 175 and event.y < 275:
                if not app.healthBuy and app.bank >= app.healthCost:
                    getAnA.fullHeal()
                    app.bank -= app.healthCost
        if event.x > 1195 and event.x < 1395:
            if event.y > 175 and event.y < 275:
                if not app.speedBuy and app.bank >= app.speedCost:
                    app.speed += 1
                    app.bank -= app.speedCost
                    app.speedCost += 100
        if event.x > 635 and event.x < 835:
            if event.y > 175 and event.y < 275:
                if not app.sniper and app.bank >= 10:
                    app.gunList.append(sniper)
                    app.bank -= 10
                    app.sniper = True
        #Continue button that resets everything
        if event.x < 1420 and event.x > 1120:
            if event.y < 770 and event.y > 700:
                app.x = 0
                app.y = 0
                app.mapList = []
                app.timerDelay = 20
                app.zombieIndex = 0
                app.round += 1
                app.zombiesKilled = 0
                app.pause = False
                app.nextRound = False
                app.startRound = True
                for i in app.gunList:
                    i.reload()
                app.xBound1 = -1470
                app.xBound2 = 2940
                app.yBound1 = -820
                app.yBound2 = 1640

def keyPressed(app, event):
    #Play Again
    if (event.key == "j" and app.healthPerc <= 0):
        appStarted(app)
        pistol.reload()
        shotgun.reload()
        sniper.reload()
        rifle.reload()
        getAnA.fullHeal()
    #Starts Game
    if (event.key == "Space"):
        app.pause = False
        app.start = False
    #Pause Game
    if (event.key == "p"):
        app.pause = not app.pause
    #Reloads
    if (event.key == "r"):
        app.reload = True
    #Next Weapon
    if (event.key == "e"):
        if not app.reload:
            if app.currWeapon == (len(app.gunList) - 1):
                app.currWeapon = 0
            else:
                app.currWeapon += 1
    #Previous Weapon
    if (event.key == "q"):
        if not app.reload:
            if app.currWeapon == 0:
                app.currWeapon = len(app.gunList) - 1
            else:
                app.currWeapon -= 1
    #Checks if player can move up and moves everything accordingly
    if (event.key == "w" and not playerTreeCollide(app, 0, app.speed) and 
        not playerBoundCollide(app, 0, app.speed)):
        app.y += app.speed
        app.yBound1 += app.speed
        app.yBound2 += app.speed
        for i in range(len(app.zombies)):
            app.zombies[i].changeY(app.speed)
        for i in range(len(app.bullet)):
            app.bullet[i].changeY(app.speed)
        for i in app.mapList:
            i.changeY(app.speed)
        for i in app.coinList:
            i.changeY(app.speed)
    #Checks if player can move down and moves everything accordingly
    if (event.key == "s" and not playerTreeCollide(app, 0, -1 * app.speed) and 
        not playerBoundCollide(app, 0, -1 * app.speed)):
        app.y -= app.speed
        app.yBound1 -= app.speed
        app.yBound2 -= app.speed
        for i in range(len(app.zombies)):
            app.zombies[i].changeY(-1 * app.speed)
        for i in range(len(app.bullet)):
            app.bullet[i].changeY(-1 * app.speed)
        for i in app.mapList:
            i.changeY(-1 * app.speed)
        for i in app.coinList:
            i.changeY(-1 * app.speed)
    #Checks if player can move left and moves everything accordingly
    if (event.key == "a" and not playerTreeCollide(app, app.speed, 0) and 
        not playerBoundCollide(app, app.speed, 0)):
        app.x += app.speed
        app.xBound1 += app.speed
        app.xBound2 += app.speed
        for i in range(len(app.zombies)):
            app.zombies[i].changeX(app.speed)
        for i in range(len(app.bullet)):
            app.bullet[i].changeX(app.speed)
        for i in app.mapList:
            i.changeX(app.speed)
        for i in app.coinList:
            i.changeX(app.speed)
    #Checks if player can move right and moves everything accordingly
    if (event.key == "d" and not playerTreeCollide(app, -1 * app.speed, 0) and 
        not playerBoundCollide(app, -1 * app.speed, 0)):
        app.x -= app.speed
        app.xBound1 -= app.speed
        app.xBound2 -= app.speed
        for i in range(len(app.zombies)):
            app.zombies[i].changeX(-1 * app.speed)
        for i in range(len(app.bullet)):
            app.bullet[i].changeX(-1 * app.speed)
        for i in app.mapList:
            i.changeX(-1 * app.speed)
        for i in app.coinList:
            i.changeX(-1 * app.speed)

def mouseMoved(app, event):
    app.mousex = event.x
    app.mousey = event.y

def timerFired(app):
    removeBullet(app)
    takeCoin(app)
    damageZombie(app)
    damagePlayer(app)
    if app.reload:
        reload(app)
    app.healthPerc = getAnA.getHealth() / getAnA.getTotHel()
    app.healthCost = ((1 - app.healthPerc) * 100) // 10
    if app.healthCost == 0:
        app.healthCost = 1
    #Ends Round
    if app.zombiesKilled >= (app.round * 5):
        app.pause = True
        app.nextRound = True
        app.coinList = []
    #Prepares for New Round
    if app.startRound:
        app.bullet = []
        app.zombList = selectZombies(app)
        app.mapList = selectMaps(app)
        app.treesInForest = selectTrees(app)
        assignMap(app)
        app.startRound = False
    #Spawns Zombies
    if app.timerDelay % 10 == 0 and not app.pause and app.zombieIndex < len(app.zombList):
        x0, y0, x1, y1 = spawnZombie(app.zombList[app.zombieIndex].getRadius())
        app.zombList[app.zombieIndex].assignX0(x0)
        app.zombList[app.zombieIndex].assignX1(x1)
        app.zombList[app.zombieIndex].assignY0(y0)
        app.zombList[app.zombieIndex].assignY1(y1)
        if not zombieTreeCollide(app, app.zombList[app.zombieIndex], 0, 0):
            app.zombies.append(app.zombList[app.zombieIndex])
            app.zombieIndex += 1
        app.timerDelay += 1
    elif not app.pause:
        app.timerDelay += 1
    #Moves Zombies
    if app.timerDelay % 1 == 0 and not app.pause:
        for i in app.zombies:
            xneg = app.cx - (i.getX0() + i.getRadius())
            if xneg >= 0:
                xneg = -1
            else:
                xneg = 1
            yneg = app.cy - (i.getY0() + i.getRadius())
            if yneg >= 0:
                yneg = -1
            else:
                yneg = 1
            if i.getX0() + i.getRadius() < app.cx:
                pos, move = nextMove(app, i, xneg, yneg)
                if pos == "x":
                    i.changeX(move)
                else:
                    i.changeY(move)
            else:
                pos, move = nextMove(app, i, xneg, yneg)
                if pos == "x":
                    i.changeX(move)
                else:
                    i.changeY(move)
            if i.getY0() + i.getRadius() < app.cy:
                pos, move = nextMove(app, i, xneg, yneg)
                if pos == "x":
                    i.changeX(move)
                else:
                    i.changeY(move)
            else:
                pos, move = nextMove(app, i, xneg, yneg)
                if pos == "x":
                    i.changeX(move)
                else:
                    i.changeY(move)
    #Moves bullets
    if app.timerDelay % 1 == 0 and not app.pause:
        for i in range(len(app.bullet)):
            accel = app.bullet[i].getInitialAccel()
            app.bullet[i].changeX((app.bullet[i].getXmove()) * accel)
            app.bullet[i].changeY((app.bullet[i].getYmove()) * accel)
            app.bullet[i].changeFinalAccel(1)
            app.bullet[i].changeAccel(app.bullet[i].getFinalAccel() + 1)

def redrawAll(app, canvas):
    canvas.create_rectangle(-2270, -1300, 4410, 2460, fill = "black")
    for i in app.mapList:
        i.drawMap(app, canvas)
    for j in app.mapList:
        if j.getSelection() == 1:
            for i in app.treesInForest:
                        drawTree(j.getX(), j.getY(), 
                            i.getX(), i.getY(), i.getLeaves(), canvas)
    drawGun(app,canvas)
    drawPlayer(app,canvas)
    drawHealth(app,canvas)
    gun = app.gunList[app.currWeapon]
    canvas.create_text(735, 775, text = f"${int(app.bank)}",
                        font = "Helvetica 30", fill = "black" )
    if app.reload:
        drawReload(app, canvas)
    else:
        canvas.create_text(735, 675,
                            text = f"Ammo: {gun.getAmmo()}/{gun.getMaxAmmo()}",
                            font = "Helvetica 30", fill = "black")
    canvas.create_text(1270, 20, text = "WEAPON:", 
                        font = "Helvetica 30", fill = "black")
    canvas.create_text(1270, 50, text = app.gunList[app.currWeapon].getName(),
                        font = "Helvetica 30", fill = "black")
    canvas.create_text(200, 20, text = "ROUND:",
                        font = "Helvetica 30", fill = "black")
    canvas.create_text(200, 50, text = str(app.round),
                        font = "Helvetica 30", fill = "black")
    for i in range(len(app.zombies)):
        drawZombie(app, canvas,
                    app.zombies[i].getX0(),
                    app.zombies[i].getY0(), 
                    app.zombies[i].getX1(), 
                    app.zombies[i].getY1(),
                    app.zombies[i].getColor())
    for i in range(len(app.coinList)):
        drawCoin(app, canvas,
                    app.coinList[i].getX0(),
                    app.coinList[i].getY0(),
                    app.coinList[i].getX1(),
                    app.coinList[i].getY1())
    for i in range(len(app.bullet)):
        drawBullet(app, canvas,
                    app.bullet[i].getX0(),
                    app.bullet[i].getY0(),
                    app.bullet[i].getX1(),
                    app.bullet[i].getY1())
    if app.pause:
        drawPause(app, canvas)
    if app.nextRound:
        drawShop(app, canvas)
    if app.healthPerc <= 0:
        drawGameOver(app, canvas)
    if app.start:
        canvas.create_image(735, 410, image = ImageTk.PhotoImage(app.homeScreen))

def playGame():
    runApp(width=1470, height=820)

if __name__ == '__main__':
    playGame()
import pygame
# import pygame module
import time
# import time module
import random
# import random module

pygame.init()
# game engine

# variable list --------------------------------------
gameName = "Asteroids"  # name
done = False  # sentinel value
size = (300, 300)  # size for screen
screen = pygame.display.set_mode(size)  # set screen size
# pygame.FULLSCREEN
pygame.display.set_caption(gameName)  # set window title
clock = pygame.time.Clock()  # used for ticks later
# Colour Variables for background
black = (0, 0, 0)  # colour black - clearing the screen
white = (255, 255, 255)  # text colour
# IMPORTANT
currentScore = 0  # the current score
difficulty = 1  # overall difficulty
rocketX = 100  # the rocket's X Cord
gameOver = False  # sentinel value for game
goHome = False # stops the game when help key or escape key pushed

# icon display
pygame.display.set_caption(gameName)
icon = pygame.image.load("assets/realicon.png")
pygame.display.set_icon(icon)

# images
titleScreen = pygame.image.load('assets/game_title.png')
helpNotification = pygame.image.load('assets/help.png')
background = pygame.image.load('assets/background.png')
splash = pygame.image.load('assets/splash.png')
helpScreen = pygame.image.load('assets/helpscreen.png')
gameOverScreen = pygame.image.load(r'assets/gameOver.png')
ship1 = pygame.image.load('assets/ship1.png')
ship2 = pygame.image.load('assets/ship2.png')
ship3 = pygame.image.load('assets/ship3.png')
easyAsteroid1 = pygame.image.load('assets/easyAsteroid1.png')
easyAsteroid2 = pygame.image.load('assets/easyAsteroid2.png')
easyAsteroid3 = pygame.image.load('assets/easyAsteroid3.png')
mediumAsteroid1 = pygame.image.load('assets/mediumAsteroid1.png')
mediumAsteroid2 = pygame.image.load('assets/mediumAsteroid2.png')
mediumAsteroid3 = pygame.image.load('assets/mediumAsteroid3.png')
hardAsteroid1 = pygame.image.load('assets/hardAsteroid1.png')
hardAsteroid2 = pygame.image.load('assets/hardAsteroid2.png')
hardAsteroid3 = pygame.image.load('assets/hardAsteroid3.png')
explosion1 = pygame.image.load('assets/explosion1.png')
explosion2 = pygame.image.load('assets/explosion2.png')
explosion3 = pygame.image.load('assets/explosion3.png')
explosion4 = pygame.image.load('assets/explosion4.png')


# music variables

music = 'assets/Innominate_2.mp3'



# text

font = pygame.font.SysFont("Roboto", 30)

# reset screen/background


def wipe():
    screen.fill(black)
    screen.blit(background, (0, 0))

# display new screen


def show():
    pygame.display.update()

# random asteroid lists -----------------------------------------------


easyList = [easyAsteroid1, easyAsteroid2, easyAsteroid3]
mediumList = [mediumAsteroid1, mediumAsteroid2, mediumAsteroid3]
hardList = [hardAsteroid1, hardAsteroid2, hardAsteroid3]
easyChoice = random.choice(easyList)
mediumChoice = random.choice(mediumList)
hardChoice = random.choice(hardList)
# classes ----------------------------------------------


class asteroid(pygame.sprite.Sprite):
    def __init__(self, xCords, difficult, new):
        super().__init__()
        if difficult == 1:
            easy = easyChoice
            self.image = screen.blit(easy, (xCords, new))
        elif difficult == 2:
            medium = mediumChoice
            self.image = screen.blit(medium, (xCords, new))
        elif difficult == 3:
            hard = hardChoice
            self.image = screen.blit(hard, (xCords, new))


class ship(pygame.sprite.Sprite):
    def __init__(self, xCords):
        super().__init__()
        self.image = screen.blit(ship1, (xCords, 200))

# -----------------------------------------------------

# asteroid global variables used for OPP


x = 0
globalX = 0
newLocation = 0




def startAsteroids(difficult):  # start asteroids function
    global x
    global newLocation
    global currentScore
    global gameOver
    x = random.randint(0, 270) # random x cord for asteroid
    global globalX
    global difficulty
    global goHome
    printDifficulty = ""
    globalX = x
    newLocation = 0
    for i in range(20):
        # Inputs used for main menu screen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # change difficulty - easy
                if event.key == pygame.K_1:
                    difficulty = 1
                # change difficulty - medium
                elif event.key == pygame.K_2:
                    difficulty = 2
                # change difficulty - hard
                elif event.key == pygame.K_3:
                    difficulty = 3
                # move rocket left
                elif event.key == pygame.K_LEFT:
                    wipe()
                    moveRocketLeft()
                    changingRocket(rocketX, 200)
                    asteroid(x, difficulty, newLocation)
                    show()
                # move rocket right
                elif event.key == pygame.K_RIGHT:
                    wipe()
                    moveRocketRight()
                    changingRocket(rocketX, 200)
                    asteroid(x, difficulty, newLocation)
                    show()
                # escape to title screen
                elif event.key == pygame.K_ESCAPE:
                    goHome = True
                    break
                    # show help screen
                elif event.key == pygame.K_h:
                    goHome = True
                    screen.fill(black)
                    screen.blit(helpScreen, (0, 0))
                    pygame.display.update()
            # escape help screen
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_h:
                    screen.fill(black)
                    screen.blit(titleScreen, (0, 0))
                    pygame.display.update()
            # start/restart game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                startGame()
                gameOver = False
                currentScore = 0
                goHome = False
        # Code below assists asteroids to not bug out
        time.sleep(0.025)
        wipe()
        ship(rocketX)
        asteroid(x, difficulty, newLocation)
        if difficulty==1:
            printDifficulty="Easy"
        elif difficulty==2:
            printDifficulty="Medium (x2)"
        elif difficulty==3:
            printDifficulty="Hard (x3)"
        textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
        screen.blit(textScore, (110, 0))
        show()
        newLocation += 12.5
        time.sleep(0.005)
        show()


# function to move rocket left


def moveRocketLeft():
    printDifficulty = ""
    global rocketX
    moving = 0
    if difficulty == 1:
        moving = 15
    elif difficulty == 2:
        moving = 10
    elif difficulty == 3:
        moving = 5
    if rocketX > -30:
        wipe()
        ship(rocketX-moving)
        rocketX = rocketX-moving
        asteroid(x, difficulty, newLocation)
        if difficulty == 1:
            printDifficulty = "Easy"
        elif difficulty == 2:
            printDifficulty = "Medium (x2)"
        elif difficulty == 3:
            printDifficulty = "Hard (x3)"
        textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
        screen.blit(textScore, (110, 0))
        show()
    else:
        wipe()
        ship(-30)
        rocketX = -30
        asteroid(x, difficulty, newLocation)
        textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
        screen.blit(textScore, (110, 0))
        show()

# function to move rocket right


def moveRocketRight():
    printDifficulty = ""
    global rocketX
    moving = 0
    if difficulty == 1:
        moving = 15
    elif difficulty == 2:
        moving = 10
    elif difficulty == 3:
        moving = 5
    if rocketX < 230:
        wipe()
        ship(rocketX+moving)
        rocketX = rocketX+moving
        asteroid(x, difficulty, newLocation)
        if difficulty==1:
            printDifficulty="Easy"
        elif difficulty==2:
            printDifficulty="Medium (x2)"
        elif difficulty==3:
            printDifficulty="Hard (x3)"
        textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
        screen.blit(textScore, (110, 0))
        show()
    else:
        wipe()
        ship(230)
        rocketX = 230
        asteroid(x, difficulty, newLocation)
        textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
        screen.blit(textScore, (110, 0))
        show()

# ------------------------------------------------------

# Splash screen, title screen, music loading


pygame.mixer.music.load(music)  # start the music
pygame.mixer.music.play(loops=-1)  # loop the music

# display the splash and main menu screens


screen.blit(splash, (0, 0))
pygame.display.update()
time.sleep(2)
pygame.display.update()
screen.blit(titleScreen, (0, 0))
pygame.display.update()
time.sleep(1)
screen.blit(helpNotification, (0, 0))
pygame.display.update()
time.sleep(1)
screen.fill(black)
screen.blit(titleScreen, (0, 0))
pygame.display.update()
time.sleep(1)
screen.blit(helpNotification, (0, 0))
pygame.display.update()


# rocket animation
def changingRocket(x, y):
    printDifficulty=""
    wipe()
    asteroid(globalX, difficulty, newLocation)
    screen.blit(ship1, (x, y))
    if difficulty == 1:
        printDifficulty = "Easy"
    elif difficulty == 2:
        printDifficulty = "Medium (x2)"
    elif difficulty == 3:
        printDifficulty = "Hard (x3)"
    textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
    screen.blit(textScore, (110, 0))
    show()
    wipe()
    asteroid(globalX, difficulty, newLocation)
    screen.blit(ship2, (x, y))
    textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
    screen.blit(textScore, (110, 0))
    show()
    wipe()
    asteroid(globalX, difficulty, newLocation)
    screen.blit(ship3, (x, y))
    textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
    screen.blit(textScore, (110, 0))
    show()
    wipe()
    asteroid(globalX, difficulty, newLocation)
    screen.blit(ship2, (x, y))
    textScore = font.render(str(currentScore) + " - " + printDifficulty, True, white)
    screen.blit(textScore, (110, 0))
    show()


# explosion function used before game over screen

def explosion():
    wipe()
    time.sleep(1)
    screen.fill(black)
    screen.blit(explosion1, (0,0))
    show()
    time.sleep(0.2)
    screen.fill(black)
    screen.blit(explosion2, (0, 0))
    show()
    time.sleep(0.2)
    screen.fill(black)
    screen.blit(explosion3, (0, 0))
    show()
    time.sleep(0.2)
    screen.fill(black)
    screen.blit(explosion4, (0, 0))
    show()
    time.sleep(0.2)

# main function to start game and end game when the x cords line up with each other


def startGame():
    global difficulty
    global gameOver
    global currentScore
    screen.fill(black)
    screen.blit(background, (0, 0))
    ship(rocketX)
    pygame.display.update()
    while gameOver == False:
        startAsteroids(difficulty)
        currentScore += 1*(difficulty)
        # list below indicates the hitbox of the rocket's X cord
        ranging = [rocketX, rocketX+1, rocketX+2, rocketX+3, rocketX+4, rocketX+5, rocketX+6, rocketX+7, rocketX+8, rocketX+9, rocketX+10, rocketX+11, rocketX+12, rocketX+13, rocketX+14, rocketX+15, rocketX+16, rocketX+17, rocketX+18, rocketX+19, rocketX+20, rocketX+21, rocketX+22, rocketX+23, rocketX+24, rocketX+25, rocketX+26, rocketX+27, rocketX+28, rocketX+29, rocketX+30, rocketX+31, rocketX+32, rocketX+33, rocketX+34, rocketX+35, rocketX+36, rocketX+37, rocketX+38, rocketX+39, rocketX+40, rocketX+41, rocketX+42, rocketX+43, rocketX+44, rocketX+45, rocketX+46, rocketX+47, rocketX+48, rocketX+49, rocketX+50]
        for i in ranging:
            if i == x and newLocation == 250:
                gameOver=True
        if gameOver == True:
            # code below opens file
            file=open('highScore.txt','r+')
            file.seek(0)
            highest = (file.read()).replace("\x00", "")  # replaces null values with nothing
            explosion()  # shows explosion screen
            screen.fill(black)
            # display text and game over screen below
            textScore = font.render(str(currentScore), True, white)
            textHigh = font.render(str(highest), True, white)
            screen.blit(gameOverScreen, (0, 0))
            screen.blit(textScore, (230, 135))
            screen.blit(textHigh, (230, 100))
            show()
            # if loop below replaces the high score with the current score if applicable
            if currentScore>int(highest):
                file.truncate(0)
                file.write(str(currentScore))
                file.close()
            else:
                file.close()
            # small wait, and then returns to title screen
            time.sleep(3)
            screen.fill(black)
            screen.blit(titleScreen, (0,0))
            show()
            currentScore = 0
        elif goHome==True:
            break



# ------------------------------------------------------

# Inputs used for main menu screen


while not done:  # loop to quit game once user pushes X
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # change difficulty
            if event.key == pygame.K_1:
                difficulty = 1
            elif event.key == pygame.K_2:
                difficulty = 2
            elif event.key == pygame.K_3:
                difficulty = 3
                # Move Left
            elif event.key == pygame.K_LEFT:
                moveRocketLeft()
                changingRocket(rocketX, 200)
            elif event.key == pygame.K_RIGHT:
                moveRocketRight()
                changingRocket(rocketX, 200)
                # Escape Key
            elif event.key == pygame.K_ESCAPE:
                screen.fill(black)
                screen.blit(titleScreen, (0, 0))
                pygame.display.update()
                # show help screen
            elif event.key == pygame.K_h:
                goHome=True
                screen.fill(black)
                screen.blit(helpScreen, (0, 0))
                pygame.display.update()
        # escape help screen
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                screen.fill(black)
                screen.blit(titleScreen, (0, 0))
                pygame.display.update()
        # start/restart game
        elif event.type == pygame.MOUSEBUTTONDOWN:
            startGame()
            gameOver = False
            currentScore = 0
            goHome=False

# ------------------------------------------------------
clock.tick(60)  # limited to 60 seconds a frame

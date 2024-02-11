import pygame

# initialises all imported pygame modules
pygame.init()

# introduce sounds
LoseSound = pygame.mixer.Sound("record_scratch-108233.mp3")
StartSound = pygame.mixer.Sound("archi_sonar_03-108206.mp3")
HitSound = pygame.mixer.Sound("infobleep-87963.mp3")

# initialises a "Pypong" window a width of 1000 and a height of 800 pixels
(width, height) = (1500, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyPong")

# determines where the player and the enemy are
PlayerXpos = 100
EnemyXpos = 1400
EnemyYpos = 300

# determines where the ball is and where it is going
BallXpos = 750
BallYpos = 300
BallMotionX = 1
BallMotionY = 0

StartSound.play()

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clears the screen to all black
    screen.fill((255, 255, 255))

    # finds the Y position of the mouse in a way that places the mouse in the centre of the player paddle
    MouseYpos = pygame.mouse.get_pos()[1] - 60

    # confines the Y position of the mouse to the edges of the window
    if MouseYpos > 400:
        MouseYpos = 400
    elif MouseYpos < 100:
        MouseYpos = 100

    # player mouse controls
    PlayerYpos = MouseYpos

    # works out where the ball will be on the X and Y axis
    PredictedBallX = BallXpos + BallMotionX
    PredictedBallY = BallYpos + BallMotionY

    # checks if the edge of the ball will hit a paddle and reverses the X position whilst adding a tilt based on paddle
    if PredictedBallX > 1388 and -26 < BallYpos - EnemyYpos < 110:
        BallMotionX = BallMotionX * -1
        BallMotionY += (BallYpos - EnemyYpos - 60)/-120
        HitSound.play()
    elif PredictedBallX < 128 and -26 < BallYpos - PlayerYpos < 110:
        BallMotionX = BallMotionX * -1
        BallMotionY += (BallYpos - PlayerYpos - 60)/-120
        HitSound.play()

    # checks if edge of the ball will hit window borders and reverses y momentum
    if PredictedBallY < 148 or PredictedBallY > 448:
        BallMotionY = BallMotionY * -0.5
        HitSound.play()

    # moves the ball along a pixel
    BallXpos += BallMotionX

    # moves the ball along a pixel
    BallYpos += BallMotionY

    # works out the distance between the ball and the paddle to then triangulate a response
    EnemyDistanceFromBall = 1400 - BallXpos

    # paddle brain works out where ball will be
    if EnemyDistanceFromBall < 500:
        IterationsBetweenBallAndPaddle = EnemyDistanceFromBall / BallMotionX
        BallLandingY = IterationsBetweenBallAndPaddle * BallMotionY + BallYpos - 60
        DistanceForPaddleToTravel = BallLandingY - EnemyYpos
        if DistanceForPaddleToTravel < 0:
            DistanceForPaddleToTravel = DistanceForPaddleToTravel * -1
        EnemySpeed = DistanceForPaddleToTravel / IterationsBetweenBallAndPaddle
        if EnemyYpos > BallLandingY:
            EnemyYpos -= EnemySpeed
        else:
            EnemyYpos += EnemySpeed

    # make sure that paddle doesn't go offscreen
    if EnemyYpos > 400:
        EnemyYpos = 400
    elif EnemyYpos < 100:
        EnemyYpos = 100

    # initialises red rectangle for player paddle
    colour = (255, 0, 0)
    pygame.draw.rect(screen, colour, pygame.Rect(PlayerXpos, PlayerYpos, 20, 120))

    # Initialises blue rectangle for enemy paddle
    colour = (0, 0, 255)
    pygame.draw.rect(screen, colour, pygame.Rect(EnemyXpos, EnemyYpos, 20, 120))

    # Initialises green ball to play with
    colour = (0, 255, 0)
    pygame.draw.circle(screen, colour, (BallXpos, BallYpos), 12)

    # updates the screen to prevent smearing
    pygame.display.update()

    if BallXpos < 100:
        LoseSound.play()
        pygame.time.delay(1000)
        running = False

pygame.quit()

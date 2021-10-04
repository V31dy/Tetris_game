import sys

import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

pieceNames = ('I', 'O', 'T', 'S', 'Z', 'J', 'L')

STARTING_LEVEL = 0 #Change this to start a new game at a higher level

MOVE_PERIOD_INIT = 4 #Piece movement speed when up/right/left arrow keys are pressed (Speed is defined as frame count. Game is 60 fps) 

CLEAR_ANI_PERIOD = 4 #Line clear animation speed
SINE_ANI_PERIOD = 120 #Sine blinking effect speed

ROW = (0)
COL = (1)

#Some color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GRAY = (80,80,80)
GRAY = (110,110,110)
LIGHT_GRAY = (150,150,150)
BORDER_COLOR = GRAY
NUM_COLOR = WHITE
TEXT_COLOR = GRAY

blockColors = {
'I' : (19,232,232), #CYAN
'O' : (236,236,14), #YELLOW
'T' : (126,5,126), #PURPLE
'S' : (0,128,0), #GREEN
'Z' : (236,14,14), #RED
'J' : (30,30,201), #BLUE
'L' : (240,110,2) } #ORANGE

#Initial(spawn) block definitons of each piece
pieceDefs = {
'I' : ((1,0),(1,1),(1,2),(1,3)),
'O' : ((0,1),(0,2),(1,1),(1,2)),
'T' : ((0,1),(1,0),(1,1),(1,2)),
'S' : ((0,1),(0,2),(1,0),(1,1)),
'Z' : ((0,0),(0,1),(1,1),(1,2)),
'J' : ((0,0),(1,0),(1,1),(1,2)),
'L' : ((0,2),(1,0),(1,1),(1,2)) }

directions = {
'down' : (1,0),
'right' : (0,1),
'left' : (0,-1),
'downRight' : (1,1),
'downLeft' : (1,-1),
'noMove' : (0,0) }

levelSpeeds = (48,43,38,33,28,23,18,13,8,6,5,5,5,4,4,4,3,3,3,2,2,2,2,2,2,2,2,2,2)
#The speed of the moving piece at each level. Level speeds are defined as levelSpeeds[level]
#Each 10 cleared lines means a level up.
#After level 29, speed is always 1. Max level is 99

baseLinePoints = (0,40,100,300,1200)
#Total score is calculated as: Score = level*baseLinePoints[clearedLineNumberAtATime] + totalDropCount
#Drop means the action the player forces the piece down instead of free fall(By key combinations: down, down-left, down-rigth arrows)

# Class for the game input keys and their status
class GameKeyInput:

    def __init__(self):
        self.xNav = self.KeyName('idle', False)  # 'left' 'right'
        self.down = self.KeyName('idle', False)  # 'pressed' 'released'
        self.rotate = self.KeyName('idle', False)  # 'pressed' //KEY UP
        self.cRotate = self.KeyName('idle', False)  # 'pressed' //KEY Z
        self.enter = self.KeyName('idle', False)  # 'pressed' //KEY Enter
        self.pause = self.KeyName('idle', False)  # 'pressed' //KEY P
        self.restart = self.KeyName('idle', False)  # 'pressed' //KEY R

    class KeyName:

        def __init__(self, initStatus, initTrig):
            self.status = initStatus
            self.trig = initTrig


# Class for the game's timing events
class GameClock:

    def __init__(self):
        self.frameTick = 0  # The main clock tick of the game, increments at each frame (1/60 secs, 60 fps)
        self.pausedMoment = 0
        self.move = self.TimingType(MOVE_PERIOD_INIT)  # Drop and move(right and left) timing object
        self.fall = self.TimingType(levelSpeeds[STARTING_LEVEL])  # Free fall timing object
        self.clearAniStart = 0

    class TimingType:

        def __init__(self, framePeriod):
            self.preFrame = 0
            self.framePeriod = framePeriod

        def check(self, frameTick):
            if frameTick - self.preFrame > self.framePeriod - 1:
                self.preFrame = frameTick
                return True
            return False

    def pause(self):
        self.pausedMoment = self.frameTick

    def unpause(self):
        self.frameTick = self.pausedMoment

    def restart(self):
        self.frameTick = 0
        self.pausedMoment = 0
        self.move = self.TimingType(MOVE_PERIOD_INIT)
        self.fall = self.TimingType(levelSpeeds[STARTING_LEVEL])
        self.clearAniStart = 0

    def update(self):
        self.frameTick = self.frameTick + 1


# Class for the blocks of the moving piece. Each piece is made of 4 blocks in Tetris game
class MovingBlock:

    def __init__(self):
        self.currentPos = self.CurrentPosClass(0, 0)
        self.nextPos = self.NextPosClass(0, 0)

    class CurrentPosClass:

        def __init__(self, row, col):
            self.row = row
            self.col = col

    class NextPosClass:

        def __init__(self, row, col):
            self.row = row
            self.col = col


# Main program
key = GameKeyInput()
gameClock = GameClock()

pygame.quit()
sys.exit()
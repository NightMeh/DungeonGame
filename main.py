import dungeon
import roomscript
import pygame
import player
import levelmanager

SCREENWIDTH = 1280
SCREENHEIGHT = 720
screen=pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

screen.fill([0, 0, 0])
pygame.display.flip()

testroom = dungeon.Dungeon(10,9,16,80)
testroom.createdungeon(screen)
user = player.Player(0)
clock = pygame.time.Clock()
run = True
manager = levelmanager.LevelManager(user,testroom.room)

while run:
    if manager.currentscreen == "map":
        manager.map(testroom,screen,user,clock)
    elif manager.currentscreen == "room":
        manager.room(screen,clock)
    elif manager.currentscreen == "quit":
        run = False
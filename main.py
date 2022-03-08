import pygame

import dungeon
import levelmanager
import player
import roomscript

SCREENWIDTH = 1280
SCREENHEIGHT = 720
screen=pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

screen.fill([0, 0, 0])
pygame.display.flip()

testroom = dungeon.Dungeon(30,9,16,80)
testroom.createdungeon(screen)
user = player.Player(0)
clock = pygame.time.Clock()
run = True
manager = levelmanager.LevelManager(user,testroom.room)
testroom.mapsetup()

while run:
    if manager.currentscreen == "map":
        manager.map(testroom,screen,user,clock)
    elif manager.currentscreen == "room":
        manager.room(screen,clock,user,testroom)
    elif manager.currentscreen == "quit":
        run = False

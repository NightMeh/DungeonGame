import dungeon
import roomscript
import pygame
import player
import levelmanager

SCREENWIDTH = 600
SCREENHEIGHT = 800
screen=pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
screen.fill([200, 200, 255])
pygame.display.flip()

testroom = dungeon.Dungeon(10,11,11,50)
testroom.createdungeon(screen)
testroom.drawtempgrid(screen)
user = player.Player(0)
clock = pygame.time.Clock()
run = True
manager = levelmanager.LevelManager(user,testroom.room)

while run:
    if manager.currentscreen == "map":
        manager.map(testroom,screen,user,clock)
    elif manager.currentscreen == "room":
        manager.room(screen,clock)
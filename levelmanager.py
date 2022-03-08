import pygame
from dungeon import World
from dungeon import Dungeon
class LevelManager:
    def __init__(self,user,room):
        self.player = user
        self.lvl = 1
        self.currentlayout = room
        self.currentscreen = "map"
        self.ifBattle = False

    def updateMap(self,dungeon,screen,user):
        for x in range(len(dungeon.room)):
            if dungeon.room[x].roomtype == "entrance":
                dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[2])
            elif dungeon.room[x].roomtype == "chest":
                dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[3])
            elif dungeon.room[x].roomtype == "exit":
                dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[4])
            elif dungeon.room[x].cleared == False:
                dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[1])
            elif dungeon.room[x].cleared == True and dungeon.room[x].roomtype == "battle":
                dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[5])
            elif dungeon.room[x].cleared == True and (dungeon.room[x].roomtype != "entrance" or "chest" or "exit" or "battle"):
                dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[6])
            if dungeon.room[x].roomlocation == dungeon.room[user.currentroom].roomlocation:
                dungeon.drawimage(screen,dungeon.room[user.currentroom].roomlocation,dungeon.roomlist[0])
        return False

    def updateWorld(self,world,screen,user):
        world.drawtempgrid
        

    def map(self,dungeon,screen,user,clock):
        map = True
        screen.fill([0, 0, 0])
        needUpdate = True
        dungeon.drawcorridors(screen)
        while map:
            if needUpdate == True:
                needUpdate = self.updateMap(dungeon,screen,user)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.currentscreen = "quit"
                    map = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    dungeon.openroom(user)
                    needUpdate = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.currentscreen = "room"
                        map = False
                    elif event.key == pygame.K_w:
                        dungeon.room[user.currentroom].cleared = True
                        needUpdate = True
        clock.tick(60)

    def room(self,screen,clock,user,dungeon):
        screen.fill([0, 0, 0])
        currentroom = World(dungeon.nrooms,dungeon.blockheight,dungeon.blockwidth,dungeon.block_size)
        currentroom.CreateWorld(screen)
        pygame.display.flip()
        room = True
        while room:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.currentscreen = "quit"
                    room = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.currentscreen = "map"
                        room = False
        clock.tick(60)
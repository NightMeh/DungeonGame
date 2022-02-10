import pygame
class LevelManager:
    def __init__(self,user,room):
        self.player = user
        self.lvl = 1
        self.currentlayout = room
        self.currentscreen = "map"
        self.ifBattle = False
        

    def map(self,dungeon,screen,user,clock):
        map = True
        screen.fill([0, 0, 0])
        needUpdate = True
        dungeon.drawcorridors(screen)
        while map:
            if needUpdate == True:
                for x in range(len(dungeon.room)):
                    if dungeon.room[x].roomtype == "entrance":
                        dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[2])
                    if dungeon.room[x].roomlocation == dungeon.room[user.currentroom].roomlocation:
                        dungeon.drawimage(screen,dungeon.room[user.currentroom].roomlocation,dungeon.roomlist[0])
                        needUpdate = False
                    elif dungeon.room[x].roomlocation != dungeon.room[user.currentroom].roomlocation and dungeon.room[x].roomtype != "entrance":
                        dungeon.drawimage(screen,dungeon.room[x].roomlocation,dungeon.roomlist[1])
                        needUpdate = False
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
                        print(user.currentroom,"has been cleared")
                        print(dungeon.room[user.currentroom].cleared)
        clock.tick(60)

    def room(self,screen,clock):
        screen.fill([0, 0, 0])
        room = True
        while room:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.currentscreen = "quit"
                    map = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.currentscreen = "map"
                        room = False
        clock.tick(60)
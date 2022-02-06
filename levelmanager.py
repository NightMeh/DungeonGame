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
        screen.fill([200, 200, 255])
        dungeon.drawtempgrid(screen)
        dungeon.drawrooms(screen)
        while map:
            for x in range(len(dungeon.room)):
                if dungeon.room[x].roomlocation == dungeon.room[user.currentroom].roomlocation:
                    dungeon.drawdot(screen,dungeon.room[user.currentroom].roomlocation,[255,0,0])
                else:
                    dungeon.drawdot(screen,dungeon.room[x].roomlocation,[0,0,0])
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    dungeon.openroom(user)
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
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.currentscreen = "map"
                        room = False
        clock.tick(60)
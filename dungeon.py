import pygame
import random
import roomscript

class Dungeon:
  def __init__(self,rooms,blockheight,blockwidth,block_size):
    self.blockheight = blockheight
    self.blockwidth = blockwidth
    self.block_size = block_size
    self.nrooms = rooms-3
    self.roomloc = []
    self.worlddata = []
    self.room = []

  def drawtempgrid(self,screen):
    for y in range(self.blockheight):
      for x in range(self.blockwidth):
        pygame.draw.rect(screen, [255,255,255], pygame.Rect(x*self.block_size,y*self.block_size,self.block_size,self.block_size),1)
    pygame.display.flip()

  def getworlddata(self):
    for w in range(0,self.blockwidth):
      for h in range(0,self.blockheight):
        temp = [w,h]
        self.worlddata.append(temp)

    return

  def findroomnumbylocation(self,location):
    for x in range(len(self.room)):
      if location == self.room[x].roomlocation:
        return x

  def drawmiddleroom(self,screen):
    #pygame.draw.rect(screen, [255,0,0], pygame.Rect((SCREENHEIGHT/2)-(self.block_size/2), (SCREENWIDTH/2)-(self.block_size/2), self.block_size, self.block_size),1)
    wdlen = len(self.worlddata)
    midx = int((self.worlddata[wdlen-1][0])/2)
    midy = int((self.worlddata[wdlen-1][1])/2)
    pygame.display.flip()
    midloc = [midx,midy]
    print(midloc)
    roomcount = 1
    self.room.append(roomscript.Room(roomcount,"room",[midx,midy]))
    return midloc,roomcount

  def drawdot(self,screen,location,colour):
    locx = location[0]
    locy = location[1]
    pygame.draw.rect(screen, colour, (((locx)*self.block_size)+self.block_size/4,((locy)*self.block_size)+self.block_size/4,self.block_size/2,self.block_size/2),0)
    pygame.display.flip()

  def findsurroundingsquares(self,centre):
    surroundlist = []
    surroundlist.append([centre[0]-1,centre[1]])
    surroundlist.append([centre[0]+1,centre[1]])
    surroundlist.append([centre[0],centre[1]-1])
    surroundlist.append([centre[0],centre[1]+1])
    return surroundlist

  def chooserandom(self,surroundlist):
    #print("surroundlist",)
    randomnum = random.randint(0,len(surroundlist)-1)
    return surroundlist[randomnum]

  def addroom(self,surroundlist,screen,roomcount):
    surroundlistsecond = []
    tries = 0
    failed = False
    while len(surroundlistsecond) != 3:
      tries += 1
      if len(surroundlist) != 0:
        newroomloc = self.chooserandom(surroundlist) #choose a random place around the established room
      else:
        failed = True
        newroomloc = []
        return newroomloc,roomcount,failed
      surroundlistsecond = self.findsurroundingsquares(newroomloc) #find the places around the new roomloc
      #print("surroundlistsecond before for", newroomloc,surroundlistsecond)
      for element in self.roomloc: #remove the rooms around new roomloc where are other rooms
          if element in surroundlistsecond:
            surroundlistsecond.remove(element) 
      if len(surroundlistsecond) < 3:
        surroundlist.remove(newroomloc)

      #print("surroundlistsecond for", newroomloc,surroundlistsecond)
      if tries == 5:
        #print("failed to place room at",newroomloc)
        failed = True
        return newroomloc,roomcount,failed


    roomcount+=1
    self.drawdot(screen,newroomloc,[0,0,0])
    #print("randchosen",newroomloc)
    surroundlist.remove(newroomloc)
    #print("roomloc b4",roomloc)
    self.roomloc.append(newroomloc)
    #print("roomloc after",roomloc)
    self.room.append(roomscript.Room(roomcount,"test",newroomloc))
    return newroomloc,roomcount,failed

  def createdungeon(self,screen):
    self.getworlddata()
    midloc,roomcount = self.drawmiddleroom(screen)
    self.roomloc.append(midloc)
    self.drawdot(screen,midloc,[0,0,0])
    surroundlist = self.findsurroundingsquares(midloc)
    #print("surroundlist",surroundlist)
    for x in range(2):
      randroom,roomcount,failed = self.addroom(surroundlist,screen,roomcount)

    roomamountcount = 0

    while roomamountcount != self.nrooms:
      randroom = self.chooserandom(self.roomloc) #find a random room
      surroundlist = self.findsurroundingsquares(randroom) #find surround rooms from that
      for element in self.roomloc: #remove the places with rooms already
        if element in surroundlist:
          surroundlist.remove(element)
      #print(randroom)
      randroom,roomcount,failed = self.addroom(surroundlist,screen,roomcount)
      if not failed:
        roomamountcount+=1

    return

  def pressinsquare(self):
    position = pygame.mouse.get_pos()
    print(position)
    xloc = (position[0] // self.block_size)
    yloc = (position[1] // self.block_size)
    print(xloc,yloc)
    location = [xloc,yloc]
    return location

  def openroom(self,user):
    location = self.pressinsquare()
    surroundlist = self.findsurroundingsquares((self.room[user.currentroom].roomlocation))
    if location in self.roomloc and location in surroundlist:
      for x in range(len(self.room)):
        if self.room[x].roomlocation == location:
          user.currentroom = x
    else:
      print("nah")
    return

  def drawrooms(self,screen):
    for x in range(self.nrooms+3):
      self.drawdot(screen,self.room[x].roomlocation,[0,0,0])
      
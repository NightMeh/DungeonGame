from email.generator import Generator
import pygame
import random
import roomscript

class Generator:
  def __init__(self,rooms,blockheight,blockwidth,block_size):
    self.blockheight = blockheight
    self.blockwidth = blockwidth
    self.block_size = block_size
    self.randomroomaroundcentre = random.randint(1,4)
    self.nrooms = rooms-self.randomroomaroundcentre
    self.roomloc = []
    self.worlddata = []
    self.room = []
    self.imageconstant = 1.6

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
    self.room.append(roomscript.Room(roomcount,"entrance",[midx,midy],self))
    return midloc,roomcount

  def drawimage(self,screen,location,image):
    locx = location[0]
    locy = location[1]
    #print("drawimageloc",locx,locy)
    offset = (self.block_size - (self.block_size / self.imageconstant))/2
    screen.blit(image, (((locx)*self.block_size)+offset,((locy)*self.block_size)+offset,self.block_size/self.imageconstant,self.block_size/self.imageconstant))
    pygame.display.flip()

  def drawdot(self,screen,location,colour):

    locx = location[0]
    locy = location[1]
    pygame.draw.rect(screen, colour, (((locx)*self.block_size)+self.block_size/4,((locy)*self.block_size)+self.block_size/4,self.block_size/2,self.block_size/2),2)
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




  
  def pressinsquare(self):
    for x in range(len(self.room)):
      if self.room[x].rect.collidepoint(pygame.mouse.get_pos()):
        print(self.room[x].roomlocation,self.room[x].roomnum)
        return self.room[x].roomlocation

  def drawrooms(self,screen):
    for x in range(self.nrooms+3):
      self.drawdot(screen,self.room[x].roomlocation,[0,0,0])
  
  def fillroom(self,screen,location,colour):
    locx = location[0]
    locy = location[1]
    pygame.draw.rect(screen, colour, (locx*self.block_size,locy*self.block_size,self.block_size,self.block_size),0)
    pygame.display.flip()
      
class Dungeon(Generator):
  def __init__(self,rooms,blockheight,blockwidth,block_size):
    Generator.__init__(self,rooms,blockheight,blockwidth,block_size)
    self.newcorridorsize = 32
    unclearedroomimage = pygame.image.load(r'Images\Rooms\UnclearedRoom.png').convert()
    treasureroomimage = pygame.image.load(r'Images\Rooms\Treasure.png').convert()
    entranceroomimage = pygame.image.load(r'Images\Rooms\Entrance.png').convert()
    exitroomimage = pygame.image.load(r'Images\Rooms\Exit.png').convert()
    battleroomimage = pygame.image.load(r'Images\Rooms\Battle.png').convert()
    emptyroomimage = pygame.image.load(r'Images\Rooms\Empty.png').convert()
    currentroomimage = pygame.image.load(r'Images\Rooms\CurrentRoomIcon.png').convert_alpha()
    self.roomlist = [currentroomimage,unclearedroomimage,entranceroomimage,treasureroomimage,exitroomimage,battleroomimage,emptyroomimage]
    for x in range(len(self.roomlist)):
      self.roomlist[x] = pygame.transform.scale(self.roomlist[x],(block_size/self.imageconstant,block_size/self.imageconstant))
    corridor = pygame.image.load(r'Images\Rooms\Corridor\EmptyCorridor.png').convert()
    self.corridorlist = [corridor]
    for x in range(len(self.corridorlist)):
      self.corridorlist[x] = pygame.transform.scale(self.corridorlist[x],(self.newcorridorsize,self.newcorridorsize))

  def drawcorridorimage(self,screen,location,image,roomnum):
    currentlocation = self.room[roomnum].roomlocation
    locx = location[0]
    locy = location[1]
    newlocx = 0
    newlocy = 0
    location = [locx,locy]
    if location == [currentlocation[0],currentlocation[1]-1]:
      #print("north")
      newlocx = (currentlocation[0]*self.block_size + self.block_size/2)-self.newcorridorsize/2
      newlocy = ((currentlocation[1]*self.block_size + self.block_size/2)- (self.block_size/self.imageconstant)/2) - self.newcorridorsize
    elif location == [currentlocation[0]+1,currentlocation[1]]:
      #print("east")
      newlocx = (currentlocation[0]*self.block_size + self.block_size/2)+ (self.block_size/self.imageconstant)/2
      newlocy = (currentlocation[1]*self.block_size + self.block_size/2)-self.newcorridorsize/2
    elif location == [currentlocation[0],currentlocation[1]+1]:
      #print("south")
      newlocx = (currentlocation[0]*self.block_size + self.block_size/2)-self.newcorridorsize/2
      newlocy = (currentlocation[1]*self.block_size + self.block_size/2)+(self.block_size/self.imageconstant)/2
    elif location == [currentlocation[0]-1,currentlocation[1]]:
      #print("west")
      newlocx = ((currentlocation[0]*self.block_size + self.block_size/2)- (self.block_size/self.imageconstant)/2)- self.newcorridorsize
      newlocy = (currentlocation[1]*self.block_size + self.block_size/2)-self.newcorridorsize/2
    
    #print("drawimageloc",locx,locy)
    screen.blit(image, (newlocx,newlocy,self.block_size/self.imageconstant,self.block_size/self.imageconstant))
    pygame.display.flip()
      
  def addroom(self,surroundlist,screen,roomcount):
    surroundlistsecond = []
    tries = 0
    failed = False
    while len(surroundlistsecond) != 3:
      tries += 1
      if len(surroundlist) != 0:
        newroomloc = self.chooserandom(surroundlist) #choose a random place around the established room
        while newroomloc[0] < 0 or newroomloc[1] < 0 or newroomloc[0] >= self.blockwidth or newroomloc[1] >= self.blockheight:
          newroomloc = self.chooserandom(surroundlist)
          tries+=1
          if tries > 4:
            failed = True
            newroomloc = []
            return newroomloc,roomcount,failed

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
    #self.drawdot(screen,newroomloc,[0,0,0])
    #print("randchosen",newroomloc)
    surroundlist.remove(newroomloc)
    #print("roomloc b4",roomloc)
    self.roomloc.append(newroomloc)
    #print("roomloc after",roomloc)
    self.room.append(roomscript.Room(roomcount,"",newroomloc,self))
    return newroomloc,roomcount,failed
  
  def createdungeon(self,screen):
    self.getworlddata()
    midloc,roomcount = self.drawmiddleroom(screen)
    self.roomloc.append(midloc)
    #self.drawdot(screen,midloc,[0,0,0])
    surroundlist = self.findsurroundingsquares(midloc)
    #print("surroundlist",surroundlist)
    for x in range(self.randomroomaroundcentre):
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


  def mapsetup(self):
    roomamount = len(self.room)
    roomlist = []
    for x in range(1,roomamount):
      roomlist.append(x)
    self.room[0].roomtype = "entrance"
    print(roomlist)
    self.room[len(roomlist)].roomtype = "exit"
    roomlist.remove((len(roomlist)))
    print(roomlist)
    for x in range(len(roomlist)):
      self.room[x+1].roomtype = "battle"
    print(len(roomlist))
    print(self.room[0].roomtype)
    

  def drawcorridors(self,screen):
    for x in range(len(self.room)):
      surroundlist2 = []
      surroundlist = self.findsurroundingsquares(self.room[x].roomlocation)
      #print("location",self.room[x].roomlocation)
      for element in self.roomloc: #remove the places with rooms already
        if element in surroundlist and element in self.roomloc:
          surroundlist2.append(element)
      for item in range (len(surroundlist2)):
        self.drawcorridorimage(screen,surroundlist2[item],self.corridorlist[0],x)
        corridor = roomscript.Corridor(type,self.room[x].roomlocation)
        self.room[x].corridors.append(corridor)


class World(Generator):
  def __init__ (self,rooms,blockheight,blockwidth,block_size):
    self.blockheight = blockheight
    self.blockwidth = blockwidth
    self.block_size = block_size
    self.randomroomaroundcentre = random.randint(1,4)
    self.nrooms = rooms-self.randomroomaroundcentre
    self.objectloc = []
    self.worlddata = []
    self.room = []
    self.imageconstant = 1.6
    self.citycount = 3
    self.mountaincluster = 2
    self.mountaincount = 3
      
  def generateMountains(self,screen):
    failcount = 0
    randomlocation = self.chooserandom(self.worlddata)

    self.objectloc.append(randomlocation)

    for x in range(self.mountaincount):
      surroundlist = self.findsurroundingsquares(randomlocation)
      print("surroundlist", surroundlist)
      for element in self.objectloc:
        if element in surroundlist:
          surroundlist.remove(element)
      randomlocaroundcentre = self.chooserandom(surroundlist)
      print(randomlocaroundcentre)

      while randomlocaroundcentre[0] < 0 or randomlocaroundcentre[0] > (self.blockwidth-1) or randomlocaroundcentre[1] < 0 or randomlocaroundcentre[1] > (self.blockheight-1):
        surroundlist.remove(randomlocaroundcentre)
        failcount +=1
        randomlocaroundcentre = self.chooserandom(surroundlist)
        print("failed, new loc",randomlocaroundcentre)
        if failcount == 4:
          return True
      
      self.objectloc.append(randomlocaroundcentre)
      self.fillroom(screen,randomlocation,[150,75,0])
      randomlocation = randomlocaroundcentre
    self.fillroom(screen,randomlocaroundcentre,[150,75,0])
    return False


  def createworld(self,screen):
    self.getworlddata()
    print(self.worlddata)
    self.drawtempgrid(screen)
    midloc,roomcount = self.drawmiddleroom(screen)
    self.drawdot(screen,midloc,[255,255,255])
    for x in range(self.mountaincluster):
      failed = True
      while failed:
        failed = self.generateMountains(screen)
    


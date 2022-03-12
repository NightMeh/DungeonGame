import pygame
class Room:
  def __init__(self,roomnum,roomtype,location,dungeon):
    self.roomnum = roomnum
    self.roomtype = roomtype
    self.roomlocation = location
    self.surroundingroomstotal = []
    self.surroundingrooms = []
    self.cleared = False
    self.corridors = []
    offset = (dungeon.block_size - (dungeon.block_size/dungeon.imageconstant))/2
    self.x = ((location[0])*dungeon.block_size)+(offset)
    self.y = ((location[1])*dungeon.block_size)+(offset)
    self.w = dungeon.block_size/dungeon.imageconstant
    self.h = dungeon.block_size/dungeon.imageconstant
    self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    #print("roomcreated",roomnum,roomtype,location)

  def findsurroundingroomstotal(self):
    northpos = [(self.roomlocation[0]),(self.roomlocation[1]-1)]
    southpos = [(self.roomlocation[0]),(self.roomlocation[1])+1]
    eastpos = [(self.roomlocation[0]+1),(self.roomlocation[1])]
    westpos = [(self.roomlocation[0]-1),(self.roomlocation[1])]
    #print(northpos,southpos,eastpos,westpos)
    self.surroundingroomstotal.append(northpos)
    self.surroundingroomstotal.append(eastpos)
    self.surroundingroomstotal.append(southpos)
    self.surroundingroomstotal.append(westpos)

    #print(self.surroundingroomstotal)

  def checkforrooms(self,roomloc):

    for element in roomloc:
      if element in self.surroundingroomstotal:
        try:
          self.surroundingrooms.append(element)
        except:
          continue

class City:
  def __init__(self,location):
    self.location = location
    self.alive = True



class Corridor:
  def __init__(self,type,centre):
      self.type = type
      self.location = [centre]
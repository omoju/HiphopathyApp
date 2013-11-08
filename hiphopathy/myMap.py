class Song:
   'Common base class for all songs'
   songCount = 0

   def __init__(self, name):
      self.name = name
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Song(s) %d" % Song.songCount

   def displaySong(self):
      print "Name : ", self.name
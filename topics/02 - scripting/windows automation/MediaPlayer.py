import os, sys
from file import File
from pywinauto.application import Application

class MediaPlayer(object):
	
	def __init__(self, outputFileLocation):
		self.outputFileLocation = outputFileLocation
		self.playList = []
		self.app = Application()
	
	#adds a media file to the current playlist
	def addMedia(self, aFile):
		
		#make sure that aFile contains a valid file location
		try:
			if os.path.getsize(aFile.location) > 0:
				self.playList.append(aFile)
		except:
			pass
		
	#removes a file from the current playlist
	def removeMedia(self, aFile):
		self.playList.remove(aFile)
		
	#outputs the playlist to a file
	def toM3U(self):
		out = open(self.outputFileLocation, 'w')
		out.write("#EXTM3U\n\n")
		for mediaFile in self.playList:
			titleStr = "#EXTINF:-1, " + mediaFile.name + "\n"
			locStr = mediaFile.location + "\n\n"
			out.write(titleStr)
			out.write(locStr)	
	
	#plays the current playlist
	def play(self):
		self.toM3U()
		connectionString = r"C:\Program Files\Windows Media Player\wmplayer.exe"
		connectionString += r" /play /fullscreen" + self.outputFileLocation
		self.app.start(connectionString)
	
	def stop(self):
		pass

if __name__ == '__main__':
	player = MediaPlayer( os.getcwd() + r"\selfTest.m3u")
	aFile = File()
	aFile.location = r"C:\WINDOWS\Media\tada.wav"
	aFile.name = "tada"
	player.addMedia(aFile)
	aFile = File()
	aFile.location = r"C:\WINDOWS\Media\chimes.wav"
	aFile.name = "chimes"
	player.addMedia(aFile)
	player.play()


"""
app["Windows Media Player"].TypeKeys("^u")

"""
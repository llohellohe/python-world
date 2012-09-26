#!/usr/bin/python
song='''
This is a song for you!
This is not a song for me

'''
songStore=file('/tmp/song','w')
songStore.write(song)
songStore.close()


readSong=file('/tmp/song')

while True:
	line=readSong.readline()
	if(len(line)==0):
		break
	print line





script=file("list.py")

while True:
	line=script.readline()
	if (len(line)==0):
		break
	print line
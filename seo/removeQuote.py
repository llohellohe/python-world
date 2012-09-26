#!/bin/python
# coding=utf8
"""
此程序会去除fileName文件中带有双引号的关键字，
去除双引号后,
将其保存到fileName-result文件中
"""

import sys

if(len(sys.argv)<2):
	print "ARGUMENT:filepath"
	sys.exit(0)

fileName=sys.argv[1]
print "FILE NAME IS ",fileName

file=open(fileName)

resultFile=open(fileName+"-result",'w')

for line in file:
	line=line.strip()
	lenOfLine=len(line)
	if(lenOfLine>2 and line[0]=="\"" and line[lenOfLine-1]=="\""):
		resultFile.write(line[1:lenOfLine-1]+"\n")
	else:
		resultFile.write(line+"\n")


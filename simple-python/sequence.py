#!/bin/python
name=["o2","yangqi"]
name.append("++");

newname=name[1:3]
newname.append("new-name")
for n in newname:
	print "name in newname ",n

for n in name:
	print "name in name ",n


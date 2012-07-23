#!/usr/bin/python
class Yangqi:
	count=0
	def __init__(self,name):
		self.name=name
		Yangqi.count=Yangqi.count+1
	def sayName(self):
		print "I am ",self.name
		print "Count is ",Yangqi.count

y=Yangqi('yangqi')
y.sayName()

o=Yangqi('o2')
o.sayName()

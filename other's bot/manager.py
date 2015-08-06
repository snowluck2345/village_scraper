import sys
import math
import subprocess
import re

# 1/unitspeed in tw (what to multiply by)
unitspeed = 1.5
# minutes per field (doubled because of two-way travel)
lcspeed = 10 *2
axespeed = 18 *2

minaxes = 30
minlc = 8

home = None
theHaulMin = 800

def getDistance(coord1, coord2):
		# return euclidian distance to other coord
		xOff = coord1.x - coord2.x
		yOff = coord1.y - coord2.y
		return math.sqrt(xOff*xOff + yOff*yOff)

class coordinate:
	""" vill coordinate utility class """

	def __init__(self, x, y, h, spec):
		self.toSend = False
		self.sent = False
		self.spec = spec
		self.x = int(x)
		self.y = int(y)
		self.haul = int(h)
		self.axes = 0
		self.spears = 0
		self.lc = 0
		self.swords = 0
		if home != None:
			self.axetime = axespeed * getDistance(self,home)
			self.lctime = lcspeed * getDistance(self,home)
		else:
			self.axetime = 0
			self.lctime = 0

	def display(self):
		print str(self.x) + '|' + str(self.y) + " : " + str(self.haul) + " "+ str(self.axetime) + " " + str(self.lctime)+ " " + str(c.spec)

def readCoordinates(filename):
	""" x|y|n
	x is x coord
	y is y coord
	n is minimum haul amount """
	global home
	coords = []
	speccoords = []

	f = open(filename)
	s = f.readline()
	s = s.strip().split("|")
	print s
	home = coordinate(s[0],s[1], 0, False)

	for line in f:
		s = line.strip().split("|")
		if len(s) > 3:
			speccoords.append(coordinate(s[0],s[1],s[2], True))
		else:
			coords.append(coordinate(s[0],s[1],s[2], False))

	speccoords = sorted(speccoords, key=lambda c: c.axetime)
	coords = sorted(coords, key=lambda c: c.axetime)

	return speccoords + coords


def findTroopRatio(haulA, haulB, countA, countB, minB, fullHaul):
	if fullHaul == 0:
		fullHaul = theHaulMin #TODO::: may want to change the default raid size
	aToSend = 0
	bToSend = minB

	if countB < minB:
		return (0,0)

	if countA > 0 and countB > 0:
		while haulA*aToSend + haulB*bToSend < fullHaul:
			#print float(aToSend) / countA , float(bToSend) / countB, aToSend,bToSend
			if float(aToSend) / countA > float(bToSend) / countB:
				bToSend+=1
			else:
				aToSend+=1
			if (float(aToSend) / countA) > 1 or (float(bToSend) / countB) > 1:
				return (0,0) # we don't have enough troops to hit the required haul amt
	elif countB > 0: # we have no A units
		while haulB*bToSend < fullHaul:
			bToSend += 1
			if (float(bToSend) / countB) > 1:
				return (0,0)

	elif countA > 0: # we have no B units
		return (0,0) # can't have minaxes amount


	return (aToSend,bToSend)


if __name__ == "__main__":
	# first arg is min time in minutes
	# second arg is max time in minutes
	# third arg is filename of valid villages, first coord is home village
	# fourth arg is minY, fifth is maxY
	minTimeCutoff = int(sys.argv[1])
	maxTimeCutoff = int(sys.argv[2])
	coordinates = readCoordinates(sys.argv[3])
	minY = int(sys.argv[4])
	maxY = int(sys.argv[5])
	#for c in coordinates:
	#	c.display()
	

	# determine axe-speed and lc-speed candidates
	axetargs = []
	lctargs = []
	for c in coordinates:
		if c.axetime > minTimeCutoff and c.axetime < maxTimeCutoff and c.y > minY and c.y <= maxY:
			axetargs.append(c)
		else:
			print c.y, minY,maxY
		if c.lctime > minTimeCutoff and c.lctime < maxTimeCutoff and c.y > minY and c.y <= maxY:
			lctargs.append(c)

	#get troop numbers here 

	oldid = 18518
	args = [oldid]
	p = subprocess.Popen(['osascript', 'getUnitCounts.scpt'] + [str(arg) for arg in args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	bigstring, err = p.communicate()
	
	m = re.search("<tr>\s*<td>From this village</td>\s*(.+)\s*</tr>", bigstring)
	if m:
		units = m.group(1)
		listy = re.findall(r'\d+', units)
	else:
		print "missed"

	print listy
	spears = int(listy[0])
	axes = int(listy[2])
	lc = int(listy[4])

	#spears = 52
	#axes = 1473
	#lc = 448
	print spears,axes,lc

	spearsUsed = 0
	axesUsed = 0
	lcUsed = 0

	while True:
		for c in axetargs:
			#c.display()

			# find the ratio that is over the haul amount
			(spearToSend, axeToSend) = findTroopRatio(25, 10, spears-spearsUsed, axes-axesUsed, minaxes, c.haul)
			spearsUsed += spearToSend
			axesUsed += axeToSend
			#print "sent:",spearToSend, axeToSend, "remaining:",spears-spearsUsed,axes-axesUsed
			if spearToSend > 0 or axeToSend > 0:
				c.toSend = True
				c.spears = spearToSend
				c.axes = axeToSend

		for c in lctargs:
			if not c.toSend:
				#c.display()
				(derp, lcToSend) = findTroopRatio(0, 80, 0, lc-lcUsed, minlc, c.haul)
				lcUsed += lcToSend
				#print "sent:",lcToSend, "remaining:",lc-lcUsed
				if lcToSend > 0:
					c.toSend = True
					c.lc = lcToSend

		# display the summary and see if okay with user :)
		print "to occur: \t\tspears\taxes\tlc\thaul\taxetime"
		for c in axetargs + lctargs:
			s = ""
			if c.toSend:
				s += "   x\t"
			else:
				s += "\t"
			s += str(c.x) +"|"+str(c.y) +"\t\t"+str(c.spears)+"\t"+str(c.axes)+"\t"+str(c.lc)+"\t"+str(c.haul)+"\t"+str(c.axetime)
			print s
		print "\n\tremaining:\t" + str(spears-spearsUsed) + "\t" + str(axes-axesUsed) + "\t" + str(lc-lcUsed)+"\n"

		x = input('is this okay? (0 if yes, new haul amount if no)  ' + str(theHaulMin) + '  ')

		if int(x) == 0:
			break
		else:
			#reset basically
			for c in lctargs:
				c.lc = 0
				c.axes = 0
				c.spears = 0
				c.toSend = False
			spearsUsed = 0
			axesUsed = 0
			lcUsed = 0
			theHaulMin = int(x)

	# TODO ::: send the units

	for c in axetargs + lctargs:
		if c.toSend and not c.sent:
			c.sent = True
			c.display()

			args = [oldid, c.spears, c.swords, c.axes, c.lc, 0, c.x, c.y]
			p = subprocess.Popen(['osascript', 'sendUnits.scpt'] + [str(arg) for arg in args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			out, err = p.communicate()
			"""
			if p.returncode:
		  		print 'ERROR:', err
		  	else:
		  		print "normal:",int(out)
		  	"""




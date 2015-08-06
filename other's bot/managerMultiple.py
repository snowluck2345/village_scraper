import sys
import math
import subprocess
import re

#,367|508|20515

# minutes per field (doubled because of two-way travel)
lcspeed = 10 *2
hcspeed = 11 *2
axespeed = 18 *2
swordspeed = 22 *2

minaxes = 30
minswords = 40
minlc = 8
minhc = 10

farmers = []
theHaulMin = 800

def getDistance(coord1, coord2):
		# return euclidian distance to other coord
		xOff = coord1.x - coord2.x
		yOff = coord1.y - coord2.y
		return math.sqrt(xOff*xOff + yOff*yOff)

class farmer:
	""" utility class for the villages from which to farm"""

	def __init__(self, x, y, id, name):
		self.formatedname = name + (" " * (30-len(name)))
		self.name = name
		self.x = int(x)
		self.y = int(y)
		self.id = int(id)
		self.swordtargs = []
		self.axetargs = []
		self.lctargs = []
		self.hctargs = []
		self.swordCount = 0
		self.spearCount = 0
		self.axeCount = 0
		self.lcCount = 0
		self.hcCount = 0
		self.minTimeCutoff = 0
		self.maxTimeCutoff = 0

	def display(self):
		print "farmer:  " + str(self.formatedname) + " (" + str(self.x) + "|" + str(self.y) + ")  id: " + str(self.id)

class coordinate:
	""" vill coordinate utility class """

	def __init__(self, x, y, h, spec):
		self.toSend = False
		self.sender = 0
		self.sent = False
		self.spec = spec
		self.x = int(x)
		self.y = int(y)
		self.haul = int(h)
		self.axes = 0
		self.spears = 0
		self.lc = 0
		self.hc = 0
		self.swords = 0
		self.axetimes = {}
		self.lctimes = {}
		self.swordtimes = {}
		self.hctimes = {}
		for f in farmers:
			self.axetimes[f.id] = axespeed * getDistance(self,f)
			self.lctimes[f.id] = lcspeed * getDistance(self,f)
			self.swordtimes[f.id] = swordspeed * getDistance(self,f)
			self.hctimes[f.id] = hcspeed * getDistance(self,f)

	def display(self):
		s = str(self.x) + '|' + str(self.y) + " : " + str(self.haul) + " " + str(c.spec) + " "
		for f in farmers:
			s += str(self.swordtimes[f.id]) + " " + str(self.axetimes[f.id]) + " " + str(self.lctimes[f.id])+ " "
		print s

def readCoordinates(filename):
	""" x|y|n
	x is x coord
	y is y coord
	n is minimum haul amount """
	global farmers
	coords = []
	speccoords = []

	f = open(filename)
	s = f.readline()
	s = s.strip().split(",")
	
	for str in s:
		str = str.split("|")
		farmers.append(farmer(str[0],str[1],str[2],str[3]))
	
	print " "
	for h in farmers:
		h.display()
	print " "

	for line in f:
		s = line.strip().split("|")
		if len(s) > 3:
			speccoords.append(coordinate(s[0],s[1],s[2], True))
		else:
			coords.append(coordinate(s[0],s[1],s[2], False))

	return (speccoords, coords)


def findTroopRatio(haulA, haulB, countA, countB, minB, fullHaul):
	if fullHaul < theHaulMin:
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
	"""
	print "test:"
	c1 = coordinate(200,200,100,False)
	c2 = coordinate (300,300,200,True)
	f1 = farmer(1,2,3)
	f2 = farmer(4,5,6)

	f1.axetargs.append(c1)
	f1.axetargs.append(c2)
	f2.axetargs.append(c1)
	f2.axetargs.append(c2)

	print "initial info l1:",f1.axetargs[0].toSend, f1.axetargs[1].toSend, "l2:", f2.axetargs[0].toSend, f2.axetargs[1].toSend
	f1.axetargs[0].toSend = True
	print "after info l1:",f1.axetargs[0].toSend, f1.axetargs[1].toSend, "l2:", f2.axetargs[0].toSend, f2.axetargs[1].toSend
	sys.exit()
	"""

	# only arg is filename of valid villages, first coord is home village

	(speccoordinates, coordinates) = readCoordinates(sys.argv[1])

	for f in farmers:
		x = input("enter min time for " + str(f.formatedname))
		f.minTimeCutoff = x
		x = input("enter max time for " + str(f.formatedname))
		f.maxTimeCutoff = x

	print ""
	
	# set up each farmer's sword, axe, and lc candidates
	for f in farmers:
		for c in sorted(speccoordinates, key=lambda d: d.axetimes[f.id]):
			if c.swordtimes[f.id] > f.minTimeCutoff and c.swordtimes[f.id] < f.maxTimeCutoff:
				f.swordtargs.append(c)
			if c.axetimes[f.id] > f.minTimeCutoff and c.axetimes[f.id] < f.maxTimeCutoff:
				f.axetargs.append(c)
			if c.lctimes[f.id] > f.minTimeCutoff and c.lctimes[f.id] < f.maxTimeCutoff:
				f.lctargs.append(c)
			if c.hctimes[f.id] > f.minTimeCutoff and c.hctimes[f.id] < f.maxTimeCutoff:
				f.hctargs.append(c)
		for c in sorted(coordinates, key=lambda d: d.axetimes[f.id]):
			if c.swordtimes[f.id] > f.minTimeCutoff and c.swordtimes[f.id] < f.maxTimeCutoff:
				f.swordtargs.append(c)
			if c.axetimes[f.id] > f.minTimeCutoff and c.axetimes[f.id] < f.maxTimeCutoff:
				f.axetargs.append(c)
			if c.lctimes[f.id] > f.minTimeCutoff and c.lctimes[f.id] < f.maxTimeCutoff:
				f.lctargs.append(c)
			if c.hctimes[f.id] > f.minTimeCutoff and c.hctimes[f.id] < f.maxTimeCutoff:
				f.hctargs.append(c)

	"""
	for f in farmers:
		print '\n\n'
		f.display()
		print "sword:"
		for t in f.swordtargs:
			t.display()
		print "axe:"
		for t in f.axetargs:
			t.display()
		print "lc:"
		for t in f.lctargs:
			t.display()
		print "hc"
		for t in f.hctargs:
			t.display()
	"""

	#get troop numbers here
	print "\tspears\taxes\tswords\tlc\thc"
	for f in farmers:
		if f.maxTimeCutoff > 0:
			args = [f.id]
			p = subprocess.Popen(['osascript', 'getUnitCounts.scpt'] + [str(arg) for arg in args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			bigstring, err = p.communicate()
			
			m = re.search("<tr>\s*<td>From this village</td>\s*(.+)\s*</tr>", bigstring)
			if m:
				units = m.group(1)
				listy = re.findall(r'\d+', units)
			else:
				print "missed"

			f.spearCount = int(listy[0])
			f.swordCount = int(listy[1])
			f.axeCount = int(listy[2])
			f.lcCount = int(listy[4])
			f.hcCount = int(listy[5])
			print str(f.x)+"|"+str(f.y)+":",f.spearCount,"\t",f.axeCount,"\t",f.swordCount,"\t",f.lcCount,"\t",f.hcCount


	for f in farmers:
		spearsUsed = 0
		axesUsed = 0
		lcUsed = 0
		swordsUsed = 0
		hcUsed = 0

		while True:
			if f.axeCount > f.swordCount:
				# offensive village, so send spears with axes, lc
				for c in f.axetargs:
					if not c.toSend:
						#c.display()

						# find the ratio that is over the haul amount
						(spearToSend, axeToSend) = findTroopRatio(25, 10, f.spearCount-spearsUsed, f.axeCount-axesUsed, minaxes, c.haul)
						spearsUsed += spearToSend
						axesUsed += axeToSend
						#print "sent:",spearToSend, axeToSend, "remaining:",spears-spearsUsed,axes-axesUsed
						if spearToSend > 0 or axeToSend > 0:
							c.toSend = True
							c.spears = spearToSend
							c.axes = axeToSend
							c.sender = f.id

				for c in f.lctargs:
					if not c.toSend:
						#c.display()
						(derp, lcToSend) = findTroopRatio(0, 80, 0, f.lcCount-lcUsed, minlc, c.haul)
						lcUsed += lcToSend
						#print "sent:",lcToSend, "remaining:",lc-lcUsed
						if lcToSend > 0:
							c.toSend = True
							c.lc = lcToSend
							c.sender = f.id
			else:
				# defensive village, so send spears with swords, hc
				for c in f.swordtargs:
					if not c.toSend:
						(spearToSend, swordToSend) = findTroopRatio(25, 15, f.spearCount-spearsUsed, f.swordCount-swordsUsed, minswords, c.haul)
						spearsUsed += spearToSend
						swordsUsed += swordToSend

						if spearToSend > 0 or swordToSend > 0:
							c.toSend = True
							c.spears = spearToSend
							c.swords = swordToSend
							c.sender = f.id

				for c in f.hctargs:
					if not c.toSend:
						(derp, hcToSend) = findTroopRatio(0, 50, 0, f.hcCount-hcUsed, minhc, c.haul)
						hcUsed += hcToSend
						if hcToSend > 0:
							c.toSend = True
							c.hc = hcToSend
							c.sender = f.id
			

			# display the summary and see if okay with user :)
			print "\n\n" + str(f.name)
			print "to occur: \t\tspears\taxes\tswords\tlc\thc"
			counter = 0
			for c in speccoordinates + coordinates:
				if c.sender == f.id:
					counter += 1
					#print c.x,c.y
			#print "\ttotals:\t\t" + str(f.spearCount) + "\t" + str(f.axeCount) + "\t" + str(f.swordCount) + "\t" + str(f.lcCount) + "\t" + str(f.hcCount)
			print "\tremaining:\t" + str(f.spearCount-spearsUsed) + "\t" + str(f.axeCount-axesUsed) + "\t" + str(f.swordCount-swordsUsed) + "\t" + str(f.lcCount-lcUsed) + "\t" + str(f.hcCount-hcUsed) 
			print "\nvillages hit: " + str(counter) + "\n"
			x = input('is this okay? (0 if yes, new haul amount if no)  ' + str(theHaulMin) + '  ')

			if int(x) == 0:
				break
			else:
				#reset basically
				for c in speccoordinates + coordinates:
					if c.sender == f.id:
						c.lc = 0
						c.axes = 0
						c.spears = 0
						c.swords = 0
						c.hc = 0
						c.toSend = False
						c.sender = 0
				spearsUsed = 0
				axesUsed = 0
				lcUsed = 0
				swordsUsed = 0
				hcUsed = 0
				theHaulMin = int(x)

	# send the units!

	x = input("ready to send? ")

	for f in reversed(farmers):
		for c in speccoordinates + coordinates:
			if c.sender == f.id and c.toSend and not c.sent:
				c.sent = True
				c.display()
 
				args = [f.id, c.spears, c.swords, c.axes, c.lc, c.hc, c.x, c.y]
				p = subprocess.Popen(['osascript', 'sendUnits.scpt'] + [str(arg) for arg in args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

				out, err = p.communicate()




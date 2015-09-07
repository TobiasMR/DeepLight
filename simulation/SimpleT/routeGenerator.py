#!/usr/bin/env python
"""
@file    routeGenerator.py
@author  Tobias Rijken (adapted from Simon Box)
@date    03/08/2015

Code to generate routes for the simpleX

"""

import random

routes = open("simulation/SimpleT/simpleT.rou.xml", "w")
print >> routes, """<routes>
<vType id="typeCar" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="25" guiShape="passenger"/>
<vType id="typeBus" accel="0.8" decel="4.5" sigma="0.5" length="17" minGap="3" maxSpeed="25" guiShape="bus"/>

<route id="eastSouth" edges="2:0 0:1 1:5 5:6" />
<route id="eastWest" edges="2:0 0:1 1:3 3:7" />
<route id="westSouth" edges="7:3 3:1 1:5 5:6" />
<route id="westEast" edges="7:3 3:1 1:0 0:2" />
<route id="southEast" edges="6:5 5:1 1:0 0:2" />
<route id="southWest" edges="6:5 5:1 1:3 3:7" />
"""

N = 9000
peS = 1./30
peW = 1./10
pwS = 1./30
pwE = 1./10
psE = 1./50
psW = 1./50

factor = 0.25

lastVeh = 0
vehNr = 0
for i in range(N):
	if random.uniform(0,1) < factor*peS:
		print >> routes, '    <vehicle id="%i" type="typeCar" route="eastSouth" depart="%i" />' % (vehNr, i)
		vehNr += 1
		lastVeh = i
	if random.uniform(0,1) < factor*peW:
		print >> routes, '    <vehicle id="%i" type="typeCar" route="eastWest" depart="%i" />' % (vehNr, i)
		vehNr += 1
		lastVeh = i
	if random.uniform(0,1) < factor*pwS:
		print >> routes, '    <vehicle id="%i" type="typeCar" route="westSouth" depart="%i" />' % (vehNr, i)
		vehNr += 1
		lastVeh = i
	if random.uniform(0,1) < factor*pwE:
		print >> routes, '    <vehicle id="%i" type="typeCar" route="westEast" depart="%i" />' % (vehNr, i)
		vehNr += 1
		lastVeh = i
	if random.uniform(0,1) < factor*psE:
		print >> routes, '    <vehicle id="%i" type="typeCar" route="southEast" depart="%i" />' % (vehNr, i)
		vehNr += 1
		lastVeh = i
	if random.uniform(0,1) < factor*psW:
		print >> routes, '    <vehicle id="%i" type="typeCar" route="southWest" depart="%i" />' % (vehNr, i)
		vehNr += 1
		lastVeh = i

print >> routes, "</routes>"
routes.close()


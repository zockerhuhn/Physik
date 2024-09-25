import math

import matplotlib.pyplot as plt
import numpy as np

initialVelocity = 2 #m/s
initialAngle = 20 #degrees
xInitialVelocity = initialVelocity * math.cos(math.radians(initialAngle))
yInitialVelocity = initialVelocity * math.sin(math.radians(initialAngle))
xAverageAcceleration = 0 #m/s^2
yAverageAcceleration = -9.81 #m/s^2
deltaT = 0.1
xInitialDistance = 0
yInitialDistance = 2
stopAtYN = 0
printEveryNthCalc = 100
saveToListEveryNthCalc = 10
calcsPerDeltaT = 100
alwaysPrintLast = True

vX = []
sX = []
vY = []
sY = []

deltaT = deltaT/calcsPerDeltaT

if 1:
	xVelocity = xInitialVelocity
	yDistance = yInitialDistance
	yVelocity = yInitialVelocity
	xDistance = xInitialDistance
	print("t, V(x), S(x), V(y), S(y)")
	i = 0
	while yDistance > stopAtYN:
		xDistance += xVelocity*deltaT
		xDistance =round(xDistance, 9)
		yDistance += yVelocity*deltaT
		yDistance = round(yDistance, 9)
		xVelocity += xAverageAcceleration * deltaT
		xVelocity = round(xVelocity, 9)
		yVelocity += yAverageAcceleration * deltaT
		yVelocity = round(yVelocity, 9)
		if i%printEveryNthCalc == 0:
			print(f"{round(deltaT * i, 9)}, {xVelocity}, {xDistance}, {yVelocity}, {yDistance}")
		i+=1
		if i%saveToListEveryNthCalc == 0:
			vX.append(xVelocity)
			sX.append(xDistance)
			vY.append(yVelocity)
			sY.append(yDistance)
	if alwaysPrintLast:
		print(f"{round(deltaT * i, 9)}, {xVelocity}, {xDistance}, {yVelocity}, {yDistance}")


	t = np.arange(0, len(sY)*deltaT, deltaT)
	plt.plot(t, sY)
	plt.plot(t, sX)
	plt.show()
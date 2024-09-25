import math

import matplotlib.pyplot as plt
import numpy as np

initialVelocity = 2 #m/s
initialAngle = 20 #degrees
xInitialVelocity = initialVelocity * math.cos(math.radians(initialAngle))
yInitialVelocity = initialVelocity * math.sin(math.radians(initialAngle))
print(xInitialVelocity, yInitialVelocity)
xAverageAcceleration = 0 #m/s^2
yAverageAcceleration = -9.81 #m/s^2
deltaT = 0.1 #s
xInitialDistance = 0 #m
yInitialDistance = 2 #m
stopAtYN = 0 #m
printEveryNthCalc = 1000
saveToListEveryNthCalc = 1
calcsPerDeltaT = 10000
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

  fig, axs = plt.subplots(nrows=2, ncols=1)
  ax1, ax2= axs
  t = np.arange(0, len(sY)*deltaT, deltaT)

  ax1.plot(t, sY, label="S(y)")
  ax1.plot(t, sX, label="S(x)")
  ax1.set_ylabel("Strecke in m")
  ax1.legend()

  ax2.plot(t, vY, label="v(y)")
  ax2.plot(t, vX, label="v(x)")
  ax2.set_xlabel("Zeit in t")
  ax2.set_ylabel("Geschwindigkeit in m/s")
  ax2.legend()
  plt.show()
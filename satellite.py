import math
from time import sleep

import matplotlib.pyplot as plt
import numpy as np

from Attractor import Attractor
from Object import Object
import Settings

atr = []
obj = []

deltaT = Settings.deltaT
G = 6.67430e-11

satellite = Object(x=Settings.satelliteStartingX, y=Settings.satelliteStartingY, yVelocity=Settings.satelliteStartingYVelocity, xVelocity=Settings.satelliteStartingXVelocity)
obj.append(satellite)
earth = Attractor(x=0, y=0, mass=5.972e24)
atr.append(earth)

def step():
  for i in obj:
    i.move(deltaT)
    # if -10000 <= i.y <= 10000 and i.x >= 0:
      # print(deltaT*len(i.xLog), i.y) #8586.93 #3889.226
    for z in atr:
      delta_x = z.x - i.x
      delta_y = z.y - i.y
      angle_radians = math.atan2(delta_y, delta_x)
      distance = math.sqrt(delta_x**2 + delta_y**2)
      # area = (i.x * i.xLog[i.xLog.index(i.x)-1])/2
      # print(area)
      if abs(i.y) <= 1000 and len(i.xLog) >= 50:
        print(distance, i.y, deltaT*len(i.xLog)) #11747852.242334977 #4311983.435812522
      z.update_force(G=G, distance=abs(distance))
      i.apply_force(z.force * math.cos(angle_radians), z.force * math.sin(angle_radians), deltaT)

if Settings.saveToLogEveryNthStep > 0:
  with open('log.txt', 'w') as logFile:
    logFile.write(f"x: {satellite.x}, y: {satellite.y}\n")
for e in range(Settings.amountOfSteps):
  step()
  if e%Settings.printEveryNthStep== 0:
    print(f"x: {satellite.x}, y: {satellite.y}, vx: {satellite.xVelocity}, vy: {satellite.yVelocity}")
  #sleep(0.5)
  if e%Settings.saveToLogEveryNthStep== 0 and e > 0 and Settings.saveToLogEveryNthStep > 0:
    with open('log.txt', 'a') as logFile:
      for i in range(Settings.saveToLogEveryNthStep):
        logFile.write(f"x: {satellite.xLog[(e-Settings.saveToLogEveryNthStep)+i+1]}, y: {satellite.yLog[(e-Settings.saveToLogEveryNthStep)+i+1]}, Step: {(e-Settings.saveToLogEveryNthStep)+i+1}\n")
    
fig, axs = plt.subplots(nrows=1, ncols=1)
ax1= axs
t = np.arange(0, len(satellite.xLog)*deltaT, deltaT)

ax1.plot(satellite.xLog, satellite.yLog)
#ax1.plot(t, satellite.xLog, label="S(x)")
ax1.set_ylabel("Position in m")
#ax1.legend()

#ax2.plot(t, satellite.yVLog, label="v(y)")
#ax2.plot(t, satellite.xVLog, label="v(x)")
#ax2.set_xlabel("Zeit in s")
#ax2.set_ylabel("Geschwindigkeit in m/s")
#ax2.legend()
plt.savefig('graph.png')
plt.show()

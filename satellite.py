import math
from time import sleep

import matplotlib.pyplot as plt
import numpy as np

from Attractor import Attractor
from Object import Object

atr = []
obj = []

deltaT = 60
G = 6.67430e-11

satellite = Object(x=400000+6.371e6, y=0, mass=4500)
obj.append(satellite)
earth = Attractor(x=0, y=0, mass=5.972e24)
atr.append(earth)

def step():
  for i in obj:
    i.move(deltaT)
    for z in atr:
      delta_x = z.x - i.x
      delta_y = z.y - i.y
      angle_radians = math.atan2(delta_y, delta_x)
      distance = math.sqrt(delta_x**2 + delta_y**2)
      z.update_force(G=G, objMass=i.mass, distance=abs(distance))
      print(z.force, distance)
      i.apply_force(z.force * math.cos(angle_radians), z.force * math.sin(angle_radians), deltaT)

satellite.yVelocity = 9000
for e in range(2000):
  step()
  if e%10000 == 0:
    print(f"x: {satellite.x}, y: {satellite.y}, vx: {satellite.xVelocity}, vy: {satellite.yVelocity}")
  #sleep(0.5)
fig, axs = plt.subplots(nrows=1, ncols=1)
ax1= axs
t = np.arange(0, len(satellite.xLog)*deltaT, deltaT)

ax1.plot(satellite.xLog, satellite.yLog)
#ax1.plot(t, satellite.xLog, label="S(x)")
ax1.set_ylabel("Position in m")
ax1.legend()

#ax2.plot(t, satellite.yVLog, label="v(y)")
#ax2.plot(t, satellite.xVLog, label="v(x)")
#ax2.set_xlabel("Zeit in s")
#ax2.set_ylabel("Geschwindigkeit in m/s")
#ax2.legend()
plt.show()
from math import radians


class Object:
  x:float
  y:float
  xVelocity:float
  yVelocity:float
  mass:float
  xLog = []
  yLog = []
  xVLog = []
  yVLog = []
  def __init__(self, x:float, y:float, mass:float, xVelocity:float = 0, yVelocity:float = 0):
    self.x = x
    self.y = y
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity
    self.mass = mass
  def move(self, deltaT):
    self.x += self.xVelocity * deltaT
    self.y += self.yVelocity * deltaT
    self.xLog.append(self.x)
    self.yLog.append(self.y)
  def apply_force(self, xForce:float, yForce:float, deltaT:float, skipListing = False):
    self.xVelocity += xForce*deltaT
    self.yVelocity += yForce*deltaT
    if not skipListing:
      self.xVLog.append(self.xVelocity)
      self.yVLog.append(self.yVelocity)
class Attractor:
  x: float
  y: float
  force:float
  mass:float
  def __init__(self, x: float, y: float, mass: float):
    self.x = x
    self.y = y
    self.mass = mass
  def update_force(self, G, objMass, distance):
    self.force = (G * self.mass / distance**2)#/1000000
    if self.force >= 10:
      print(self.force, distance)
      raise Exception("crashed")
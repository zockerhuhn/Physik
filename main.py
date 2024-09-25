initialVelocity = 0
averageAcceleration = 9.81
deltaT = 0.1
initialDistance = 0
generateAmount = 51
printEveryNthTime = 1
calcsPerPrint = 1

deltaT = deltaT/calcsPerPrint
generateAmount = generateAmount*calcsPerPrint
printEveryNthTime = printEveryNthTime*calcsPerPrint

if __name__ == "__main__":
  velocityNum = initialVelocity
  distanceNum = initialDistance
  velocityAna = initialVelocity
  distanceAna = initialDistance
  print("t, V (num), S (num), V (ana), S (ana)")
  for i in range(generateAmount):
    distanceNum += velocityNum * deltaT
    distanceNum =round(distanceNum, 9)
    velocityNum += averageAcceleration * deltaT
    velocityNum = round(velocityNum, 9)
    velocityAna = averageAcceleration * deltaT*i
    velocityAna = round(velocityAna, 9)
    distanceAna = 0.5 * averageAcceleration * deltaT*i * deltaT*i
    distanceAna = round(distanceAna, 9)
    if i == 0:
      velocityNum = 0
    if i%printEveryNthTime == 0:
      print(f"{round(deltaT * i, 2)}, {velocityNum}, {distanceNum}, {velocityAna}, {distanceAna}")
cubedata = open("data.txt").readlines()

thresholds = {"red": 12, "green": 13, "blue": 14}

cubePowerSum = 0

for game in cubedata:
    gameInfo = game.replace(":", "").split()
    gameNumber = int(gameInfo[1])

    minCubes = {"red": 0, "green": 0, "blue": 0}

    power = 1
    
    for i in range(2, len(gameInfo), 2):
        value = int(gameInfo[i])
        color = gameInfo[i + 1].rstrip(',;')

        if value > minCubes[color]:
            minCubes[color] = value
    
    for cubes in minCubes:
        power *= minCubes[cubes]
    
    cubePowerSum += power

print(cubePowerSum)



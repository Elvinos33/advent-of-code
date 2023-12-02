cubeData = open("data.txt").readlines()

# Define thresholds for each color
thresholds = {"red": 12, "green": 13, "blue": 14}

gameSum = 0

for game in cubeData:
    gameInfo = game.replace(":", "").split()
    gameNumber = int(gameInfo[1])
    
    for i in range(2, len(gameInfo), 2):
        value = int(gameInfo[i])
        color = gameInfo[i + 1].rstrip(',;')  

        if value > thresholds[color]:
            break
    else:
        gameSum += gameNumber

print(gameSum)


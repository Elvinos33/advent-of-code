enginedata = open("data.txt").read().replace("\n", "")

symbol = "*"
indexes = [1, -1, 140, -140, 141, -141, 139, -139]

symbolnumbers = {}
numindexes = []

gears = []

for i in range(len(enginedata)):
    num = enginedata[i]

    if num.isdigit():
        numindexes.append(i)

    if (i + 1 < len(enginedata) and not enginedata[i + 1].isdigit()) or (i == len(enginedata) - 1):
        for number in numindexes:
            for index in indexes:
                if 0 <= number + index < len(enginedata) and enginedata[number + index] == symbol and numindexes:
                    if str(number + index) not in symbolnumbers:
                        symbolnumbers[str(number + index)] = []
                    symbolnumbers[str(number + index)].append(int(''.join(str(enginedata[i]) for i in numindexes)))
                    numindexes = []
        numindexes = []

for symbol in symbolnumbers:
    if len(symbolnumbers[symbol]) == 2:
        gears.append(symbolnumbers[symbol][1] * symbolnumbers[symbol][0])


print(sum(gears))

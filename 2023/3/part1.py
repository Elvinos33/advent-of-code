enginedata = open("data.txt").read().replace("\n", "")

symbols = set(filter(lambda c: not c.isdigit() and c != '.', enginedata))
indexes = [1, -1, 140, -140, 141, -141, 139, -139]

numindexes = []

nums = []

for i in range(len(enginedata)):
    num = enginedata[i]

    if num.isdigit():
        numindexes.append(i)

    if num.isdigit() and not enginedata[i + 1].isdigit():
        for number in numindexes:
            for index in indexes:
                if 0 <= number + index < len(enginedata) and enginedata[number + index] in symbols and numindexes:
                    nums.append(int(''.join(str(enginedata[i]) for i in numindexes)))
                    numindexes = []
        numindexes = []

print(sum(nums))

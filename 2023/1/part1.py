calibrationdata = open("input.txt").readlines()

numbers = []

for line in calibrationdata:
    digits = []

    for letter in line:
        if letter.isdigit():
            digits.append(letter)

    numbers.append(int(digits[0] + digits[len(digits)-1]))

numbers = sum(numbers)
print(numbers)


lines = []
with open("input.txt") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    numbers = list(map(lambda x: int(x), line.split()))
    for number1 in numbers:
        for number2 in numbers:
            if number1 != number2:
                if number1 > number2 and number1 % number2 == 0:
                    sum += number1 / number2
print(sum)

lines = []
with open("input.txt") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    numbers = line.split()
    smallest = 10000
    largest = 0
    for number in numbers:
        n = int(number)
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    sum += largest - smallest
print(sum)
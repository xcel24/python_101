numbers = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
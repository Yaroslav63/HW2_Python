import math

def diffNumbers(numbers):
    print(numbers)
    min = max = round(math.modf(numbers[0])[0], 4)
    for i in numbers:
        num = round(math.modf(i)[0], 4)
        if max < num: max = num
        if num != 0 and min > num: min = num

    return max - min

listNum = [1.1, 1.2, 3.1, 5, 10.01]
print(f"{diffNumbers(listNum)}\n")

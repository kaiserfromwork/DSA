import random

list_of_numbers = [
    [12, 45, 78, 23, 56, 89, 34, 67, 90, 21],
    [43, 76, 11, 88, 99, 32, 55, 20, 63, 74],
    [50, 92, 10, 31, 87, 29, 41, 57, 68, 81],
    [95, 24, 77, 62, 38, 15, 82, 49, 96, 100],
    [18, 35, 79, 46, 54, 91, 27, 83, 71, 66],
    [39, 53, 26, 58, 44, 72, 19, 64, 85, 93],
    [97, 30, 40, 52, 14, 17, 61, 98, 37, 70],
    [16, 75, 33, 84, 28, 60, 48, 47, 22, 80],
    [59, 42, 25, 51, 13, 20, 36, 32, 65, 86],
    [31, 50, 11, 88, 99, 32, 55, 20, 63, 74]
]

my_list = list_of_numbers[random.randint(0, len(list_of_numbers) - 1)]
print(my_list)
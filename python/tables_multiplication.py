import random
import math
import os

print("-------------------------------------------")

os.system("clear")

nb1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nb2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = 0
score = 0
n = 1

while n <= 10:

    while 2 > nb1[n] < 9:
        nb1[n] = math.floor(random.random() * 10)

    while 2 > nb2[n] < 9:
        nb2[n] = math.floor(random.random() * 10)

    print(f"{nb1[n]} x {nb2[n]}")
    result = input()

    if int(result) != int(nb1[n] * nb2[n]):
        print('faut')
    else:
        print('bravo')
        score = score + 1
    n = n + 1

    print("")
    print("-------------------------------------------")

print(f"ton score est de {score}/10")

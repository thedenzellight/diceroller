#Dice

import random
import time

dices = int(input("Number of dices: "))
dicenumber = int(input("Max number you can get: "))

print("The dice is rolling")
time.sleep(3)

a = 0
b = dices

while b > a:
    print("Dice #", a+1, ":", random.randint(1, dicenumber))
    a = a + 1
    time.sleep(0.05)

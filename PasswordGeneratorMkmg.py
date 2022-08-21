import random
from random import randint
import time
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("Welcome To My Monkey Magic")
total = input("Generate Number ")
#Number To Generate
number = int(total)
file = (total + " Generated.txt")
file2 = 'GiftCardsCodes.txt'
mode = input("GeneratedCode\nPasswordABC\nPassword123\nPassword123ABC\nPassword123ABCPlus\n")
#PasswordABC
if(mode == "PasswordABC"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+newline)
#Password123
if(mode == "Password123"):
    gentype = '123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+newline)
#Password123ABCPlus
if(mode == "Password123ABCPlus"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+newline)
print("Thanks For Using This Script")
time.sleep(5)
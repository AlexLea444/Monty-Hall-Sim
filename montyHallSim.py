import random

def game():
    car = random.randint(1,3)
    guess = random.randint(1,3)
    switch = 0
    if car == 1:
        if guess == 1:
            switch = random.randint(2,3)
        if guess == 2:
            switch = 1
        if guess == 3:
            switch = 1
    elif car == 2:
        if guess == 1:
            switch = 2
        if guess == 2:
            switch = random.randint(0,1)
            switch *= 2
            switch += 1
        if guess == 3:
            switch = 2
    elif car == 3:
        if guess == 1:
            switch = 3
        if guess == 2:
            switch = 3
        if guess == 3:
            switch = random.randint(1,2)
    if switch == car:
        return 1
    else:
        return 0

tally = 0
total = 100000
for j in range(0,total,1):
    if game() == 1:
        tally += 1
    

print(tally/total)

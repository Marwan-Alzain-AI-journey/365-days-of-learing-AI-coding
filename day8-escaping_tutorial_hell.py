import random
low = 1
high = 100
correct = "c"
c1 = ""
higher = "H"
lower = "L"
tries = 3
wrong = 0
out_of_tries = False
while c1 != correct and not(out_of_tries):
    yournum= random.randint(low, high)
    print(yournum)
    my_answer = input()
    if my_answer == higher:
            
            low = yournum + 1
            wrong += 1
    elif my_answer == lower:
            
            high = yournum - 1
            wrong += 1
    elif my_answer == correct:
            c1 = correct
            print("I win HAHAHAHAHA")

    if wrong == tries:
           out_of_tries = True
           print("I lost")


import random
secret_num = random.randint(1,100)
guess = ""
haerts = 10
hit = 0
out_of_haerts = False
while secret_num != guess and not(out_of_haerts):
    if hit < haerts:
        guess = int(input("enter a number: "))
        hit += 1
        if guess > secret_num:
            print("LOWER")
        elif guess < secret_num:
            print("HIGHER")
        print(haerts - hit)
    else:
        out_of_haerts = True
        print("Game Over!!!!")

if not(out_of_haerts):
    print("congrats you've won")

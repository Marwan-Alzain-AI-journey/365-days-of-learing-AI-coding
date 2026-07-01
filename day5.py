

for letter in "marwan":
    print(letter)


n = ["mahmoud", "ali", "marwan", "malek"]
for s in range(len(n)):
    print(n[s])


for d in n:
    print(d)

c = int(input("enter a number: "))
for x in range(1, c + 1 ):
    print(x, end="")
    if x == c:
        print("first")
    elif x == c + 1:
        print("second")
    elif x == c + 3:
        print("thrid")
    else:
        print("please stop!!1")
    

print(n.index("ali"))



def raise_to_power():
    base_num = int(input("enter base num: "))
    pow_num = int(input("enter pow num: "))
    
    result = 1

    for x in range(pow_num):
        result = result * base_num
    return result    
    

print(raise_to_power())    

s =[[1, 2, 3 ,4],[5, 6, 7, 8],[9,0]]
print(s[2][1])
w = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0]
]
print(w[2][1])
for d in s:
    for a in d:
        print(a)


def translator(phrase):
    translation = ""
    for g in phrase:
        if g in "AEOUIaeoui":
            translation = translation + "gp" 
        else:
            translation = translation + g

    return translation
    
print(translator(input("enter anything: ")))


import random
secret_num = random.randint(1, 1000000000)
g = ""
geusses = 0
lives = 40
out_of_geusses = False
while g != secret_num and not(out_of_geusses):
    if lives > geusses:
        g = float(input("enter a number: "))
        geusses += 1
        if secret_num > g:
            print("higher")
        elif secret_num < g:
            print("lower")
        print(lives - geusses)
    else:
        out_of_geusses = True
        print("game over")
if not(out_of_geusses):
    print("you win")
         


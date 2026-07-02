import random
secret_num = random.randint(1, 1000)
guess = ""
deaths = 0
lives = 10
out_of_lives = False
while secret_num != guess and not(out_of_lives):
    if lives > deaths:
        guess = int(input("enter a number: "))
        deaths += 1
        if secret_num > guess:
            print("HIGHER")
        elif secret_num < guess:
            print("LOWER")
        print(lives - deaths)
    else:
        out_of_lives = True
        print("GAME OVER!!")
else:
    print("write a number")

if not(out_of_lives):
    print("YOU win")


def translator(phrase):
    translation = ""
    
    for x in phrase:
        if x in "aeiouAEIOU":
            translation += "g"
        else:
            translation += x
    return translation

print(translator(input("write a word: ")))


try:
    num = int(input("enter a  number: "))
    print(num)

except ValueError as k:
    print(k)


x = open(r"C:\Users\marwan\Desktop\New folder (4)\New Text Document.txt", "r")

for l in x.readlines():
    print(l)






x.close()


z1 = open(r"C:\Users\marwan\Desktop\New folder (4)\marwan1.html", "a")


z1.write("<p>\nnarwan _ alzai1n\n<p>")





z1.close()
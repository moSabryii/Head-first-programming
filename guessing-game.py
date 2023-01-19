from random import randint
secret = randint(1, 10)
#print(secret)
print('welcome')
label = True
while label:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("you win")
        label = False
    else:
        if guess > secret:
            print('too high')
        else:
            print('too low')
print('game over')


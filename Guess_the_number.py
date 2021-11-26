import random
num= random.randrange(1,25)
i=9
j=0
print("Let's begin the game\n")
print(f"Guess the no in between 1 and 25 in {i} guesses\n")
while(i<=9 and i>0):
    x=int(input("Enter your guess: \n"))
    i=i-1
    j=j+1
    if (x>num):
        print("Guess lower")
    elif(x<num):
        print("Guess higher")
    else:
        print(f"Your guess {x} matches the number {num}")
        print(f"You won in {j} guesses")
        break
    print(f"you have {i} guesses left")
    continue
if(i==0):
    print("Game Over\n")
secret_number = 9
guess_count =0
guess_limit = 0
while guess_count<guess_limit:
    guess = int(input("Guess a number: "))
    guess_count+= 1
    if guess == secret_number:
        print("you win")
        break
else:
    print("Sorry! You fail")
    


import random

print("Welcome to Guessing Game")

ran_no = random.randint(1, 11)
tries = 0
tuloy = True

while tuloy == True:
    num = int(eval(input("Guess a random number from 1 to 10--> ")))
    tries += 1

    if num == ran_no:
        print("TAMA!!,  AT DAHIL JAN NAKAKUHA KA NG,,,,,,,,,,,,, TOROTOT!!")
        print(f"Only took {tries} tries")
        break
    else:
        print("MALI!! haha, PLEASE TRY AGAIN!")
        print("Continue")
        continue



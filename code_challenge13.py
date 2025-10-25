name = input("Enter your name")
print("Odd number summation program, press 0 to stop.\n")

con = True
sum = 0
odd = " "
while con == True:
    num = eval(input(f"Enter arandom number, {name}: "))
    if num == 0:
        con = False
        print("Program ended")
        break
    elif num % 2 == 1:
        sum += num
        odd += str(num) + " "
        continue
    else:
        print("Indvalid input!")
        continue

print(f"\nHeloo {name}, the sum of odd number is: {sum}")
print(f"L:ist of odd numbers:{odd}")
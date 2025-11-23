#WHILE LOOP
#Washing loop
soDirty = True #boolean initial value
sum = 0
while soDirty == True:
    wash = input("Do you with to continue washing? (yes / no)").lower()
    sum += 1
    if wash == 'yes':
        print("Washing Continues...")
        continue
    else:
        print("Washing Stop...")
        break
    print(f"Number of cycle is {sum}")

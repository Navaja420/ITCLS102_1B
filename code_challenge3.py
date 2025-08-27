name = input("What is your name? --> ")
fare = eval(input(" Fare fee --> "))
isStudent = input(" Are you a student ? (yes / no) ")

if isStudent == 'yes':
    discount = fare * 0.2
    #fare -= discount
    sukli_mo = fare - discount
    print("Hi ", name)
    print("Your Discount is ", discount)
    print("Your new fare is ", sukli_mo)
else:
    PRint("Sorry ", name, "You are to old for student discount")
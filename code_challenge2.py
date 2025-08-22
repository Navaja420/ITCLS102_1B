deposit = eval(input(" Enter the amount to deposit -->",))
print("Here it the breakdown of the deposit amount:")

Thousand = deposit // 1000
deposit = deposit % 1000
Fivehundred = deposit // 500
deposit = deposit % 500
Twohundred = deposit // 200
deposit = deposit % 200
Onehundred = deposit // 100
deposit = deposit % 100
Fifty = deposit // 50
deposit = deposit % 50 
Twenty = deposit // 20
deposit = deposit % 20
Ten = deposit // 10
deposit = deposit % 10
Five = deposit // 5
deposit = deposit % 5
One = deposit // 1
deposit = deposit % 1

print(Thousand,"-1000")
print(Fivehundred,"-500")
print(Twohundred,"-200")
print(Onehundred,"-100")
print(Fifty,"-50")
print(Ten,"-10")
print(Five,"-5")
print(One,"-1")

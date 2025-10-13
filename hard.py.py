loan = eval(input("Enter the amount of loan:"))
loan_period = eval(input("Enter the amount loan period:"))

months = loan_period * 12
principal = loan / months
balance = loan
print("Months/t|\tPrincipal Peyment\t|\tRemainig Balance\t|\t\tInterest/t")

for i in range(1, months + 1, 1):
    balance -= principal
    interest = balance * 0.03s
    monthly = principal + interest
    print(f"{i}\t|\t\t{round(principal,2)}\t\t|\t\t{round(balance,2)}\t\t|\t\t{round(interest,2)}")
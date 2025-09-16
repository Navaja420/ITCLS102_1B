factorial = 1
num = eval(input(" Enter any number here -->"))
for x in range(num, 0, -1):
    factorial *= x
print("The factorial of your", num," is",factorial)

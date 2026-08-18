# Create a calculator
result = 0
var1 = float(input("enter the first number"))
var2 = float(input("Enter the second number"))
op = input("Enter any operand(+, -, *, /)")
if op == "+" :
    result = var1 + var2
elif op == "-" :
    if var1 > var2 :
        result = var1 - var2
    else :
        result = var2 - var1
elif op == '*' : 
    result = var1 * var2
elif op == '/' :
    if var2 == 0:
        print("the division by zero is not valid")
    else :
        result = (var1/var2)
else :
    print("the wrong input entered")
print("the result is", result)
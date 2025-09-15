print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
if num1 * num2 < 0:
    print("The result is negative.")
elif num1 * num2 == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")
print("Enter a number less than 25")
num1 = int(input())
if num1 < 25:
    for i in range(num1, 26):
        print("Inside the loop, my variable is " + str(i))
else:
    print("Error")
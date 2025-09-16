number = float(input("Give me a number: "))
rounded_number = round(number)
if number > float(rounded_number):
    rounded_number += 1
print(rounded_number)
number = input("Give me a number: ")
if '.' in number:
    float_number = float(number)
    if float_number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
else:
    int_number = int(number)
    print("This number is an integer.")

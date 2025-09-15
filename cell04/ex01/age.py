age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
for future_year in range(1,4):
    future_age = age + future_year*10
    print(f"In {future_year*10} years, you will be {future_age} years old.")
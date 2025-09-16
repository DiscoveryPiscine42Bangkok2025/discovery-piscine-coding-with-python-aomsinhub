str = input()
newStr = ""
for c in str:
    if c.isupper():
        newStr += c.lower()
    elif c.islower():
        newStr += c.upper()
    else:
        newStr += c
print(newStr)

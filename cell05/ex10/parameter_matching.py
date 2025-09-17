import sys
if len(sys.argv) == 2:
    str = input("What was the parameter? ")
    if sys.argv[1] == str:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
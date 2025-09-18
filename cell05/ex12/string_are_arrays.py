import sys
if len(sys.argv) == 2:
    check = sys.argv[1].split('z')
    if len(check) > 1:
        print('z'*(len(check)-1))
    else:
        print("none")
else:
    print("none")   
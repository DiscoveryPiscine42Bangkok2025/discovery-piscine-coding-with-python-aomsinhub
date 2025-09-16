import sys
if len(sys.argv) > 2:
    for arg in reversed(sys.argv[1:]):
        print(arg)
else:
    print("none")
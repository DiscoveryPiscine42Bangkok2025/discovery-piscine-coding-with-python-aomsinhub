import sys
if len(sys.argv) == 3:
    strSplit = sys.argv[2].split(sys.argv[1])
    print(len(strSplit)-1)
else:
    print("none")
import sys
data = [d.rstrip() for d in sys.stdin.readlines()]
data = [str(int(data[i]) + int(data[i+1])) if data[i].isdigit() and data[i+1].isdigit() else "?" for i in range(0,len(data),2)]
for res in data :
    print(res)
import sys
data = [d.rstrip().split() for d in sys.stdin.readlines()]
data = [(bin(int(x,16))[2:],int(y)) for x,y in data]
data = [((32-len(x))*'0' +x , y ) for x , y in data]
data = [x[:-i]+x[-i:][::-1]  if i in range(2,32+1) else x for x,i in data ]

for d in data:
    print("0x"+ hex(int(d,2))[2:].upper())
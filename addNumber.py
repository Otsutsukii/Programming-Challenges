import sys

data = [d.rstrip() for d in sys.stdin.readlines()]
data = [(data[i],data[i+1]) for i in range(0,len(data),2)]

def addNumbers(data):
    for c in data:
        a,b = c
        if a.isdigit() == False or b.isdigit() == False:
            print("?")
            continue
        else:
            padding = abs(len(b)-len(a))
            if len(a)>len(b):
                a,b = b,a
            padded = "0"*padding + a
            carry = 0 
            res = ""
            for i in range(len(padded)-1, -1, -1):
                tmp = int(padded[i])+int(b[i]) + carry
                carry = int(tmp / 10)
                tmp = tmp%10
                res += str(tmp)
                if i == 0:
                    res+=str(carry)
            
            print(res[::-1].lstrip("0"))

addNumbers(data)
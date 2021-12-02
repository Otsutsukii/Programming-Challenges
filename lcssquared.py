import sys

data = [d.rstrip() for d in sys.stdin.readlines()][1:]
data = [[data[i],data[i+1]] for i in range(len(data))  ]


def sol(data):
    for couple in data:
        length , k = couple[0].split()
        binary = couple[1]
        res= 0 
        for i in range(len(binary)):
            j = i
            tmp = 0
            while k>0 and j<length:
                tmp+=1
                if binary[j] == "1":
                    k-=1
                res = max(res,tmp)




import sys
data = [d.rstrip() for d in sys.stdin.readlines()]

data = [line.split()[:-1] for line in data]
#print(data)
base1 = {0:"Ga",1:"Bu",2:"Zo",3:"Meu"}
base2 = {"Ga":0,"Bu":1,"Zo":2,"Meu":3}

def convert(i,b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result


def process(number):
    if number in ["-","+","*","/"]:
        return number

    if number.isdigit():
        return int(number)
    else:
        if len(number) > 2:
            res = 0
            digits = number.split("-")
            l = len(digits)
            for i in range(len(digits)):
                res += base2[digits[i]]*(10**(l-1))
                l-=1
            return int(str(res),4)
        else:
            return int(str(base2[number]),4)

#%%
for i in range(1,len(data)):
    for j in range(len(data[i])):
        data[i][j] = process(data[i][j])
        data[i][j] = str(data[i][j])
#%%
#print(data)
def eval2(tokens):
    stack = []
    ops = {'+':lambda x, y: x+y, '-':lambda x, y: x-y, '*':lambda x, y: x*y, '/':lambda x, y: x/y}
    for s in tokens:
        try:
            stack.append( float( s ) )
        except:
            stack.append( int( ops[s]( stack.pop(-2), stack.pop(-1) ) ) )
    return int( stack[-1] )

#%%

for d in data[1:]:
    #print("d",d)
    if len(d) > 1 :
        res = eval2(d)
        #print("res",res)
        if res == 0:
            print("Ga")
        else:
            tmp = list(map(str,convert(res,4)))
            tmp = [base1[int(l)] for l in tmp]
            #print(tmp)
            print("-".join(map(str,tmp)))
    else:
        tmp = "".join(d)
        if tmp == "0":
            print("Ga")
        else:
            tmp = convert(int(tmp),4)
            #tmp = list(map(str,convert(d,4)))
            tmp = [base1[int(l)] for l in tmp]
            print("-".join(map(str,tmp)))
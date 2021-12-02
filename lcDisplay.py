

def expand(n,s):
    numbers = {"1":[[" ", " "," "],[" "," ","|"],[" "," "," "],[" "," ","|"],[" ", " "," "]],
		   "2":[[" ","-"," "],[" "," ","|"],[" ","-"," "],["|"," "," "],[" ","-"," "]],
		   "3":[[" ","-"," "],[" "," ","|"],[" ","-"," "],[" "," ","|"],[" ","-"," "]],
		   "4":[[" ", " "," "],["|"," ","|"],[" ","-"," "],[" "," ","|"],[" "," "," "]],
		   "5":[[" ","-"," "],["|"," "," "],[" ","-"," "],[" "," ","|"],[" ","-"," "]],
		   "6":[[" ","-"," "],["|"," "," "],[" ","-"," "],["|"," ","|"],[" ","-"," "]],
		   "7":[[" ","-"," "],[" "," ","|"],[" "," "," "],[" "," ","|"],[" "," "," "]],
		   "8":[[" ","-"," "],["|"," ","|"],[" ","-"," "],["|"," ","|"],[" ","-"," "]],
		   "9":[[" ","-"," "],["|"," ","|"],[" ","-"," "],[" "," ","|"],[" ","-"," "]],
		   "0":[[" ","-"," "],["|"," ","|"],[" "," "," "],["|"," ","|"],[" ","-"," "]]
}
    M = numbers[n]
    elines = [[1],[0,1,2],[1],[0,1,2],[1]]
    for i in range(len(M)):
        coefs = elines[i]
        for c in coefs:
            M[i][c] =  M[i][c]*s
    return M

def resPrint(A):
    expandLine = [1,3]
    s = []
    for i in range(len(A)):
        if i in expandLine:
            for size in range(len(A[i][0])):
                s.append(A[i][0][size]+A[i][1]+A[i][2][size])
                #print(A[i][0][size]+A[i][1]+A[i][2][size])
        else:
            s.append(A[i][0]+A[i][1]+A[i][2])
            #print(A[i][0]+A[i][1]+A[i][2])

    return s


def printLine(n,s):
    nb = [resPrint(expand(char,s)) for char in n]

    for line in range(len(nb[0])):
        l = ""
        for n in range(len(nb)):
            l+= nb[n][line] + " "
        l = l[:-1]
        print(l)

data = input()
s,n = data.split()
s,n = int(s),n
printLine(n,int(s))
while n != "0" and s != "0":
    print()
    data = input()
    s,n = data.split()
    printLine(n,int(s))
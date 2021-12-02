def verif(L):
    if L[-1]!=L[-2]:
        return L[:-1]

def har(s):
    S=list(s)
    n=len(S)
    if n==0 or n==1:
        return S
    if n==2:
        return verif(S)
    for i in range(n-2):
        if S[i]==S[i+2] and S[i+1]!=S[i]:
            S[i+1]=S[i]
    if S[-1]!=S[-2]:
        return S[:-1]
    return S

def pr(s):
    r=""
    S=har(s)
    for i in S:
        r=r+i
    return r

def rebond(L):
    for i in L:
        print(pr(i))


if __name__=="__main__":
    import sys
    data = input().rstrip()
    rebond(data)
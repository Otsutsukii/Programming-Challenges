def no_zero(l,start):
    for i in range(start,len(l)):
        if l[i] != 0:
            return i
    return -1 
        

l = [1,3,0,0,4,5,0,7]

zero_i = l.index(0)

while zero_i != len(l) :
    no_zero_i = no_zero(l,zero_i+1)
    if no_zero_i==-1:
        break
    l[zero_i] , l[no_zero_i] = l[no_zero_i] , l[zero_i]
    print(l)
    zero_i = l.index(0)

print(l)

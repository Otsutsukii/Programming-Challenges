# Author: Zhaopeng tao , zhaopeng.tao@etu.unice.fr
# sliding window with radius r. Time complexity: O(n)
################################################################################

import sys
data = [d.rstrip() for d in sys.stdin.readlines()]
data = [line.split() for line in data]
data = data[1:]

def solution(w,N, R, W):
    if N <= R+1: #when the radius if bigger than the array 
        return 0

    max_somme = 0
    if N <= 2 * R + 1:
        pos = 0
        temp = sum([w[i] for i in range(R+1) if w[i]>=W])
        for i in range(1, N - R):
            if w[i+R] >= W:
                temp += w[i+R]
            if temp > max_somme:8
                max_somme = temp
                pos = i
        return pos
    # when window size < number of fish, slide
    else:
        for i in range(2 * R + 1):
            if w[i] >= W:
                max_somme += w[i]
        pos = R
        temp = max_somme
        for i in range(pos + 1, N - R):
            if w[i-R-1] >= W:
                temp -= w[i-R-1]
            if w[i+R] >= W:
                temp += w[i+R]
            
            if temp > max_somme:
                max_somme = temp
                pos = i
        return pos

if __name__ == "__main__":
    for i in range(0,len(data),2):
        l1 = list(map(int,data[i]))
        l2 = list(map(int,data[i+1]))
        res = solution(l2,l1[0],l1[1],l1[2])
        print(res+1) 
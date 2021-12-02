

def getinterval(binary):
    res = []
    for i in range(len(binary)):
        if binary[i] == "1":
            res.append(i)
    return res

def getMaxInterval(intervals,binary,length,k):
    maxInterval = 0
    length = int(length)
    k = int(k)
    a,e = 0,length
    for i in range(len(intervals)):
        if k+i > len(intervals) :
            break
        elif k+i == len(intervals):
            maxInterval = max(maxInterval,e-a)
            return maxInterval
        else:
            b = k+i 
            maxInterval = max(maxInterval,intervals[b] - a)
            a = intervals[i]
    return maxInterval -1
        

testCase = input()

for case in range(int(testCase)):
    length , k = input().split()
    binary = input()
 
    intervals = getinterval(binary)
    print(getMaxInterval(intervals,binary,length,k))

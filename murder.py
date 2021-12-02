import sys
import math
data = [d.rstrip() for d in sys.stdin.readlines()]
data = data[1:]


def solve(listes):
    res = 0
    for i in range(len(listes)):
        for j in range(0,i):
            if listes[j]<listes[i]:
                res+=listes[j]
    return res

def merge_sort(arr,temp,l,r):
    if l<r:
        mid = l+(r-l)/2
        merge_sort(arr,temp,l,mid)
        merge_sort(arr,temp,mid+1,r)
        merge(arr,temp,l,mid+1,r)

def merge(arr,temp,l,mid,r):
    i,j,k = l,mid,1
    while i <= mid-1 and j <= r:
        if arr[i] < arr[j]:
            global count
            count += arr[i]*(r-j+1)
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[i]
            k+=1
            i+=1
    while i <= mid-1:
        temp[k]=arr[i] 
        k+=1
        i+=1
    while j<=r:
        temp[k]=arr[j]
        k+=1
        j+=1
    for i in range(1,r+1):
        arr[i] = temp[i]           

def sort(arr,temp,n):
    merge_sort(arr,temp,0,n-1)

for i in range(0,len(data),2):
    count = 0
    ll = [d.rstrip() for d in data[i+1].split()]
    ll = [int(x) for x in ll]
    sort(ll,[0 for _ in range(len(ll))],len(ll))
    print(count)
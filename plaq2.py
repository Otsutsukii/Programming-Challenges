from sys import stdin
data = stdin.readline()
l = len(data)
if l == 7 and  65<=ord(data[0])<=90 and 65<=ord(data[1])<=90 and 48<=ord(data[2])<=57 and 48<=ord(data[3])<=57 and 48<=ord(data[4])<=57 and 65<=ord(data[5])<=90 and 65<=ord(data[6])<=90:
    print("V")
elif l == 5 and 65<=ord(data[0])<=90 and 65<=ord(data[1])<=90 and 48<=ord(data[2])<=57 and 48<=ord(data[3])<=57 and 65<=ord(data[4])<=90 :
    print("M")
else:
    print("?")
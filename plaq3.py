from sys import stdin
data = stdin.readline()
l = len(data)

if l == 7 and  all(65<=ord(x)<=90 for x in data[:2]+data[5:]) and all(48<=ord(x)<=57 for x in data[2:5]) :
    print("V")
elif l == 5 and all(65<=ord(x)<=90 for x in data[:2]+data[4]) and all(48<=ord(x)<=57 for x in data[2:4]) :
    print("M")
else:
    print("?")
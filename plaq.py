
import re,sys

data= sys.stdin.readline().strip()
r = re.compile(r"^[A-Z][A-Z][0-9][0-9][0-9][A-Z][A-Z]$")
r2 = re.compile(r"^[A-Z][A-Z][0-9][0-9][A-Z]$")
l = len(data)
if l == 7 :
    if r.match(data) is not None:
        print("V")
    else:
        print("?")
elif l == 5:
    if r2.match(data) is not None:
        print("M")
    else:
        print("?")
else:
    print("?")
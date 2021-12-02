

def main():
    data = int(input().rstrip())
    while data is not 0:
        classes = [int(x.rstrip()) for x in input().split()]
        price = [int(x.strip()) for x in input().split()]
        res = sum(c*p for c,p in zip(sorted(classes,reverse=True),sorted(price)))
        print(res)
        data = int(input().rstrip())
        

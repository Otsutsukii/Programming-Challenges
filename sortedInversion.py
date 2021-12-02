from functools import cmp_to_key
liste = [5,2,3,8,6,1]
InversionCount = []
res = sorted(liste , key = cmp_to_key(lambda a,b: (-1,InversionCount.append(1))[0] if a<b else 1  ))
print(sum(InversionCount))
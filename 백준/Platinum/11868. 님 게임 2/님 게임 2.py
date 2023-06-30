from functools import reduce;from operator import xor
n= int(input());p = [int(i) for i in input().split()];gn = reduce(xor, p)
if gn !=0:
    print("koosaga")
else:
    print("cubelover")
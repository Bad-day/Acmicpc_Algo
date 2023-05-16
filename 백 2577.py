num_l = [0]*10
a = int(input())
b = int(input())
c = int(input())
r = a*b*c
for i in str(r):
    num = int(i)
    num_l[num] +=1
for i in num_l:
    print(i)
    
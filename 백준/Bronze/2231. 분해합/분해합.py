n = int(input())  ;f = False 
for i in range(max(1, n-54), n): 
    num = i + sum((map(int, str(i)))) 
    if num == n: 
        print(i);f = True;break
if not f:
    print(0)
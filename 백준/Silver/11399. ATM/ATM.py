sum=0;r_sum=0;n= int(input());a = list(map(int, input().split()));a.sort()
for i in a:
    sum+=i
    r_sum +=sum 
print(r_sum)
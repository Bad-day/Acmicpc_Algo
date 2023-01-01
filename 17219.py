dick = {}
site_n, target= map(int, input().split())
for i in range(site_n):
    tkey,tvalue = map(str, input().split())
    dick[tkey]=tvalue

for j in range(target):
    print(dick[input()])

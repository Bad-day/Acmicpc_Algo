import sys; input= sys.stdin.readline
ail=[];count=0
n,k = map(int, input().split())
# for i in range(n):
#     j = int(input())
#     ail.append(j)
#     if k < int(j):
#         ail.remove(j)
# ail = list(filter(lambda x: x < k, map(int, [input() for i in range(n)])))
# ail = sorted(ail, reverse=True)
ail = sorted(list(map(int, [input() for i in range(n)])),reverse=True)
# ail = sorted(list(filter(lambda x: x < k, map(int, [input() for i in range(n)]))), reverse=True)
for j in range(n):
    count += k//ail[j];print(count)
    k = k%ail[j];print(k)
print(count)



# while True:
    # reamin = k % ail[0]
    # count +=1
# if reamin >ail[1]:
#     remain = reamin % ail[1]
#     count +=1
#     if reamin > ail[2]:
#         remain = remain % ail[2]
#         count +=1
# print(count)
    
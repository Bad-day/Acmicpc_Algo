N,M = map(int, input().split())
do_not_listen= set()
for i in range(N):
    do_not_listen.add(input())
do_not_look= set()
for j in range(M):
    do_not_look.add(input())
result = sorted(list(do_not_listen&do_not_look))
print(len(result))
for i in result:
    print(i)
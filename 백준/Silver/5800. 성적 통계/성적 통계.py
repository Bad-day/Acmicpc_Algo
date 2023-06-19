k = int(input());sc = [];a = [];result = 0
for i in range(k):
    score = list(map(int, input().split()))
    a.append(score[0]);sc.append(score[1:]);r = sorted(sc[i], reverse=True)
    count = 1;gap = 0
    for j in range(len(r)):
        if count >= len(r):
            count -= 1; result = gap;gap = 0
        point = r[count]
        if gap <= r[j]-point:
            gap = r[j]-point
        count += 1
    print(f'Class {i+1}')
    print(f'Max {max(sc[i])}, Min {min(sc[i])}, Largest gap {result}')
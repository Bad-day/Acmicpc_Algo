n=1
while True:
    split_num = sum(map(int, str(n)))
    n+=split_num
    print(n)
    if n>=10000:
        break
    
55 < n < 57
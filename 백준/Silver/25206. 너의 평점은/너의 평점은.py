sum=0 ;r=0;count=20
#sum = (학점 * 과목평점) / 학점의 총합
for i in range(count):
    a, b, c = map(str, input().split());b=float(b)
    if c == 'A+':
        sum+=b* 4.5
    elif c =='A0':
        sum+=b*4.0
    elif c=='B+':
        sum+=b*3.5
    elif c=='B0':
        sum+=b*3.0
    elif c=='C+':
        sum+=b*2.5
    elif c=='C0':
        sum+=b*2.0
    elif c=='D+':
        sum+=b*1.5
    elif c=='D0':
        sum+=b*1.0
    elif c=='F':
        sum+=b*0
    if c=='P':
        pass
    else:
        r +=b
result = sum/r;print("{:.6f}".format(result))
    
        
        
    
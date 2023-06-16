n=input()
if len(n)==1:
    n=int(n)
    if n==9:
        print(11)
    else:
        print(n+1)
elif len(n)&1:
    a=int(n[:len(n)//2][::-1])
    b=int(n[len(n)//2+1:])
    if a>b:
        print(n[:len(n)//2]+n[len(n)//2]+n[:len(n)//2][::-1])
    else:
        if int(n[len(n)//2])==9:
            c=str(int(n[:len(n)//2])+1)
            if len(c)==len(n[:len(n)//2]):
                print(c+"0"+c[::-1])
            elif len(c)>len(n[:len(n)//2]):
                print(c+c[::-1])
        else:
            print(n[:len(n)//2]+str(int(n[len(n)//2])+1)+n[:len(n)//2][::-1])
else:
    a=int(n[:len(n)//2][::-1])
    b=int(n[len(n)//2:])
    if a>b:
        print(n[:len(n)//2]+n[:len(n)//2][::-1])
    else:
        c=str(int(n[:len(n)//2])+1)
        if len(c)==len(n[:len(n)//2]):
            print(c+c[::-1])
        elif len(c)>len(n[:len(n)//2]):
            print(c+c[::-1][1:])
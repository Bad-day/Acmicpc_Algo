n = input();count=0
def fuck(u):
    global count
    if len(u) ==1:
        if int(u) %3 ==0:
            print(count);print("YES")
        else:
            print(count);print("NO")
    else:
        result = 0
        for i in range(len(u)):
            result += int(u[i])
        u=str(result);count +=1;fuck(u)
fuck(n)
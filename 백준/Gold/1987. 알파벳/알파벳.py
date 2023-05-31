def dfs(x, y, c):
    global answer
    dx = [-1, 1, 0, 0] # 좌우 이동량
    dy = [0, 0, -1, 1] # 상하 이동량
    answer = max(answer, c) #최대 이동가능칸수 업데이트
    for i in range(4): #상하좌우 이동하는 반복문
        nx, ny = x + dx[i], y+dy[i] #새로운 좌표 계산
        if 0 <= nx < row and 0 <= ny < col and alpha_list[nx][ny] not in visited:
            
                visited.add(alpha_list[nx][ny]) #방문 판정 처리
                dfs(nx, ny, c+1) #재귀, 새로운칸으로 이동, 칸수증가
                visited.remove(alpha_list[nx][ny])
row, col = map(int, input().split()) #행, 열
alpha_list = [list(input().strip())for _ in range(row)] #알파벳리스트 입력받기
visited = set(alpha_list[0][0]) #시작위치 방문판정 처리
answer = 1 #시작위치 칸수 포함 조건


dfs(0,0,answer)
print(answer)
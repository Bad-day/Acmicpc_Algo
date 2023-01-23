import sys,math; input=sys.stdin.readline
A,B,V= map(int, input().split())
dis=V-B #하룻밤 총 거리 
result = math.ceil(dis/(A-B));print(result)

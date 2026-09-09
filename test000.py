num = 1_000_000

cnt = (int)(input())

s = set()
for i in range(cnt):
    s.add((int)(input())) 
    if(i >= num):
        break

for i in s:
    print(i)







#-------------------------------------------------------
# 정답
N = 1_000_000
cnt = 1

for i in range(N):
    print("연산횟수 " + str(cnt))
    cnt += 1

N = 3
graph = [[] for _ in range(N + 1)]

N, E = map(int, input().split())
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

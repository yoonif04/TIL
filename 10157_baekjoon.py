# C:가로, R:세로
# 하-우-상-좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

C, R = map(int, input().split())
graph = [[0]*(C+1) for _ in range(R+1)]
K = int(input())    # 대기번호
d = 0
i, j = 1, 1
p = 1
while p <= K:
    if p == K:
        print(j, i)
    if graph[i][j] == 0:
        graph[i][j] = p
        p += 1
    else:
        print(0)
        break
    # 새로운 방향
    ni, nj = i + di[d], j + dj[d]
    # 방향 가능한지 여부
    if 0<ni<=R and 0<nj<=C and graph[ni][nj] == 0:
        i, j = ni, nj
    else:
        d = (d + 1) % 4
        i += di[d]
        j += dj[d]

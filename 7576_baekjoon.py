di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs():
    day = 0
    size = N*M+1
    q = [0] * size
    front = rear = -1
    # 토마토가 있으면 큐에 넣기
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == 1:
                rear = (rear + 1) % size
                q[rear] = (r, c)
                visited[r][c] = 1
    # 큐가 비어있지 않으면
    while front != rear:
        # 큐의 길이만큼 제한 반복
        for _ in range(abs(rear-front)):
            front = (front + 1) % size
            i, j = q[front]
            # 4방향 탐색
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < M and tomatoes[ni][nj] != -1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    rear = (rear + 1) % size
                    q[rear] = (ni, nj)
        day += 1

    # 익지 않은 토마토가 있는 자리를 다 방문했는지 확인
    for i in range(N):
        for j in range(M):
            if not tomatoes[i][j] and not visited[i][j]:
                return -1

    # 여기까지 왔으면 다 익었다
    return day - 1


M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(bfs())

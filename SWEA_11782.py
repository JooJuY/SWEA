def BFS(sx, sy):
    q = []
    q.append([sx, sy])
    visited[sx][sy] = 0
    while q:
        nx, ny = q.pop(0)
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = nx + di, ny + dj
            if 0 <= ni < N and 0 <= nj < N:
                now = visited[nx][ny] + 1
                if arr[ni][nj] - arr[nx][ny] > 0:
                    now += (arr[ni][nj] - arr[nx][ny])
                if visited[ni][nj] > now:
                    visited[ni][nj] = now
                    q.append([ni, nj])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1000*100*100] * N for _ in range(N)]  # 가중치 저장
    BFS(0, 0)
    print(f'#{t} {visited[N-1][N-1]}')
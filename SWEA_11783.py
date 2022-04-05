def BFS(s):
    q = []
    q.append(s)
    visited[s] = 0
    while q:
        now = q.pop(0)
        for n, w in adj[now]:
            if visited[n] > visited[now] + w:
                visited[n] = visited[now] + w
                q.append(n)


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    visited = [10*N] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
    BFS(0)
    print(f'#{t} {visited[N]}')
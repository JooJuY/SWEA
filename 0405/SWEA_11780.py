def BFS(n):
    q = []
    q.append(n)
    visited[n] = 1
    while q:
        now = q.pop(0)
        for node in adj[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = 1


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    cnt = 0
    for i in range(M):
        adj[tmp[i*2]].append(tmp[i*2+1])
        adj[tmp[i*2+1]].append(tmp[i*2])
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            BFS(i)
            cnt += 1

    print(f'#{t} {cnt}')

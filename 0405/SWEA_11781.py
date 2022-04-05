def prim(n):
    cnt = 0
    U = []
    U.append(n)
    visited[n] = 1
    while len(U) != (V+1):
        k = 0
        min_w = 11
        for now in U:
            for node, w in adj[now]:
                if not visited[node] and min_w > w:
                    k, min_w = node, w
        visited[k] = min_w
        U.append(k)
        cnt += min_w
    return cnt


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append([n2, w])
        adj[n2].append([n1, w])

    print(f'#{t} {prim(0)}')

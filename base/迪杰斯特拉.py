N, P = [int(i) for i in input().split()]

passed = [False for _ in range(N)]
distance = [float('INF') for _ in range(N)]

cost = [[float('INF') for _ in range(N)] for _ in range(N)]
for i in range(P):
    v, u, w = list(map(int, input().split()))
    cost[v][u] = w
    cost[u][v] = w
mudi = int(input())


def diji(s, t, N):
    distance[s] = 0
    while True:
        v = -1
        for u in range(N):
            if not passed[u] and (v == -1 or distance[u] < distance[v]):
                v = u
        if v == -1:
            break
        passed[v] = True
        for u in range(N):
            distance[u] = min(distance[u], distance[v] + cost[v][u])
    return distance[t]


ans = diji(0, mudi, N)
print(ans)
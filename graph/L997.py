import numpy as np
import collections
def findJudge(N, trust):
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for a,b in trust:
        graph[a-1][b-1] = 1

    graph = np.array(graph)
    res = []
    for i in range(N):
        if sum(graph[i]) == 0 and sum(graph[:,i]) == N-1:
            res.append(i + 1)

    if len(res) == 1:
        return res[0]
    else:
        return -1

def findJudge2(N, trust):
    if not trust:
        return -1
    adj = collections.defaultdict(list)
    for a,b in trust:
        adj[a].append(b)

    inDegree = [0] * (N + 1)

    for node in adj:
        for v in adj[node]:
            inDegree[v] += 1

    for i in range(1,len(inDegree)):
        if inDegree[i] == N - 1:
            if len(adj[i]) == 0:
                return i
    return -1

if __name__ == '__main__':
    N = 1
    trust = []
    print(findJudge2(N,trust))
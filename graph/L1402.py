import collections
def gardenNoAdj(N,paths):
    flowers = set([i for i in range(1,5)])
    graph = collections.defaultdict(list)

    for a,b in paths:
        graph[a].append(b)
        graph[b].append(a)

    res = [0]*(N+1)
    for gardn in range(1,N+1):
        neighbor_flow_set = set()
        for neighbor in graph[gardn]:
            neighbor_flow_set.add(res[neighbor])
        res[gardn] = list(flowers - neighbor_flow_set)[0]
    return res[1:]

if __name__ == '__main__':
    N = 3
    paths = [[1, 2], [2, 3], [3, 1]]
    print(gardenNoAdj(N,paths))
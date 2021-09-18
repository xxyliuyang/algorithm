

def canVisitAllRooms(rooms):
    def dfs(root):
        see.add(root)
        for v in graph[root]:
            if v not in see:
                dfs(v)

    graph = {}
    for i in range(len(rooms)):
        graph[i] = rooms[i]
    see = set()

    dfs(0)
    return len(see) == len(rooms)

if __name__ == '__main__':
    f = open("t",'r')
    s = f.readline()
    print(type(s))
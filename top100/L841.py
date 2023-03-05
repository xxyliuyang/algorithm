# https://mp.weixin.qq.com/s/E9NlJy9PW1oJuD8N2EURoQ
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(rooms, visited, index):
            if visited[index]:
                return
            visited[index] = True
            for i in rooms[index]:
                dfs(rooms, visited, i)
        visited = [False for _ in range(len(rooms))]
        dfs(rooms, visited, 0)
        return all(visited)

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:

        visited = [False for _ in range(len(rooms))]
        q = [0]
        visited[0] = True
        while q:
            room = q.pop()
            for next in rooms[room]:
                if visited[next]:
                    continue
                q.append(next)
                visited[next] = True
        return all(visited)


if __name__ == '__main__':
    rooms = [[1], [2], [3], []]
    solution = Solution()
    print(solution.canVisitAllRooms2(rooms))

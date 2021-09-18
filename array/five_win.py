"""五子棋问题：给一个19*19的矩阵作为五子棋棋盘，用0代表空，1代表黑子，2代表白子，
判断当前是否有一方已经获胜（不存在两方都获胜的情况），
返回0，1，2分别代表：没有一方获胜、黑子获胜、白子获胜。"""

def win1(nums):
    row = len(nums)
    col = len(nums[0])
    result = [[[0,0,0,0,0,0, 0, 0, 0] for i in range(col + 2)] for j in range(row+1)]

    directions = [(-1, -1, 0), (0, -1, 1), (-1, 0, 2), (-1, 1, 3)]
    for i in range(row):
        for j in range(col):
            if nums[i][j] == 0:
                continue
            cur_i = i+1
            cur_j = j+1
            for d_i, d_j, d_k in directions:
                if nums[i][j] == 2:
                    d_k += 4
                result[cur_i][cur_j][d_k] = result[cur_i + d_i][cur_j + d_j][d_k] + 1
                if result[cur_i][cur_j][d_k] == 5:
                        return nums[i][j], i, j
    return 0

if __name__ == '__main__':
    nums = [[0, 1, 2, 2, 2, 2, 0, 2, 1, 1],
            [1, 0, 1, 2, 1, 1, 0, 1, 1, 1],
            [1, 1, 2, 1, 2, 2, 0, 0, 1, 1],
            [1, 2, 1, 1, 2, 2, 2, 1, 1, 1],
            [2, 2, 1, 2, 0, 2, 1, 2, 0, 0],
            [0, 2, 0, 1, 1, 2, 0, 1, 1, 1],
            [1, 1, 1, 1, 2, 0, 1, 2, 1, 1],
            [1, 0, 1, 2, 1, 1, 2, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 2, 1, 2, 1],
            [0, 1, 2, 1, 1, 2, 1, 1, 2, 0]]

    print(win1(nums))

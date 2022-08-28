import copy

class Solution:
    def __init__(self):
        # 第一个位置表示人，第二个位置表示鬼
        self.left_state = (3, 3)
        self.right_state = (0, 0)
        self.left2right_choice = [[1,1], [1,2], [2,2]]
        self.right2left_choice = [[1,1], [1,2], [2,2], [1, 0], [0, 2]]

        self.path = []
        self.result = []
        self.used = [(self.left_state[0], self.left_state[1],
                      self.right_state[0], self.right_state[1])]
        self._init()

    def _init(self):
        choice = []
        for left2right in self.left2right_choice:
            for right2left in self.right2left_choice:
                if left2right == right2left:
                    continue
                choice.append(left2right + right2left)
        self.choice = choice

    def check_step(self, step):
        left1, left2 = self.left_state
        right1, right2 = self.right_state

        # 左侧移动检查
        for i in [0, 1]:
            if step[i] == 1:
                left1 -= 1
                right1 += 1
            elif step[i] == 2:
                left2 -= 1
                right2 += 1

        if left1 == 0 and left2 == 0:
            return True

        if left1 < 0 or left2 < 0 \
                or (left1 < left2 and left1 != 0) \
                or (right1 < right2 and right1 != 0):
            return False

        # 右侧移动检查
        for i in [2, 3]:
            if step[i] == 1:
                left1 += 1
                right1 -= 1
            elif step[i] == 2:
                left2 += 1
                right2 -= 1
        if right1 < 0 or right2 < 0 \
                or (left1 < left2 and left1!=0) \
                or (right1<right2 and right1!=0):
            return False
        if (left1, left2, right1, right2) in self.used:
            return False
        return True

    def move_step(self, step):
        left1, left2 = self.left_state
        right1, right2 = self.right_state

        # 左侧移动检查
        for i in [0, 1]:
            if step[i] == 1:
                left1 -= 1
                right1 += 1
            elif step[i] == 2:
                left2 -= 1
                right2 += 1

        # 右侧移动检查
        for i in [2, 3]:
            if step[i] == 1:
                left1 += 1
                right1 -= 1
            elif step[i] == 2:
                left2 += 1
                right2 -= 1
        self.left_state = (left1, left2)
        self.right_state = (right1, right2)

    def back_move(self, step):
        left1, left2 = self.left_state
        right1, right2 = self.right_state

        # 左侧移动检查
        for i in [0, 1]:
            if step[i] == 1:
                left1 += 1
                right1 -= 1
            elif step[i] == 2:
                left2 += 1
                right2 -= 1

        # 右侧移动检查
        for i in [2, 3]:
            if step[i] == 1:
                left1 -= 1
                right1 += 1
            elif step[i] == 2:
                left2 -= 1
                right2 += 1
        self.left_state = (left1, left2)
        self.right_state = (right1, right2)

    def check_success(self, step):
        left1, left2 = self.left_state
        right1, right2 = self.right_state

        # 左侧移动检查
        for i in [0, 1]:
            if step[i] == 1:
                left1 -= 1
                right1 += 1
            elif step[i] == 2:
                left2 -= 1
                right2 += 1

        if left1 == 0 and left2 == 0:
            return True


    def backtrack(self):
        for step_choice in self.choice:
            if self.check_success(step_choice):
                self.path.append(step_choice)
                self.result.append(copy.deepcopy(self.path))
                self.path.pop()
                break

            if not self.check_step(step_choice):
                continue
            self.path.append(step_choice)
            self.move_step(step_choice)
            self.used.append((self.left_state[0], self.left_state[1],
                      self.right_state[0], self.right_state[1]))
            self.backtrack()
            self.path.pop()
            self.back_move(step_choice)
            self.used.pop()

    def find_all_path(self):
        self.backtrack()
        return self.result

if __name__ == '__main__':
    solution = Solution()
    print(solution.find_all_path())
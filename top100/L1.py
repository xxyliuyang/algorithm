def twoSum(nums, target):
    need_index = {}
    num_index = {}
    for index,num in enumerate(nums):
        if num in need_index:
            return [need_index[num],index]
        else:
            need_index[target-num] = index
    return []




if __name__ == '__main__':
    print(twoSum(nums = [2, 7, 11, 15], target = 9))
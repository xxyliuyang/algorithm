'''对于一有序的数组，旋转一下，找最小值'''
def findMin(nums) : # 二分查找
    if len(nums) == 1:
        return nums[0]

    left, right = 0,len(nums)-1
    while left<right:
        pivot = (left+right)//2
        if nums[pivot]>nums[right]:
            left = pivot + 1
        else:
            right = pivot
    return nums[left]

if __name__ == '__main__':
    print(findMin([1,2,3]))
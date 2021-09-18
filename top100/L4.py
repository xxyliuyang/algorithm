def findMedianSortedArrays(nums1, nums2):
    '''找到两个排序数组的中位数：
    二分法：
    a. 找到两个下标i，j，将两个数组分开；左边的小于右边的，根据条件返回具体的哪一个值；同时左右两边的数量为一半
        left_part            |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

    b. 寻找二分的满足的条件：
    在 [0, m] 中找到一个使下面不等式成立的 i :
    B[j-1] <= A[i] and A[i-1] <= B[j], ( where j = (m + n + 1)/2 - i )

    c. 注意边界条件
    '''
    m,n = len(nums1), len(nums2)
    if m>n:
        nums1, nums2, m, n = nums2, nums1, n, m
    left_i, right_i, half_len = 0, m, (m+n+1)//2
    while left_i<=right_i:
        i = (left_i+right_i)//2
        j = half_len-i

        if i<m and nums2[j-1]>nums1[i]:
            left_i = i+1
        elif i>0 and nums1[i-1]>nums2[j]:
            right_i = i-1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j==0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1],nums2[j-1])
            if (m+n)%2 == 1:
                return max_of_left
            if i==m:
                min_of_right = nums2[j]
            elif j==n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i],nums2[j])
            return (min_of_right+max_of_left)/2.0

if __name__ == '__main__':
    print(findMedianSortedArrays([1,3],[2]))
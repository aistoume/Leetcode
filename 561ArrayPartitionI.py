### Youbin 2017/06/19
### 561 Array Partition I

def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    s = 0
    for i in range(0,len(nums),2):
        s += nums[i]
    return s

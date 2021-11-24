def kbig(nums,k):
    for i in range(k):
        maxnum = max(nums)
        nums.remove(maxnum)
    return maxnum

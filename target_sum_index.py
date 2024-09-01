def twosum(nums, target):
    length = len(nums)
    
    for i in range(length):
        x=nums.index(target-nums[i]) if target-nums[i] in nums else -1
        if x==-1:
            return -1
        return [i,x]
n = [3, 1, 1, 2]
t = 5
print(twosum(n, t))

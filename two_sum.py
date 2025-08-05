class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls=[]
        sum=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    sum=nums[i]+nums[j]
                    if target==sum:
                        ls.append(i)
        return ls

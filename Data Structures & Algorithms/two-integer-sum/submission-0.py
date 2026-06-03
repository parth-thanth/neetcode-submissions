class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hashmap={}
        index =0
        for num in nums:
            neednum=target-num
            if neednum in Hashmap:
                return [Hashmap.get(neednum),index]
            Hashmap[num]=index
            index+=1    

    
        
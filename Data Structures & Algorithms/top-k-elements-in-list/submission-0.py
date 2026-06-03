class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num in  hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1  
        ans=[]          
        while k>0:
            bestNum=max(hashmap, key=hashmap.get)
            ans.append(bestNum)
            del hashmap[bestNum]
            k-=1
        return ans




    
        
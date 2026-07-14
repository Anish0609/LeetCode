class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        temp=[]
        res=[]

        def find(idx,total):
            if idx==n :
                if total==target :
                    res.append(temp[:])
                return
            
            find(idx+1,total)

            if total+candidates[idx]<=target :
                temp.append(candidates[idx])
                total+=candidates[idx]
                find(idx,total)
                temp.pop()
                total-=candidates[idx]
            
        find(0,0)

        return res
        
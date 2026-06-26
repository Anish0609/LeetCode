class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=high=1
        res=-1

        for i in piles :
            high=max(high,i)
        
        while low<=high :
            guess=(low+high)//2

            et=0
            for i in piles :
                t = 0
                t=(i//guess)
    
                if i%guess!=0 :
                    t+=1
                et=et+t
            
            if et>h :
                low=guess+1
            elif et<=h :
                res=guess
                high=guess-1
        
        return res
            


        
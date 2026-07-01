class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        f={}
        res=[]
        seat=0

        for ch in s :
            f[ch]=f.get(ch,0)+1
        
        class Pair :
            def __init__ (self,freq,lett):
                self.freq=freq
                self.lett=lett
            def __lt__ (self,other) :
                if self.freq!=other.freq :
                    return self.freq>other.freq
                return self.lett<other.lett
        heap=[]
        for lett , freq in f.items() :
            heapq.heappush(heap, Pair(freq, lett))
        
        prev=None
        while heap :
            curr=heapq.heappop(heap)
            
            res.append(curr.lett)
            curr.freq-=1

            if prev and prev.freq>0 :
                heapq.heappush(heap, prev)
            
            prev=curr
            
        if len(res)<len(s) :
            return ""
        return "".join(res)
    





        
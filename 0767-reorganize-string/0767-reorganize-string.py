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
        
        while heap :
            p=heapq.heappop(heap)
            letter=p.lett

            if seat==0 or res[seat-1]!=letter :
                res.append(letter)
                seat+=1
                p.freq-=1
                if p.freq>0 :
                    heapq.heappush(heap, p)

            else :
                if not heap :
                    return ""
                else :
                    p1=heapq.heappop(heap)
                    letter=p1.lett
                    res.append(letter)
                    seat+=1
                    p1.freq-=1
                    if p1.freq>0 :
                        heapq.heappush(heap, p1)
                    if p.freq>0 :
                        heapq.heappush(heap, p)
        
        return "".join(res)
    





        
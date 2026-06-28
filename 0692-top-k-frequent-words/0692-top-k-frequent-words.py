class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq

        f={}

        for word in words :
            f[word]=f.get(word,0)+1
        
        class Word :
            def __init__ (self, word, freq) :
                self.word=word
                self.freq=freq
            def __lt__ (self, other) :
                if self.freq!=other.freq :
                    return self.freq<other.freq
                return self.word>other.word
        
        heap=[]

        for word, freq in f.items() :
            heapq.heappush(heap,Word(word,freq))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        while heap :
            res.append(heapq.heappop(heap).word)
        
        return res[::-1]
        
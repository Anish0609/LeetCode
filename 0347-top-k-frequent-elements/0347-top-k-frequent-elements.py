class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import heapq

        f={}
        for num in nums :
            f[num]=f.get(num,0)+1
        
        heap=[]
        for num , freq in f.items() :
            heapq.heappush(heap,(freq,num))
            if len(heap)>k :
                heapq.heappop(heap)

        return [num for freq, num in heap ]
        

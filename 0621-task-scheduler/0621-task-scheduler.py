class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import deque

        f={}
        for task in tasks :
            f[task]=f.get(task,0)+1
        
        heap=[]
        for freq in f.values() :
            heapq.heappush(heap, -freq)
        
        queue = deque()
        time=0

        while heap or queue :
            time+=1

            if heap :
                freq=heapq.heappop(heap)+1
                if freq!=0 :
                    queue.append((freq,time+n))
            
            if queue and queue[0][1]==time :
                heapq.heappush(heap, queue.popleft()[0])
        
        return time


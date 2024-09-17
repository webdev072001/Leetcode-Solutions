class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # calculate the distance from 1"s and choose a disatnace with maximum distnace
        # i feel i need to store the mi _distance from 0 to closest 1 using bfs
        paths=deque()
        # i will use a hashmap to store the min_distance from a node to nearesr one
        dic={}
        visited=set()
        max_row=len(grid)
        max_col=len(grid[0])
        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col]==1:
                    dic[(row,col)]=0
                    paths.append([0,row,col])
        neib=[[0,1],[0,-1],[1,0],[-1,0]]
        while paths:
            distance,row,col=paths.popleft()
            if (row,col) in visited:
                continue
            dic[(row,col)]=-1*distance
            visited.add((row,col))
            for nr,nc in neib:
                if min(nr+row,nc+col)<0 or nr+row>=max_row or nc+col>=max_col or (nr+row,nc+col) in visited:
                    continue
                paths.append([distance+1,nr+row,nc+col])
        # i will use a dikstra algortim from 0,0 to end,end
        max_heap=[[dic[0,0],0,0]]
        ans=float("-inf")
        visited=set()
        while max_heap:  #v^2
            far_dis,row,col=heapq.heappop(max_heap)
            ans=max(ans,far_dis)
            if row==max_row-1 and col==max_col-1:
                return -1*ans
            if (row,col) in visited:
                continue
            visited.add((row,col))
            for nr,nc in neib:
                if min(nr+row,nc+col)<0 or nr+row>=max_row or nc+col>=max_col or (nr+row,nc+col) in visited:
                    continue
                heapq.heappush(max_heap,[dic[(nr+row,nc+col)],nr+row,nc+col])



        

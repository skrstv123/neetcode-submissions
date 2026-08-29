class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        r, c = len(board), len(board[0])
        issafe = lambda i,j: i >= 0 and j >= 0 and i < r and j < c

        dxdy = ((0, -1), (1, 0), (0, 1), (-1, 0)) # LDRU
        # oppmap = {
        #     dxdy[2]: dxdy[0],
        #     dxdy[3]: dxdy[1],
        #     dxdy[0]: dxdy[2],
        #     dxdy[1]: dxdy[3],
        # }


        def bt(cti, i, j, vis):
            nonlocal ans, dxdy, issafe
            if cti == len(word):
                ans = True
                return

            for dx,dy in dxdy:
                
                x, y = i + dx, j + dy
                if (x,y) not in vis:
                    if issafe(x, y) and board[x][y] == word[cti]:
                        vis.add((x,y))
                        bt(cti+1, x, y, vis)
                        if (x,y) in vis:
                            vis.remove((x,y))
    
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    currvis = set()
                    currvis.add((i,j))
                    bt(1, i, j, currvis)
        return ans


            

        
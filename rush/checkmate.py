def checkmate(board: str):
    rows = board.strip().split("\n")
    grid = [list(r.strip()) for r in rows]

    h, w = len(grid), len(grid[0])

    #King
    king_pos = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "K":
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return




    def inside(x, y):
        return 0 <= x < h and 0 <= y < w

    # Pawn
    def pawn_attacks(i, j):
        for di, dj in [(-1, -1), (-1, 1)]:
            ni, nj = i + di, j + dj
            if inside(ni, nj) and (ni, nj) == king_pos:
                return True
        return False

    # Rook
    def rook_attacks(i, j):
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            while inside(ni, nj):
                if grid[ni][nj] != ".":
                    if (ni, nj) == king_pos:
                        return True
                    break
                ni += di
                nj += dj
        return False
    
    # Bishop
    def bishop_attacks(i, j):
        for di, dj in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            ni, nj = i+di, j+dj
            while inside(ni, nj):
                if grid[ni][nj] != ".":
                    if (ni, nj) == king_pos:
                        return True
                    break
                ni += di
                nj += dj
        return False

    # Queen
    def queen_attacks(i, j):
        return rook_attacks(i,j) or bishop_attacks(i,j)


    for i in range(h):
        for j in range(w):
            piece = grid[i][j]
            if piece == "." or piece == "K":
                continue
            if piece == "P" and pawn_attacks(i,j):
                print("Success")
                return
            if piece == "R" and rook_attacks(i,j):
                print("Success")
                return
            if piece == "B" and bishop_attacks(i,j):
                print("Success")
                return
            if piece == "Q" and queen_attacks(i,j):
                print("Success")
                return
    print("Fail")

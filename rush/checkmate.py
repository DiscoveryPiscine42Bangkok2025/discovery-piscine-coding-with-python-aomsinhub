def checkmate(board: str):
    # แปลงกระดานจาก string ให้เป็น list 2D
    rows = board.strip().split("\n")
    grid = [list(r.strip()) for r in rows]

    h, w = len(grid), len(grid[0])

    # หา King
    king_pos = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "K":
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")  # ไม่มี King
        return

    ki, kj = king_pos

    # --------- Helper ฟังก์ชัน ---------
    def inside(x, y):
        return 0 <= x < h and 0 <= y < w

    def pawn_attacks(i, j):
        # Pawn เดินเฉียงขึ้นไปหา King (ตามที่คุณกำหนด)
        for di, dj in [(-1, -1), (-1, 1)]:
            ni, nj = i + di, j + dj
            if inside(ni, nj) and (ni, nj) == king_pos:
                return True
        return False

    def rook_attacks(i, j):
        # เดินเป็นเส้นตรง 4 ทิศ
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

    def bishop_attacks(i, j):
        # เดินทแยง 4 ทิศ
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

    def queen_attacks(i, j):
        # ควีน = rook + bishop
        return rook_attacks(i,j) or bishop_attacks(i,j)

    # --------- Loop หาหมากทั้งหมด ---------
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

    # ถ้าไม่มีใครกินได้
    print("Fail")

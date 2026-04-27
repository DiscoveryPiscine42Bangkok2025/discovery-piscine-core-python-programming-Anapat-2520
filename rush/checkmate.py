def checkmate(board):
    # 1. เตรียมข้อมูล: แยกกระดานเป็นแถวๆ และตรวจสอบว่าไม่ว่างเปล่า [cite: 25]
    lines = [line for line in board.strip().split('\n') if line.strip()]
    if not lines:
        print("The board is empty. No checkmate possible.")
        return # คืนการควบคุมหากกระดานว่าง [cite: 28]

    # 2. ตรวจสอบความเป็นสี่เหลี่ยมจัตุรัส [cite: 23]
    size = len(lines)
    for row in lines:
        if len(row) != size:
            print("Board is not square")
            return # หากไม่ใช่สี่เหลี่ยมจัตุรัสให้หยุดทำงานทันที (Undefined behavior) [cite: 28]
        
    king_pos = None
    king_count = 0
    for i in range(size):
        for j in range(size):
            cell = lines[i][j]

            if cell not in ('.', 'P'):
                print(f"Invalid character '{cell}' found. Only '.' and 'P' are allowed.")
                return # หากพบตัวอักษรที่ไม่ถูกต้องให้หยุดทำงานทันที (Undefined behavior) [cite: 28]
            
            if cell == 'K':
                if king_pos is not None:
                    print("Multiple kings found. Invalid board.")
                    return # หากพบพระราชามากกว่าหนึ่งตัวให้หยุดทำงานทันที (Undefined behavior) [cite: 28]
                king_pos = (i, j)
                king_count += 1

            if king_count == 0:
                print("No king found. Invalid board.")
                return # หากไม่พบพระราชาให้หยุดทำงานทันที (Undefined behavior) [cite: 28]
            

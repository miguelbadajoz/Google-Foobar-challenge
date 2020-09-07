# Level 2 / Challenge 1                
def chessKnightMovements(src,dest):

    def possible_dest(pos):

        pos_dest = []

        for mov1 in [-16,16]:
            pos1 = pos + mov1
            if pos1 > 63 or pos1 < 0:
                continue
            for mov2 in [-1,1]:
                if pos1%8 == 0 and mov2 ==-1 :
                    continue
                if pos1%8 == 7 and mov2 ==+1 :
                    continue
                pos2 = pos1 + mov2
                pos_dest.append(pos2)
                
        for mov1 in [-8,8]:
            pos1 = pos + mov1
            if pos1 > 63 or pos1 < 0:
                continue
            for mov2 in [-2,2]:
                if (pos1%8 == 0 or pos1%8 == 1) and mov2 ==-2 :
                    continue
                if (pos1%8 == 6 or pos1%8 == 7) and mov2 ==+2 :
                    continue
                pos2 = pos1 + mov2
                pos_dest.append(pos2)

        return pos_dest

    n = 0
    boxes = [src]
    while dest not in boxes:
        n = n + 1
        new_boxes = []
        for pos in boxes:
            more_boxes = possible_dest(pos)
            for one_more_box in more_boxes:
                new_boxes.append(one_more_box)
        boxes = new_boxes
    return n

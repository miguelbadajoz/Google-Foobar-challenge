# level 3 / Challenge 1
def getPathLength(map):
    import copy

    h = len(map)
    w = len(map[0])
    min_pos_path = w + h -1
    print('heigh =',h)
    print('width =',w)

    def valid_pos(pos,mymaze):
        if  pos[0]<h and pos[1]<w and pos[0]>=0 and pos[1]>=0:
            if mymaze[pos[0]][pos[1]]==0:
                return True
            else:
                return False
        else:
            return False

    def possible_dest(pos,mymaze):
        pos_dest = []
        # right
        new_pos = [pos[0],pos[1]+1]
        if valid_pos(new_pos,mymaze):
            pos_dest.append(new_pos)
        # down
        new_pos = [pos[0]+1,pos[1]]
        if valid_pos(new_pos,mymaze):
            pos_dest.append(new_pos)
        # left
        new_pos = [pos[0],pos[1]-1]
        if valid_pos(new_pos,mymaze):
            pos_dest.append(new_pos)
        # up
        new_pos = [pos[0]-1,pos[1]]
        if valid_pos(new_pos,mymaze):
            pos_dest.append(new_pos)
        return pos_dest

    def calculate_min_path(mymaze):

        # Starting position:
        boxes = [[0,0]]
        this_round_boxes = [[0,0]]
        steps = 1

        #for row in mymaze:
            #print(row)

        # Run:
        while [h-1,w-1] not in boxes:
            #time.sleep(1)
            #print '************************************'
            #for row in mymaze:
                #print(row)
            next_round_boxes = []
            for pos in this_round_boxes:
                
                mymaze[pos[0]][pos[1]]=8
                paths = possible_dest(pos,mymaze)
                
                for box in paths:
                    #print '==>', box
                    boxes.append(box)
                    next_round_boxes.append(box)
                
            steps = steps + 1
            this_round_boxes = next_round_boxes
            if len(next_round_boxes)==0 and [w-1,h-1] not in boxes:
                print('==> No solution (',steps,')')
                return -1

        print '==>',steps
        return steps    
    
    # Bucle removing one wall each turn:
    all_solutions = []
    a_maze = copy.deepcopy(map)
    print('Original maze')
    steps = calculate_min_path(a_maze)
    if steps == min_pos_path:
        return steps
    if steps > 0:
        all_solutions.append(steps)
    
    for h_0 in range(h-1,-1,-1):
        for w_0 in range(w-1,-1,-1):
            a_maze = copy.deepcopy(map)

            # Break the wall if any:
            if a_maze[h_0][w_0] == 1:
                # Only if it is a thin wall:
                zeros = 0
                if h_0>0:
                    if a_maze[h_0-1][w_0]==0:
                        zeros = zeros + 1
                if w_0>0:
                    if a_maze[h_0][w_0-1]==0:
                        zeros = zeros + 1
                if h_0<(h-1):
                    if a_maze[h_0+1][w_0]==0:
                        zeros = zeros + 1
                if w_0<(w-1):
                    if a_maze[h_0][w_0+1]==0:
                        zeros = zeros + 1
                if zeros >=2:
                    print('Maze without wall [',h_0,'][',w_0,']')
                    a_maze[h_0][w_0] = 0
                    steps = calculate_min_path(a_maze)
                    if steps == min_pos_path:
                        return steps
                    if steps > 0:
                        all_solutions.append(steps)

    if min(all_solutions) < min_pos_path:
        print 'Wrong solution'
        return all_solutions
    if len(all_solutions) > 0:
        return min(all_solutions)
    else:
        for row in map:
            print(row)
        return -1

def creates_maze(h,w):

    from random import random
    print(h,'x',w)
    maze = [[None for _ in range(w)] for _ in range(h)]
    
    for h_0 in range(0, h):
        for w_0 in range(0, w):
            maze[h_0][w_0] = int(round(pow(random(),2)))

    maze[0][0] = 0
    maze[h-1][w-1] = 0

    for row in maze:
        print(row)
    return maze

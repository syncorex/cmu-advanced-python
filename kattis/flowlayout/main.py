import sys
from typing import List, Tuple


m = 35
example = [(10, 5), (20, 12), (8, 13), (-1, -1)]
m2 = 25
example2 = [(10, 5), (20, 13), (3, 12), (-1, -1)]

def window_dims(max_width: int, boards: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    row_w, row_h, window_w, window_h = (0, 0, 0, 0)
    for board in boards:
        x, y = board[0], board[1]
        
        if x == y == -1:
            window_h += row_h
            if row_w > window_w:
                window_w = row_w        
        
        if row_w + x > max_width:
            if row_w > window_w:
                window_w = row_w
            window_h += row_h
            row_w = 0
            row_h = 0
        
        row_w += x
        if y > row_h:
            row_h = y



    return (window_w, window_h) 
     
# print(window_dims(m, example))
# print(window_dims(m2, example2))

if __name__ == "__main__":
    result = ""
    done = False
    m = -1
    boards = []

    while(not done):
        line = list(map(lambda x: int(x) ,sys.stdin.readline().split()))

        if len(line) == 1 and line[0] == 0:
            print(result)
            break

        elif(len(line) > 1):
            boards.append((line[0], line[1]))
            
            if line[0] == line[1] == -1:
                dims = window_dims(m, boards)
                result = result + f"{dims[0]} x {dims[1]}\n"
                m = -1
                boards = []

        else:
            m = line[0]
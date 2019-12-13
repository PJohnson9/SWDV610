# Patrick Johnson        12/12/2019 #
# SWDV 610 3W 19/FA2    Week 8 - FP #
#####################################
from time import time

def row_col_from_num(square_num):
    """ returns the row (0-7) and column (0-7) for a square number """
    row = (square_num)//8
    col = square_num%8
    return (row,col)

def square_id_from_num(square_num):
    """ takes square number (0-63) and returns grid square """
    row,col = row_col_from_num(square_num)
    return "ABCDEFGH"[col] + "12345678"[row]

def square_num_from_id(square_id):
    """ takes grid square id and returns square number """
    row = "12345678".index(square_id[1])
    col = "ABCDEFGH".index(square_id[0])
    return col + row*8

class position:
    visited = []   # list of visited nodes
    
    def __init__(self, square, previous_position = None):
        self.square = square   
        self.previous_position = previous_position
        if previous_position == None:  # starting square
            self.move_number = 0
            position.visited.append(self.square)
        else:
            self.move_number = previous_position.move_number + 1
        self.candidate_moves = moves_graph[square].copy() # get moves from graph
        for candidate in moves_graph[square]:
            if candidate in position.visited:
                self.candidate_moves.remove(candidate)
        self.next_moves = None
        
    def move(self):
        if self.next_moves == None:
            self.next_moves = []
            for next_square in self.candidate_moves:
                next_move = position(next_square, self)
                if len(next_move.candidate_moves) > 0 or next_move.move_number == 63:
                    i = 0
                    while (i < len(self.next_moves) and
                        len(next_move.candidate_moves) > len(self.next_moves[i].candidate_moves)):        
                        i += 1
                    self.next_moves.insert(i,next_move)

        if len(self.next_moves) > 0:
            next_position = self.next_moves.pop(0)
            position.visited.append(next_position.square)
            return next_position         
        else:
            position.visited.remove(self.square)
            return self.previous_position
        
    def print_steps(self):
        print("List of Moves:")
        for square in position.visited:
            print("  {:2} - {}".format(square, square_id_from_num(square)))



def is_move_valid(squareA, squareB):
    """ check if a knight is allowed to move from squareA to squareB """
    rowA,colA = row_col_from_num(squareA)
    rowB,colB = row_col_from_num(squareB)
    
    return ((abs(rowA-rowB) == 1 and abs(colA-colB) == 2)
         or (abs(rowA-rowB) == 2 and abs(colA-colB) == 1))

def generate_moves_graph():
    """ Generate graph of possible moves for each square """
    graph = {}
    squares = list(range(64))
    for i in squares:
        posssible_moves = []
        for j in squares:
            if is_move_valid(i,j):
                posssible_moves.append(j)
        graph.update({ i : posssible_moves })
    return graph






start_time = time()
moves_graph = generate_moves_graph()


##########################################
# Knight's Tour Script


starting_square = 28
closed_tour = True
current_position = position(starting_square)
end_squares = moves_graph[starting_square] # for closed tours
step_count = 0

while len(current_position.candidate_moves) > 0 or current_position.move_number > 0:
    if current_position.move_number == 63 and (
       current_position.square in end_squares or not closed_tour ):
        current_position.print_steps()
        break
    else:
#        print("{:4}  Square: {:2}   Move: {:2}   Available: {}".format( step_count,
#            current_position.square, current_position.move_number,
#            current_position.candidate_moves))
        current_position = current_position.move()
        step_count += 1

end_time = time()
print("Took: {:.5f} seconds to try {} steps.".format(end_time-start_time, step_count))

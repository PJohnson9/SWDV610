# Patrick Johnson        12/12/2019 #
# SWDV 610 3W 19/FA2    Week 8 - FP #
#####################################
# Final Project:  Knight's Tour
#    Finds knight's tour solutions using an iterative depth-first
#    search algorithm, optimized with Warnsdorff's Rule

# Some helper methods for identifying squares in different ways:
#   square number: 0-63, startingat 0 in lower left and going row by row
#   row, col: 0-7, 0-7, row number and column number, 0,0 is lower left
#   grid id: A1 - H8, chess notation, A1 is lower left, H1 is lower right
def row_col_from_num(square_num):
    """ returns the row (0-7) and column (0-7) for a square number (0-63) """
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

def is_move_valid(squareA, squareB):
    """ Check if a knight is allowed to move from squareA to squareB
    returns True or False """
    rowA,colA = row_col_from_num(squareA)
    rowB,colB = row_col_from_num(squareB)
    
    return ((abs(rowA-rowB) == 1 and abs(colA-colB) == 2)
         or (abs(rowA-rowB) == 2 and abs(colA-colB) == 1))

def generate_moves_graph():
    """ Generate graph of possible moves for each square
        For each square, checks against all squares to find valid moves
        and appends them to the possible_moves list for that square
    returns the graph as a dictionary with squares as keys and move lists as values
    """
    graph = {}
    squares = list(range(64))
    for i in squares:
        posssible_moves = []  
        for j in squares:
            if is_move_valid(i,j):  # 
                posssible_moves.append(j)
        graph.update({ i : posssible_moves })
    return graph


class position:
    """ position class acts as a node for a linked list of moves
    Each instance has:
        square - current location (square number) on board
        previous_position - position class instance for previous square
                            (this is None for the starting position)
        move_number - 0 for starting location, increments with each move
        candidate_moves - list of square numbers that are possible next moves
        next_moves - ordered list of position class instances to try
    
    move() is an instance method that will return the next move
        - will try to move forward, unless all options have been tried
        - otherwise will return to previous position
        
    There is also the class variable visited for a list of visited nodes
    and class methods print_steps() and print_board() for displaying output
    """
    visited = []   # list of visited nodes
    
    def print_steps():
        """ Outputs a list of moves in both square number and grid ID formats """
        print("List of Moves:")
        for square in position.visited:
            print("  {:2} - {}".format(square, square_id_from_num(square)))
            
    def print_board():
        """ Prints a representation of the board, with the move number shown in each square """
        board = [''] * 64   # Generate list for board squares
        for s in range(len(position.visited)): 
            board[position.visited[s]] = s # Assign move number to each square
        # Print the board, with the move number shown in each square    
        print("|----" * 8 + "|")     
        for i in range(7,-1,-1): # Start at last row (row 7)
            for j in range(8):   # work across each row
                print("| {:2} ".format(board[i*8+j]), end='')
            print("|")
            print("|----" * 8 + "|")     
    
    def __init__(self, square, previous_position = None):
        self.square = square   
        self.previous_position = previous_position
        if previous_position == None:  # starting square
            self.move_number = 0
            position.visited = [self.square]
        else:
            self.move_number = previous_position.move_number + 1
        self.candidate_moves = moves_graph[square].copy() # get moves from graph
        for candidate in moves_graph[square]:
            if candidate in position.visited:
                self.candidate_moves.remove(candidate)
        self.next_moves = None
        
    def move(self):
        """ Returns the position for the next move """
        if self.next_moves == None:  # Check if next_moves hasn't been populated yet
            self.next_moves = []     # Start with an empty list
            for next_square in self.candidate_moves:  # Add next_move for each candidate_move
                next_move = position(next_square, self)  # Create new position instance
                if len(next_move.candidate_moves) > 0 or next_move.move_number == 63: # Check for dead ends
                    # Apply Warnsdorff's Rule by ordering by the number of candidate moves
                    i = 0
                    while (i < len(self.next_moves) and
                        len(next_move.candidate_moves) > len(self.next_moves[i].candidate_moves)):        
                        i += 1
                    self.next_moves.insert(i,next_move)  # inserts next_move, orderd by len(candidate_moves)

        if len(self.next_moves) > 0: # Unexplored forward moves, move ahead
            next_position = self.next_moves.pop(0)  # removes first item from next_moves list
            position.visited.append(next_position.square) # update visited list
            return next_position         
        else:                        # No path forward, so go back
            position.visited.remove(self.square)
            return self.previous_position


def tour(start = "A1", closed_tour = False):
    starting_square = square_num_from_id(start)
    current_position = position(starting_square)
    end_squares = moves_graph[starting_square] # for closed tours
    step_count = 0 # Tracks number of steps (including backtracks)

    while current_position != None: # No valid paths => move() returns None
        if current_position.move_number == 63 and ( # board has been covered
           current_position.square in end_squares or not closed_tour ):
            #position.print_steps()
            position.print_board()
            break
        else:
            current_position = current_position.move()
            step_count += 1

    print("\n{} steps to find a{} tour starting from {}".format(
            step_count," closed" if closed_tour else "n open", start))

if __name__ == "__main__":
    moves_graph = generate_moves_graph()  # Generate graph for use
    tour("A1")  # find an open tour starting in the lower left corner

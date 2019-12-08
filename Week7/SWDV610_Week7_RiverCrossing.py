# Patrick Johnson         12/7/2019 #
# SWDV 610 3W 19/FA2         Week 7 #
#####################################

# Three missionaries and three cannibals need to cross a river
# There is a boat that can hold two people
# More cannibals than missionaries on either side => lunchtime

# Notes on Approach:
# State:  On Starting Side: [C := # Cannibals, M := # missionaries, B := Boat Present (0/1)]
# Starting Node: [3,3,1]
# End Node:      [0,0,0]
# Valid Nodes: [C,M,B] such that (C<=M or M=0) and ((3-C) <= (3-M) or M=3) and B in [0,1] 
#                                     and C in [0,1,2,3] and M in [0,1,2,3]
# Valid Edges: [C1,M1,B1] => [C2,M2,B2] if |B2-B1| = 1 and (C2-C1)*(M2-M1) >= 0
#                                          and 0 < ((C2-C1) + (M2-M1))*(B2-B1) <= 2
#
# Since there are only 4 X 4 X 2 = 32 possible states, and not all of those are valid,
# I'll start by generating all nodes, add valid ones to graph with adjacency lists,
# then find a solution by searching the graph.  This should be easier than generating
# nodes by attempting possible moves and checking if the result is valid.
#
# Step 1: Generate all possible nodes, and add valid ones to graph
# Step 2: Check all combinations of nodes to see if a valid edge can exist between them.
# Step 3: Perform a graph search to find a path from starting node to end node.


# Some helper functions:    
def is_state_valid(state, start_state):
    """ state is [c, m, b] (list or tuple) where
        c = # of cannibals on starting side
        m = # of missionaries on starting side
        b = # of boats on starting side (always 0 or 1)
    start_state is the initial condition (all on near side)
    
    returns True if cannibals don't outnumber missionaries on either side and
                    number of people and boats are within valid ranges """
    if (state[2] not in range(2)                       # invalid number of boats
        or state[0] not in range(start_state[0] + 1)   # invalid number of cannibals
        or state[1] not in range(start_state[1] + 1)): # invalid number of missonaries
        return False 
    
    if state[0] > state[1] and state[1] > 0: # cannibals > missionaries on starting side
        return False
    
    if ((start_state[0]-state[0]) > (start_state[1]-state[1])
        and state[1] < start_state[1]) : # cannibals > missionaries on far side
        return False
     
    return True # nothing invalid about state

def is_edge_valid(stateA, stateB, boat_limit = 2):
    """returns True or False depending on whether it is possible to
        get from stateA to stateB in one move        
    (Assumes both states are valid)
    boat_limit: maximum capacity of boat, default = 2
    """
    # Calculate changes for each variable
    # Negative values will represent crossing from near side to far side
    deltaC = stateB[0] - stateA[0] # Change in number of cannibals
    deltaM = stateB[1] - stateA[1] # Change in number of missionaries
    deltaB = stateB[2] - stateA[2] # Change in number of boats
    
    # Cannibals and Missionaries cannot move in opposite directions: dC * dm >= 0
    # Boat must move: db != 0
    # At least one cannibal or missionary must move: (dC+dM) != 0
    # No more than two cannibals or missionaries can move at a time |dC+dM| <= boat_limit
    # Cannibals and missionaries must move with boat: (dC+dM)*db > 0
    # Therefore: 0 < (deltaC + deltaM) * deltaB <= 2 and deltaC * deltaM >= 0
    if 0 < (deltaC + deltaM) * deltaB <= boat_limit and deltaC * deltaM >= 0:
        return True 
    else:
        return False

def search_graph(nodes, start, goal):
    """Performs a breadth-first search of the graph, from start looking for goal
    nodes: dictionary with states as keys and adjacency lists for the values
    start: intial state
    goal:  desired final state

    Returns a list of states forming a path through the graph from start to goal,
            or None if no path is found.
    """
    class search_node:
        def __init__(self, value, parent = None):
            self.value = value
            self.parent = parent
            
    def retrieve_path(node):
        """ Takes a search_node and climbs the tree to generate a path list
        returns a list of the states in order from start to goal
        """
        path = []
        while node != None:  # Work through nodes to root
            path.insert(0, node.value) # Insert each node at start of list
            node = node.parent  # move to the parent node
        return path
    
    if start not in nodes: # No possible solution if start isn't in the graph
        return None
            
    frontier = [search_node(start)] # begin search with the start node as our "frontier"
    visited = [start]               # list of visited states, beginning with start
        
    while len(frontier) > 0: # ensures that search will stop if we don't find final state
        current_node = frontier.pop(0)          # Get next search_node off of frontier
        if current_node.value == goal:          # Check to see if it is the goal
            path = retrieve_path(current_node)  # Generate the path to current_node
            return path                         # Return path
        for successor_node in nodes[current_node.value]: # Not the goal, so check neighbors
            if successor_node not in visited:   # Check neighbor hasn't already been visited
                visited.append(successor_node)  # Add neighbor state to visited list
                frontier.append(search_node(successor_node,current_node)) # Add to frontier               
    return None # Goal not found


#### Main Script ####
# Parameters/Constants
boat_capacity = 2       # maximum number of passengers in boat
initial_state = (3,3,1) # 3 cannibals, 3 missionaries, and the boat on near side
final_state = (0,0,0)   # all made it (alive) to the far side

# Create List of Nodes (for iteration and building graph)
state_list = []
# Iterate through all possible combinations of cannibals, missionaries, and boat positions
for c in range (initial_state[0] + 1):      # # of cannibals
    for m in range (initial_state[1] + 1):  # # of missionaries
        for b in range (2):                 # # of boats
            if is_state_valid([c,m,b], initial_state): # Check if state is valid
                state_list.append((c,m,b)) # Saved as tuple, sinces lists are unhashable

# Create Map of Nodes (Graph - state as key with adjacency list as value)
states = {}
# Find valid connections, by iterating through state_list against itself
for state1 in state_list:
    connected_states = []
    for state2 in state_list:
        if is_edge_valid(state1, state2, boat_capacity): # Check if edge is valid
            connected_states.append(state2)           # Add to adjacency list
    states.update({state1 : connected_states}) # Add node to graph with adjacency list
    
#for s in state_list:
#    print(s,":",states[s])

# Conduct breadth-first search of graph:
steps = search_graph(states, initial_state, final_state)

if steps != None: # Print out steps in solution
    print("Solution found in {} steps:\n".format(len(steps)-1)) # steps includes start state
    print("   Near Side |~~~|  Far Side" + " "*29 + "Near Side |~~~|  Far Side ")
    print("    C   M    |~~~|   C   M  " + " "*29 + "  C   M   |~~~|    C   M  ")
    print("-------------|~~~|----------" + "-"*29 + "----------|~~~|-----------")
          
    for i in range(len(steps)-1): # Go through steps to show before and after states
        nearA = steps[i]    # current near side is described by current state
        farA = [initial_state[j] - nearA[j] for j in range(3)] # far side is what's left
        
        nearB = steps[i+1]  # next step is the state for near side for after the move
        farB = [initial_state[j] - nearB[j] for j in range(3)] # far side is what's left
        
        if nearA[2] == 1: # Boat starts on near side
            boat = [farB[j] - farA[j] for j in range(2)] # difference in state for c and m
            direction = ">"
        else:             # Boat starts on far side
            boat = [nearB[j] - nearA[j] for j in range(2)] # difference in state
            direction = "<"

        passengers = " " # Build up a description of boat passengers
        if boat[0] >= 2:    passengers = " {} Cannibals ".format(boat[0])
        elif boat[0] == 1:  passengers = " 1 Cannibal "
        if boat[1] >= 2:    passengers += "{} Missionaries ".format(boat[1])
        elif boat[1] == 1:  passengers += "1 Missionary "
                        
        move = ("{:" + direction + "^29}").format(passengers) # adds direction '<' or '>'
        
        if nearA[2] == 1: # Only print left side values when boat is on near side
            print("    {}   {}   B|~~~|   {}   {}   {:29}         |~~~|           "
                  .format(nearA[0], nearA[1], farA[0], farA[1],""))
        
        print("{:2}:          |~~~|          {:s}          |~~~|           ".format(i+1,move))
            
        if farB[2] == 1:  # Only print right side values when boat is on far side
            print("             |~~~|          {:29}  {}   {}   |~~~|B   {}   {}  "
                  .format("", nearB[0], nearB[1], farB[0], farB[1]))
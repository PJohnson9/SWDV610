# Patrick Johnson        10/23/2019 #
# SWDV 610 3W 19/FA2    Week 3 - #1 #
#####################################

def find_min_max(sequence):
    """ Finds the minimum and maximum values of a sequence recursively.
    Returns a list with the minimum value first and the maximum value second."""
    if len(sequence) == 1:
        return [sequence[0], sequence[0]]
    elif len(sequence) == 2:
        if sequence[0] < sequence[1]:
            return sequence
        else:
            return [sequence[1], sequence[0]]

    elif len(sequence) == 3:
        if sequence[0] > sequence[1]:
            sequence[0],sequence[1] = sequence[1],sequence[0]
        if sequence[1] > sequence[2]:
            sequence[2],sequence[1] = sequence[1],sequence[2]
            if sequence[0] > sequence[1]:
                sequence[0] = sequence[1]      
        return [sequence[0],sequence[2]]

    else:
        return find_min_max([sequence[0]] + find_min_max(sequence[1:]))



if __name__ == "__main__":
    print(find_min_max([10,9,8,7,6,5,4,3,2,1]))
    print(find_min_max([1,2,3,4,5,6,7,8,9,10]))
    print(find_min_max([10, 2, 2, 2, 1, 2, 9, 7, 2, 6, -96,
                        15, 44, 96, 25, 27, 27, 0, -85, 34]))

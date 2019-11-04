# Patrick Johnson         11/4/2019 #
# SWDV 610 3W 19/FA2    Week 3 - #2 #
#####################################

def reverse(sequence):
    """ Recursively reverses a list"""
    if len(sequence) <= 1:
        return sequence

    else:
        return reverse(sequence[1:]) + [sequence[0]]


if __name__ == "__main__":
    print(reverse([10,9,8,7,6,5,4,3,2,1]))
    print(reverse([1,2,3,4,5,6,7,8,9,10]))
    print(reverse([10, 2, 2, 2, 1, 2, 9, 7, 2, 6, -96,
                        15, 44, 96, 25, 27, 27, 0, -85, 34]))
    print(reverse(range(2)))
    print(reverse([42]))

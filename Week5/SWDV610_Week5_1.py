# Patrick Johnson        11/24/2019 #
# SWDV 610 3W 19/FA2    Week 5 - #1 #
#####################################

# Bubble, Select, and Insertion Sorts
# Hash Function
# Not actually sure about this part of the assignment,
# just guessing based on the rubric

def bubble_sort(list_to_sort):
    l = list_to_sort # Just a shorter reference
    i = 1 # Iterator for each pass
    swapped = True # Assume list needs to be sorted before first pass
    while swapped == True and i < len(l):      
        swapped = False # Set false at start of each pass
        for j in range(len(l) - i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        i += 1
    return l 


def selection_sort(list_to_sort):
    l = list_to_sort # Just a shorter reference  
    for i in range(len(l) - 1, 0, -1): # i starts with last index and works to 0
        max_index = 0 
        for j in range(1, i+1):
            if l[j] > l[max_index]:
                max_index = j
            l[i], l[max_index] = l[max_index], l[i]
    return l


def insertion_sort(list_to_sort):
    l = list_to_sort
    for sorted_count in range(1,len(l)):
        index = sorted_count
        value_to_insert = l[index]
        
        while index > 0 and l[index-1] > value_to_insert:
            l[index] = l[index-1]
            index -= 1
        l[index] = value_to_insert
    return l
    

def hash(number, bin_count): # implementation of a folding hash
    folded_sum = 0
    while number > 0:
        folded_sum += number % 100  # Take last two digits from number for sum
        number = number//100        # Remove last two digits from number
    return folded_sum % bin_count


if __name__ == "__main__":
    unsorted = [8,1,6,3,4,2,5,9,7]
    
    l = unsorted[:] # copy list
    print(l, end=" -> ")
    print(bubble_sort(l))
    
    l = unsorted[:]
    print(l, end=" -> ")
    print(selection_sort(l))
    
    l = unsorted[:]
    print(l, end=" -> ")
    print(insertion_sort(l))
    
    alist = [54,26,93,17,77,31,44,55,20]
    print(alist, end=" -> ")   
    insertion_sort(alist)
    print(alist)    
        
    print(hash(4365554601,11))
    print(hash(8675309,11))
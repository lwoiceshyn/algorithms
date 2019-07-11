def insertion_sort(l):
    '''
    Sorts a list of values for which the comparison operators are valid using insertion sort.
    Uses a shuffle operation to place values into the sublist rather than swapping values.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for i in range(1, len(l)):
        current_index = i
        current_value = l[i]
        while current_index > 0 and current_value < l[current_index-1]:
            l[current_index] = l[current_index-1]
            current_index -= 1
        l[current_index] = current_value
        print(l)
    return l

if __name__ == "__main__":
	unsorted_list [1,7,5,2,9,3,4,-5,10,15,25]
	print('Input List:', unsorted_list)
	output_list = insertion_sort(unsorted_list)
	print('Output List:', output_list)
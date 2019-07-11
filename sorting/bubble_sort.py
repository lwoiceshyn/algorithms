def bubble_sort(l):
    '''
    Sorts a list of integer values, in ascending fashion, using the bubblesort algorithm.
    Since the max value is guaranteed to reach its appropriate spot at the end of the list each iteration,
    we can reduce our iteration value by 1 each time.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for iter_range in range(len(l)-1, 0, -1):
        for i in range(iter_range):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l

if __name__ == "__main__":
	unsorted_list [1,7,5,2,9,3,4,5,10,15,25]
	print('Input List:', unsorted_list)
	output_list = bubble_sort(unsorted_list)
	print('Output List:', output_list)

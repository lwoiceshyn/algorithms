def selection_sort(l):
    '''
    Sorts a list of integers using selection sort.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for fill_slot in range(len(l)-1,0, -1):
        max_index = 0
        for i in range(1, fill_slot+1):
            if l[i] > l[max_index]:
                max_index = i
        l[fill_slot], l[max_index] = l[max_index], l[fill_slot]
    return l

if __name__ == "__main__":
	unsorted_list [1,7,5,2,9,3,4,-5,10,15,25]
	print('Input List:', unsorted_list)
	output_list = selection_sort(unsorted_list)
	print('Output List:', output_list)





def quick_sort(l):
    '''
    Sorts a list of values for which the comparison operators are valid using quick sort.
    
    Time Complexity: Worse case O(n^2), Average case O(nlog(n))
    Space Complexity: O(n)
    '''
    if len(l) == 1 or len(l) == 0:
        return l
    
    pivot = l[-1]
    i = 0
    j = len(l)-2
    
    while i <= j:
        if l[i] > pivot:
            if l[j] < pivot:
                l[i], l[j] = l[j], l[i]
                i += 1
            else:
                j -= 1
        else:
            i += 1
            
    l[i], l[-1] = l[-1], l[i]
    left = quick_sort(l[:i])
    right = quick_sort(l[i+1:])
    left.append(pivot)
    return left + right


def quick_sort_inplace(l, low, high):
	 '''
    Sorts a list of values for which the comparison operators are valid using quick sort.
    
    Time Complexity: Worse case O(n^2), Average case O(nlog(n))
    Space Complexity: O(1)
    '''
    def partition(l,low,high):
        pivot = l[high]
        i = low-1         
        for j in range(low,high):
            if l[j] <= pivot: 
                i = i+1 
                l[i],l[j] = l[j],l[i] 
        l[i+1],l[high] = l[high],l[i+1] 
        return i+1 
    if low < high: 
        pivot = partition(l,low,high)  
        quick_sort_inplace(l, low, pivot-1) 
        quick_sort_inplace(l, pivot+1, high) 

if __name__ == "__main__":
    unsorted_list [1,7,5,2,9,3,4,-5,10,15,25]
    print('Input List:', unsorted_list)
    output_list = quick_sort(unsorted_list)
    print('Quick Sort Output:', output_list)
    unsorted_list [1,7,5,2,9,3,4,-5,10,15,25]
    quick_sort_inplace(unsorted_list,0,len(unsorted_list)-1)
    print('In-place Quick Sort Output:', output_list)
def merge_sort(l):
    '''
    Sorts a list of values for which the comparison operators are valid using merge sort.
    
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    '''
    def merge(a,b):
        '''
        Merges two ordered lists (a and b) while retaining ordering.
        '''
        c = []
        while len(a) > 0 and len(b) > 0:
            if a[0] < b[0]:
                c.append(a[0])
                a.pop(0)
            else:
                c.append(b[0])
                b.pop(0)
            
        if len(a) > 0:
            c += a
        else:
            c += b
        return c
    
    if len(l) == 1 or len(l) == 0:
        return l
    
    else:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        a = merge_sort(left)
        b = merge_sort(right)
        return merge(a,b)
        
if __name__ == "__main__":
    unsorted_list [1,7,5,2,9,3,4,-5,10,15,25]
    print('Input List:', unsorted_list)
    output_list = merge_sort(unsorted_list)
    print('Output List:', output_list)
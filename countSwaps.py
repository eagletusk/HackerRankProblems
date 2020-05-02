def countSwaps(a):
    '''
    for (int i = 0; i < n; i++) {
        
        for (int j = 0; j < n - 1; j++) {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
            }
        }
        
    }
    '''
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            # print(i,j)
            if a[j]> a[j+1]:
                count +=1
                a[j],a[j+1] = a[j+1],a[j]
    # print(a)            
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
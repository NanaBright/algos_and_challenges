def bitonic_sort(up, x):
    if len(x) <= 1:
        return x
    else:
        first = bitonic_sort(True, x[:len(x) // 2])
        second = bitonic_sort(False, x[len(x) // 2:])
        return bitonic_merge(up, first + second)
    
def bitonic_merge(up, x):
    # assume input x is bitonic and sorted list is returned
    if len(x) == 1:
        return x
    else:
        bitonic_compare(up, x)
        first = bitonic_merge(up, x[:len(x) // 2])
        second = bitonic_merge(up, x[len(x) //2:])
        return first + second
    
def bitonic_compare(up, x):
    dist = len(x) // 2
    for i in range(dist):
        if (x[i] > x[i + dist]) == up:
            x[i], x[i + dist] = x[i + dist], x[i] #swap

#>>> bitonic_sort(True, [10, 30, 11, 20, 4, 330, 21, 110])
#[4, 10, 11, 20, 21, 30, 110, 330]
#>>> bitonic_sort(False, [10, 30, 11, 20, 4, 330, 21, 110])
#[330, 110, 30, 21, 20, 11, 10, 4]

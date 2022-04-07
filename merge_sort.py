#!/usr/bin/env python3
def merge_sort(a):
    if len(a) > 1:
        m = len(a)//2
        l = a[:m]
        r = a[m:]
        merge_sort(l)
        merge_sort(r)
        size_l = len(l)
        size_r = len(r)
        # i curr element of l
        # j curr element of r
        # k curr element of a
        i = j = k = 0
        while True:
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
                k += 1
                if i == size_l:
                    while j < size_r:
                        a[k] = r[j]
                        j += 1
                        k += 1
                    return 
            else:
                a[k] = r[j]
                j += 1
                k += 1
                if j == size_r:
                    while i < size_l:
                        a[k] = l[i]
                        i += 1
                        k += 1
                    return 

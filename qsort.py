#!/usr/bin/env python3
def qsort(a,l,r):
    if l < r:
        p = part(a,l,r)
        qsort(a,l,p-1)
        qsort(a,p+1,r)

def part(a,l,r):
    #swap middle element with the left most
    a[l],a[(l+r)//2] = a[(l+r)//2], a[l]
    #pivot_index
    p_i = l
    #pivot value
    p = a[p_i]
    while l<r:
        while l < len(a) and a[l] <= p:
            l = l+1
        while a[r] > p:
            r = r-1
        #Check for overlap
        if l < r:
            #swap misplaced elements
            a[l], a[r] = a[r], a[l]
    #put pivot in the correct place
    a[p_i],a[r] = a[r], a[p_i]
    return r

#!/usr/bin/python

import random
OKGREEN = '\033[92m'
ENDC = '\033[0m'

def print_arr(a,*ind):
    print("[",end="")
    for idx, x  in enumerate(a):
        if idx in ind:
            print(OKGREEN+str(x)+ENDC+",",end="")
        else:
            print(str(x)+",",end="")
    print("]")
    return

def qsort(a, l, r):
    if l < r:
        #print(a[l:r])
        p = part(a, l, r)
        qsort(a, l, p-1)
        qsort(a, p+1, r)


def part(a, l, r):
    # swap middle element with the left most
    (a[l], a[(l + r) // 2]) = (a[(l + r) // 2], a[l])
    # pivot_index
    p_i = l
    # pivot value
    p = a[p_i]
    while l < r:
        while l < len(a) and a[l] <= p:
            l = l + 1
        while a[r] > p:
            r = r - 1
        # Check for overlap
        if l < r:
            # swap misplaced elements
            (a[l], a[r]) = (a[r], a[l])
    # put pivot in the correct place
    (a[p_i], a[r]) = (a[r], a[p_i])
    return r
def randarr(n):
    a = list()
    for i in range(n):
        a.append(random.randint(0,2*n))
    return a

if __name__ == "__main__":
    a = randarr(150)
    print("Strt:",a)
    qsort(a,0,len(a)-1)
    print("Res:",a)

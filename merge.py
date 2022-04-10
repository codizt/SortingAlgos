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


def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        l = a[:m]
        r = a[m:]
        #print(l,r)
        merge_sort(l)
        merge_sort(r)
        size_l = len(l)
        size_r = len(r)
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
                
def randarr(n):
    a = list()
    for i in range(n):
        a.append(random.randint(0,2*n))
    return a

if __name__ == "__main__":
    a = randarr(150)
    print("Strt:",a)
    merge_sort(a)
    print("Res:",a)

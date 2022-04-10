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


def insertionSort(unsortedList):
    for i in range(1, len(unsortedList)):
        key = unsortedList[i]
        ptr = i-1
        while ptr >= 0 and unsortedList[ptr] > key:
            unsortedList[ptr + 1] = unsortedList[ptr]
            ptr -= 1
            #print_arr(a,ptr,ptr+1)
        unsortedList[ptr + 1] = key
    return

def randarr(n):
    a = list()
    for i in range(n):
        a.append(random.randint(0,2*n))
    return a

if __name__ == "__main__":
    a = randarr(150)
    print("Strt:",a)
    insertionSort(a)
    print("Res:",a)


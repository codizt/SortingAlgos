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

def selectionSort(unsortedList):
    for i in range(len(unsortedList)):
        minIndex = i
        for j in range(i + 1, len(unsortedList)):
            if unsortedList[minIndex] > unsortedList[j]:
                minIndex = j
        #print_arr(a,i,minIndex)
        (unsortedList[i], unsortedList[minIndex]) = \
            (unsortedList[minIndex], unsortedList[i])
    return

def randarr(n):
    a = list()
    for i in range(n):
        a.append(random.randint(0,2*n))
    return a

if __name__ == "__main__":
    a = randarr(150)
    print("Strt:",a)
    selectionSort(a)
    print("Res:",a)


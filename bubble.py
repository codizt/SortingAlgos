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
def bubbleSort(unsortedList):
    for i in range(len(unsortedList)):
        for j in range(len(unsortedList) - 1 - i):
            if unsortedList[j] > unsortedList[j + 1]:
                print_arr(a,j,j+1)
                unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
    return


def randarr(n):
    a = list()
    for i in range(n):
        a.append(random.randint(0,2*n))
    return a

if __name__ == "__main__":
    a = randarr(10)
    print("Strt:",a)
    bubbleSort(a)
    print("Res:",a)

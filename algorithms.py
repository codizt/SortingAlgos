#!/usr/bin/python

def bubbleSort(unsortedList):
    for i in range(len(unsortedList)):
        for j in range(len(unsortedList) - 1 - i):
            if unsortedList[j] > unsortedList[j + 1]:
                t = unsortedList[j]
                unsortedList[j] = unsortedList[j + 1]
                unsortedList[j + 1] = t
    return

def selectionSort(unsortedList):
    for i in range(len(unsortedList)):
        minIndex = i
        for j in range(i + 1, len(unsortedList)):
            if unsortedList[minIndex] > unsortedList[j]:
                minIndex = j
        (unsortedList[i], unsortedList[minIndex]) = \
            (unsortedList[minIndex], unsortedList[i])
    return


def insertionSort(unsortedList):
    for i in range(1, len(unsortedList)):
        key = unsortedList[i]

        while ptr >= 0 and unsortedList[ptr] > key:
            unsortedList[ptr + 1] = unsortedList[ptr]
            ptr -= 1
        unsortedList[ptr + 1] = key
    return

def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        l = a[:m]
        r = a[m:]
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


def qsort(a, l, r):
    t_comp += 1
    if l < r:
        p = part(a, l, r)
        qsort(a, l, p - 1)
        qsort(a, p + 1, r)


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

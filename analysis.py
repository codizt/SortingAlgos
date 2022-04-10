#!/usr/bin/python
import random
from time import perf_counter_ns
import numpy as np
import matplotlib.pyplot as plt
from sys import maxsize
import tracemalloc
plt.rcParams.update({
    "font.family": "monospace",
})


def plotter(title, ylabel, values, filename):
    n = np.array(range(1,len(values["Bubble Sort"])+1))
    bubble = np.array(values["Bubble Sort"])
    select = np.array(values["Selection Sort"])
    insert = np.array(values["Insertion Sort"])
    merge = np.array(values["Merge Sort"])
    quick = np.array(values["Quick Sort"])


    plt.title(title)
    plt.xlabel("Size of Array")
    plt.ylabel(ylabel)
    plt.plot(n, bubble, color='red', label="Bubble")
    plt.plot(n, select, color='lawngreen', label="Selection")
    plt.plot(n, insert, color='springgreen', label="Insertion")
    plt.plot(n, merge, color='cyan', label="Merge")
    plt.plot(n, quick, color='magenta', label="Quick")
    plt.legend()
    plt.savefig(filename, backend="pgf")
    plt.close()

def singlePlotter(title, ylabel, values, filename,l):
    n = np.array(range(1,len(values)+1))
    arr = np.array(values)

    plt.title(title)
    plt.xlabel("Size of Array")
    plt.ylabel(ylabel)
    plt.plot(n, arr, color='springgreen',label=l)
    plt.legend()
    plt.savefig(filename,backend="pgf")
    plt.close()

def genShuffledArrays(n):
    suffledArrayCollection = []

    for i in range(100,n+101):
        a =  np.random.randint(0, maxsize, size=(i))
        suffledArrayCollection.append(a)

    return suffledArrayCollection


def bubbleSort(unsortedList):
    swap = 0
    itr = 0
    comp = 0
    tracemalloc.start()
    t_s = perf_counter_ns()
    for i in range(len(unsortedList)):
        for j in range(len(unsortedList) - 1 - i):
            itr += 1
            comp += 1
            if unsortedList[j] > unsortedList[j + 1]:
                t = unsortedList[j]
                unsortedList[j] = unsortedList[j + 1]
                unsortedList[j + 1] = t
                swap += 1
    t_e = perf_counter_ns()
    mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return {"Time":t_e-t_s,
            "Memory":mem,
            "Comparisons":comp,
            "Swaps":swap,
            "Iterations":itr}


def selectionSort(unsortedList):
    swap = 0
    itr = 0
    comp = 0
    tracemalloc.start()
    t_s = perf_counter_ns()
    for i in range(len(unsortedList)):
        minIndex = i
        for j in range(i + 1, len(unsortedList)):
            itr += 1
            comp += 1
            if unsortedList[minIndex] > unsortedList[j]:
                minIndex = j
        (unsortedList[i], unsortedList[minIndex]) = \
            (unsortedList[minIndex], unsortedList[i])
        swap += 1
    t_e = perf_counter_ns()
    mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return {"Time":t_e-t_s,
            "Memory":mem,
            "Comparisons":comp,
            "Swaps":swap,
            "Iterations":itr}


def insertionSort(unsortedList):
    swap = 0
    itr = 0
    comp = 0
    tracemalloc.start()
    t_s = perf_counter_ns()
    for i in range(1, len(unsortedList)):
        itr += 1
        key = unsortedList[i]
        ptr = i - 1
        comp += 1

        while ptr >= 0 and unsortedList[ptr] > key:
            unsortedList[ptr + 1] = unsortedList[ptr]
            ptr -= 1
            swap += 1
            itr += 1

        unsortedList[ptr + 1] = key
    t_e = perf_counter_ns()
    mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return {"Time":t_e-t_s,
            "Memory":mem,
            "Comparisons":comp,
            "Swaps":swap,
            "Iterations":itr}

def merge_sort(a):
    global t_comp
    global t_swap
    global t_itr
    if len(a) > 1:
        m = len(a) // 2
        l = a[:m]
        r = a[m:]
        merge_sort(l)
        t_itr+=1
        merge_sort(r)
        t_itr+=1
        size_l = len(l)
        size_r = len(r)
        i = j = k = 0
        while True:
            t_comp += 1
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
                k += 1
                t_comp += 1
                if i == size_l:
                    while j < size_r:
                        a[k] = r[j]
                        j += 1
                        k += 1
                    return
            else:
                t_swap += 1
                a[k] = r[j]
                j += 1
                k += 1
                t_comp += 1
                if j == size_r:
                    while i < size_l:
                        a[k] = l[i]
                        i += 1
                        k += 1
                    return


def qsort(a, l, r):
    global t_comp
    global t_swap
    global t_itr
    t_comp += 1
    if l < r:
        p = part(a, l, r)
        qsort(a, l, p - 1)
        t_itr += 1
        qsort(a, p + 1, r)
        t_itr += 1


def part(a, l, r):
    global t_comp
    global t_swap
    global t_itr
    t_swap += 1
    # swap middle element with the left most
    (a[l], a[(l + r) // 2]) = (a[(l + r) // 2], a[l])
    # pivot_index
    p_i = l
    # pivot value
    p = a[p_i]
    while l < r:
        t_comp += 1
        while l < len(a) and a[l] <= p:
            t_comp += 1
            l = l + 1
        while a[r] > p:
            t_comp += 1
            r = r - 1
        # Check for overlap
        if l < r:
            t_comp += 1
            t_swap += 1
            # swap misplaced elements
            (a[l], a[r]) = (a[r], a[l])
    t_swap += 1
    # put pivot in the correct place
    (a[p_i], a[r]) = (a[r], a[p_i])
    return r

def copy_to_arr(tmp,ind):
    global time_taken
    global mem
    global comp
    global swap
    global itr
    time_taken[ind].append(tmp["Time"])
    mem[ind].append(tmp["Memory"])
    comp[ind].append(tmp["Comparisons"])
    swap[ind].append(tmp["Swaps"])
    itr[ind].append(tmp["Iterations"])


if __name__ == "__main__":
    shuffledArrayCollection = genShuffledArrays(1000)
    time_taken ={"Bubble Sort":list(), "Selection Sort":list(), "Insertion Sort":list(), "Merge Sort":list(), "Quick Sort":list()}
    mem ={"Bubble Sort":list(), "Selection Sort":list(), "Insertion Sort":list(), "Merge Sort":list(), "Quick Sort":list()}
    comp ={"Bubble Sort":list(), "Selection Sort":list(), "Insertion Sort":list(), "Merge Sort":list(), "Quick Sort":list()}
    swap ={"Bubble Sort":list(), "Selection Sort":list(), "Insertion Sort":list(), "Merge Sort":list(), "Quick Sort":list()}
    itr ={"Bubble Sort":list(), "Selection Sort":list(), "Insertion Sort":list(), "Merge Sort":list(), "Quick Sort":list()}
    j = 1
    for i in shuffledArrayCollection:
        tmp = bubbleSort(i.copy())
        copy_to_arr(tmp,"Bubble Sort")
        tmp = insertionSort(i.copy())
        copy_to_arr(tmp,"Insertion Sort")
        tmp = selectionSort(i.copy())
        copy_to_arr(tmp,"Selection Sort")
        
        t_comp = 0
        t_swap = 0
        t_itr = 0
        tracemalloc.start()
        t_s = perf_counter_ns()
        merge_sort(i.copy())
        t_e = perf_counter_ns()
        memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        tmp = {"Time":t_e-t_s,
            "Memory":memory,
            "Comparisons":t_comp,
            "Swaps":t_swap,
            "Iterations":t_itr}
        copy_to_arr(tmp,"Merge Sort")

        t_comp = 0
        t_swap = 0
        t_itr = 0
        tracemalloc.start()
        t_s = perf_counter_ns()
        qsort(i.copy(),0,len(i)-1)
        t_e = perf_counter_ns()
        memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        tmp = {"Time":t_e-t_s,
            "Memory":memory,
            "Comparisons":t_comp,
            "Swaps":t_swap,
            "Iterations":t_itr}
        copy_to_arr(tmp,"Quick Sort")
        print(j)
        j+=1
    singlePlotter("Bubble Sort Time vs Input size","Time",time_taken["Bubble Sort"],"bs_t.pgf","Bubble")
    singlePlotter("Selection Sort  Time vs Input size","Time",time_taken["Selection Sort"],"ss_t.pgf","Selection")
    singlePlotter("Insertion Sort Time vs Input size","Time",time_taken["Insertion Sort"],"is_t.pgf","Insertion")
    singlePlotter("Merge Sort Time vs Input size","Time",time_taken["Merge Sort"],"ms_t.pgf","Merge")
    singlePlotter("Quick Sort Time vs Input size","Time",time_taken["Quick Sort"],"qs_t.pgf","Quick")

    singlePlotter("Bubble Sort Memory vs Input size","Memory",mem["Bubble Sort"],"bs_m.pgf","Bubble")
    singlePlotter("Selection Sort Memory vs Input size","Memory",mem["Selection Sort"],"ss_m.pgf","Selection")
    singlePlotter("Insertion Sort Memory vs Input size","Memory",mem["Insertion Sort"],"is_m.pgf","Insertion")
    singlePlotter("Merge Sort Memory vs Input size","Memory",mem["Merge Sort"],"ms_m.pgf","Merge")
    singlePlotter("Quick Sort Memory vs Input size","Memory",mem["Quick Sort"],"qs_m.pgf","Quick")

    singlePlotter("Bubble Sort Comparisons vs Input size","Comparisons",comp["Bubble Sort"],"bs_c.pgf","Bubble")
    singlePlotter("Selection Sort Comparisons vs Input size","Comparisons",comp["Selection Sort"],"ss_c.pgf","Select")
    singlePlotter("Insertion Sort Comparisons vs Input size","Comparisons",comp["Insertion Sort"],"is_c.pgf","Insertion")
    singlePlotter("Merge Sort  Comparisons vs Input size","Comparisons",comp["Merge Sort"],"ms_c.pgf","Merge")
    singlePlotter("Quick Sort  Comparisons vs Input size","Comparisons",comp["Quick Sort"],"qs_c.pgf","Quick")

    singlePlotter("Bubble Sort Swaps vs Input size","Swaps",swap["Bubble Sort"],"bs_s.pgf","Bubble")
    singlePlotter("Selection Sort Swaps vs Input size","Swaps",swap["Selection Sort"],"ss_s.pgf","Selection")
    singlePlotter("Insertion Sort Swaps vs Input size","Swaps",swap["Insertion Sort"],"is_s.pgf","Insertion")
    singlePlotter("Merge Sort  Swaps vs Input size","Swaps",swap["Merge Sort"],"ms_s.pgf","Merge")
    singlePlotter("Quick Sort  Swaps vs Input size","Swaps",swap["Quick Sort"],"qs_s.pgf","Quick")

    singlePlotter("Bubble Sort Iterations vs Input size","Iterations",itr["Bubble Sort"],"bs_i.pgf","Bubble")
    singlePlotter("Selection Sort Iterations vs Input size","Iterations",itr["Selection Sort"],"ss_i.pgf","Selection")
    singlePlotter("Insertion Sort Iterations vs Input size","Iterations",itr["Insertion Sort"],"is_i.pgf","Insertion")
    singlePlotter("Merge Sort  Iterations vs Input size","Iterations",itr["Merge Sort"],"ms_i.pgf","Merge")
    singlePlotter("Quick Sort Iterations vs Input size","Iterations",itr["Quick Sort"],"qs_i.pgf","Quick")

    plotter("Time vs Input size","Time",time_taken,"t.pgf")
    plotter("Memory vs Input size","Memory",mem,"m.pgf")
    plotter("Comparisons vs Input size","Comparisons",comp,"c.pgf")
    plotter("Swaps vs Input size","Swaps",swap,"s.pgf")
    plotter("Iterations vs Input size","Iterations",itr,"i.pgf")

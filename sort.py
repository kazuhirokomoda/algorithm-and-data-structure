import sys
import time
import random

# data for sorting
def output_rand(length):
    data = []
    for i in range(length):
        data.append(random.randint(0,99)%100)
    return data


# selection sort
def selection_sort(data):
    length = len(data)
    for i in range(length-1):
        #print data
        min = data[i]
        min_pos = i
        for j in range(i+1, length):
            if min > data[j]:
                min = data[j]
                min_pos = j
        tmp = data[i]
        data[i] = min
        data[min_pos] = tmp


# bubble sort
def bubble_sort(data):
    length = len(data)
    for i in range(length):
        #print data
        for j in range(length-1, i, -1):
            if data[j-1] > data[j]:
                tmp = data[j-1]
                data[j-1] = data[j]
                data[j] = tmp


# heap sort
def heap_add(data, c):
    #length = len(data)
    while True:
        p = (c-1)/2
        if p < 0 or data[p] <= data[c]:
            break
        tmp = data[p]
        data[p] = data[c]
        data[c] = tmp
        c = p

def heap_del(data, p):
    length = len(data)
    while True:
        c = 2*p + 1
        if c >= length:
            break
        if c+1<length:
            if data[c]>data[c+1]:
                c += 1
        if data[p] <= data[c]:
            break
        tmp = data[p]
        data[p] = data[c]
        data[c] = tmp
        p = c

def heap_sort(data):
    length = len(data)
    # make first heap
    #print data
    for i in range(1, length):
        heap_add(data, i)
        #print data
    #print data
    for i in range(length/2 - 1, -1, -1):
        heap_del(data, i)


# merge_sort
def merge(data, left, right, size):
    tmp = dict()
    i = left
    j = right
    k = left
    l = left+size
    while i<right and j<l:
        if data[i]<data[j]:
            tmp[k] = data[i]
            i += 1
        else:
            tmp[k] = data[j]
            j += 1
        k += 1
    if i<right:
        for h in range(i, right):
            tmp[k] = data[h]
            k += 1
    if j<l:
        for h in range(j,l):
            tmp[k] = data[h]
            k += 1
    for h in range(left, l):
        #print 'h='+str(h)
        data[h] = tmp[h]

def merge_sort(data, left, right):
    #print data
    #print left, right
    if left<right:
        middle = (left+right)/2
        merge_sort(data, left, middle)
        merge_sort(data, middle+1, right)
        merge(data, left, middle+1, right-left+1)


# quick sort
def quick_sort(data, first, last):
    x = (data[first] + data[last])/2 # pivot (ex. average)
    i = first
    j = last
    while True:
        while data[i] < x:
            i += 1
        while x < data[j]:
            j -= 1
        if i>=j:
            break
        t = data[i]
        data[i] = data[j]
        data[j] = t
        i += 1
        j -= 1
    if first < i-1:
        quick_sort(data, first, i-1)
    if j+1 < last:
        quick_sort(data, j+1, last)


if __name__ == '__main__':
    data = output_rand(100000)
    #print data
    StartTime = time.time()
    #selection_sort(data)
    #bubble_sort(data)
    #heap_sort(data)
    #merge_sort(data, 0, len(data)-1)
    quick_sort(data, 0, len(data)-1)
    EndTime = time.time()
    #print data

    print 'Running Time:', EndTime-StartTime, '[sec]'

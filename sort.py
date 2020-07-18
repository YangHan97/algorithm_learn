def bubbleSort(alist):
    # for passnum in range(len(alist)-1, 0, -1):
    #     for i in passnum:
    #         if alist[i] > alist[i+1]:
    #             alist[i], alist[i+1] = alist[i+1], alist[i]

    passnum = len(alist)-1
    exchange = True
    while passnum > 0 and exchange:
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1

def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)
def partition(alist, first, last):
    p = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <=p:
            leftmark = leftmark + 1
        while rightmark >= leftmark and alist[rightmark] >= p:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark




alist = [92,61,32,56,12,63,22,72,100,83,5]
quickSort(alist)
print(alist)
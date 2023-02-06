import random
import time

user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())


def createMatrix(user_m, user_n, user_min_limit, user_max_limit):
    return [[random.randint(user_min_limit, user_max_limit) for i in range(user_m)] for j in range(user_n)]


# сортировка выбором
def selectionSortMatrix(matrix):
    def selectionSort(arr):
        for i in range(len(arr)):
            minInd = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minInd]:
                    minInd = j
            arr[minInd], arr[i] = arr[i], arr[minInd]
        return arr

    result = []
    for i in range(len(matrix)):
        result.append(selectionSort(matrix[i]))
    return result


# сортировка вставкой

def insertionSortMatrix(matrix):
    def insertionSort(arr):
        for i in range(len(arr)):
            cursor = arr[i]
            p = i
            while p < 0 and arr[p - 1] > cursor:
                arr[p] = arr[p - 1]
                p = p - 1
            arr[p] = cursor
        return arr

    result = []
    for i in range(len(matrix)):
        result.append(insertionSort(matrix[i]))
    return result


def bubbleSortMatrix(matrix):
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    result = []
    for i in range(len(matrix)):
        result.append(bubbleSort(matrix[i]))
    return result

def shellSortMatrix(matrix):
    def shellSort(arr):
        gap = len(arr)//2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j-gap]
                    j -= gap
                    arr[j] = temp
            gap //= 2
        return arr

    result = []
    for i in range(len(matrix)):
        result.append(shellSort(matrix[i]))
    return result


def quickSortMatrix(matrix):
    def quickSort(arr):
        less = []
        equal = []
        greater = []

        if len(arr) > 1:
            pivot = arr[0]
            for x in arr:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return quickSort(less) + equal + quickSort(greater)
        else:
            return arr

    result = []
    for i in range(len(matrix)):
        result.append(quickSort(matrix[i]))
    return result

def tournamentSortMatrix(matrix):
    def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
    def heapSort(arr):
            n = len(arr)
            for i in range(n, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
            return arr

    result = []
    for i in range(len(matrix)):
        result.append(heapSort(matrix[i]))
    return result

r = createMatrix(user_m, user_n, user_min_limit, user_max_limit)
print(r)
print(selectionSortMatrix(r))
print(insertionSortMatrix(r))
print(bubbleSortMatrix(r))
print(shellSortMatrix(r))
print(quickSortMatrix(r))
print(tournamentSortMatrix(r))

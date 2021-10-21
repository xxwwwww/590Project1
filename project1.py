"""
Math 560
Project 1
Fall 2021

Partner 1:
Partner 2:
Date:
"""

"""
SelectionSort

@listToSort : original list to be sorted
@return : sorted list

Time complexity :　O(n2) for all cases
"""
def SelectionSort(listToSort):
    # loop over all elments in list
    for i in range(len(listToSort)):
        # set the current (first in unsorted list) element as min
        min = listToSort[i]
        # loop over all the unsorted (following) list
        for j in range(i+1, len(listToSort)):
            # if find a new min, swap it with the first element in unsorted list
            if min > listToSort[j]:
                # swap min and new found min
                temp = min
                min = listToSort[j]
                listToSort[j] = temp
        # set the first element in unsorted list to be the minimal of the rest
        listToSort[i] = min

    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    # print('Testing Insertion Sort')
    # print()
    # testingSuite(InsertionSort)
    # print()
    # print('Testing Bubble Sort')
    # print()
    # testingSuite(BubbleSort)
    # print()
    # print('Testing Merge Sort')
    # print()
    # testingSuite(MergeSort)
    # print()
    # print('Testing Quick Sort')
    # print()
    # testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
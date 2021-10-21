"""
Math 560
Project 1
Fall 2021

Partner 1: Zezhong Zhang
Partner 2: Yitong Wang
Date: 10/21/2021
"""

from math import floor

"""
SelectionSort

@:listToSort original list to be sorted
@:return sorted list

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

@:listToSort the unsorted list to be sorted
@:i the left bound of this sorting step(inclusive)
@:j the right bound of this sorting step(exclusive)
@:return the sorted list
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)

    # if only one element left, return it
    if j <= (i+1):
        return listToSort

    # find a pivot which is the middle number in array
    m = floor((i+j)/2)

    # partition array, put all numbers smaller to left and all numbers bigger to right
    # set left pointer as l
    l = i
    # set right pointer as r
    r = j-1
    while l<r:
        # stop at pivot or an element bigger than pivot
        while (l < m) and (listToSort[l] < listToSort[m]):
            l+=1
        # stop at pivot or an element smaller than pivot
        while (r > m) and (listToSort[r] >= listToSort[m]):
            r-=1
        # swap the two elements
        if r > l :
            # swap the two
            temp = listToSort[r]
            listToSort[r] = listToSort[l]
            listToSort[l] = temp
            # if m is one of them, reset m
            if m==l:
                m = r
            elif m == r:
                m = l

    # recursively sort left part and right part
    QuickSort(listToSort, i, m)
    QuickSort(listToSort, m+1, j)

    # return sorted list
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
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
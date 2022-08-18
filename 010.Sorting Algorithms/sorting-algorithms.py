'''
Sort a list of integers using merge sort or bubble sort
Time the amount of time it takes to sort a list of integers
Compare the performance of the two sorting algorithms
'''

import random
import time

def performance_timer(func, data):
    start = time.time()
    func(data)
    end = time.time()
    return end - start
    
def merge_sort(data):
    # If the list has only one item, return the list as it is already sorted
    if len(data) <= 1:
        return data
    else:
        # Find the middle of the list
        mid = len(data) // 2
        # Split the list into two halves
        left = merge_sort(data[:mid])
        right = merge_sort(data[mid:])
        # Merge the two halves
        result = []
        # While both lists are populated
        while len(left) > 0 and len(right) > 0:
            # If the first item in the left list is less than the first item in the right list, 
            #  append the first item in the left list to the result list
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                # Otherwise, append the first item in the right list to the result list
                result.append(right.pop(0))
        # Append the remaining items in the left list to the result list
        if len(left) > 0:
            result.extend(left)
        # Append the remaining items in the right list to the result list
        if len(right) > 0:
            result.extend(right)
        # Finally, return the result list
        return result

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def main():
    data = [random.randint(0, 100) for i in range(1000)]
    print(f"Data: {data}")
    print(f"Merge Sort: {performance_timer(merge_sort, data)}")
    print(f"Merge Sorted Data: {merge_sort(data)}")
    print(f"Bubble Sort: {performance_timer(bubble_sort, data)}")
    print(f"Bubble Sorted Data: {bubble_sort(data)}")
    input()
    exit()

if __name__ == '__main__':
    main()
    exit()
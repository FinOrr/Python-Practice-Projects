'''
Closest Pair Problem:
    The closest pair problem is a problem of computational geometry:
    Given n point in metric space, find a pair of points with the
    smallest distance between them.
'''

import math
import random
import matplotlib.pyplot as plt

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
            if left[0][0] < right[0][0]:
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

def distance_between_points(point1, point2):
    # Calculate the distance between two points
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_closest_pair(data):
    # Find the closest pair of points
    closest_pair = None
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            # If the distance between the two points is less than the current closest pair, 
            #  set the closest pair to the new distance
            if closest_pair is None or distance_between_points(data[i], data[j]) < closest_pair:
                closest_pair = distance_between_points(data[i], data[j])
    return closest_pair

def main():
    # Generate 100 random points in the x-y axis
    points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(20)]
    # Generate a matplotlib plot of the points
    for point in points:
        plt.scatter(point[0], point[1])    
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='b', linestyle='--')
    plt.show()
    # Find the closest pair of points
    closest_pair = find_closest_pair(points)
    print(f"The closest pair of points are {closest_pair} apart.")
    input()

if __name__ == '__main__':
    main()
    exit()
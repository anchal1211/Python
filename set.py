#Q.1 Write a Python program to Get Only unique items from two sets.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1.symmetric_difference(set2)

print("Unique items from both sets:", unique_items)


#Q.2 Write a Python program to Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_elements = set1.symmetric_difference(set2)

print("Elements present in Set A or B, but not both:", unique_elements)

 
#Q.3 Write a Python program to Check if two sets have any elements in common. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

common_elements = set1.intersection(set2)

if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements.")


#Q.4 Write a Python program to Remove items from set1 that are not common to both set1 and set2.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)

print("Updated set1 with common elements:", set1)

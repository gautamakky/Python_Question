def intersection_of_three(l1, l2, l3):
    return list(set(l1) & set(l2) & set(l3))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [0, 3, 5, 9]

result = intersection_of_three(list1, list2, list3)
print("Intersection:", result)
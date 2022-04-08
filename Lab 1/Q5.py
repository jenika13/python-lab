a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a_set = set(a)
b_set = set(b)
cmn_ele = a_set.intersection(b_set)
print("The common elements are {}".format(cmn_ele))
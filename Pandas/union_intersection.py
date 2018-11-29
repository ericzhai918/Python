a=[2,3,4,7,5]
b=[2,5,7,8,9]

a_set = set(a)
b_set = set(b)
union_data = a_set.union(b_set)
print(union_data)

intersection_data = a_set.intersection(b_set)
print(intersection_data)

difference_data = a_set.difference(b_set)
print(difference_data)
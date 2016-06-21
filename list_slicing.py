# -- list slicing
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[2:8])


# -- inverting list
print(a[::-1])


# -- list slicing with negative step
print(a[::-2])


# -- list slice assignment
a = [1, 2, 3, 4, 5, 6, 7]
a[2:3] = [0, 0]
print(a)

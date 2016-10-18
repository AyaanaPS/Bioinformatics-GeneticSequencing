
#This is the splitting part of the merge sort algorithm.
#Here, the inputted array is recursively split into many
#subsequences. The merge function is then called on these
#sequences.
def merge_sort(m):
    if len(m) <= 1:
        return m

    left = []
    right = []

    for i in range(len(m)):
        if i%2 != 0:
            left.append(m[i])
        else:
            right.append(m[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

#The merge function decides how to combine the elements of
#the two inputted lists so that the list is sorted. This is
#done by comparing the elements. The function returns a sorted
#list.
def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result.extend(left)
    result.extend(right)

    return result

#Example Case
lst = [3, 5, 1, 2, 10, 9]
print merge_sort(lst)
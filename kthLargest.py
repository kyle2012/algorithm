def partition(begin, end, array):
    if begin >= end:
        return
    keyword = array[begin]
    while begin < end:
        while array[end] >= keyword and begin < end:
            end = end - 1
        array[begin] = array[end]
        while array[begin] <= keyword and begin < end:
            begin = begin + 1
        array[end] = array[begin]
        array[begin] = keyword

    return begin


def main(array, k):
    begin = 0
    end = len(array) - 1
    print(kthLargest(array, begin, end, k))

def kthLargest(array, begin, end, k):
    i = partition(begin, end, array)
    if i == len(array) - k:
        return array[i: i+1]
    elif i > len(array) - k:
        return kthLargest(array, 0, i - 1, k)
    elif i < len(array) - k:
        return kthLargest(array, i + 1, len(array) - 1, k)
    return 0

main([6,1,22,2,3,10,8,9], 1)

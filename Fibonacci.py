import datetime
result = {0: None, 1: 1, 2: 2, 3: 3, 4: 5}
def getFibonacciNumByIndexRecursive(n):
    if result.get(n):
        return result[n]
    if n%2 == 0:
        index = n/2 - 1
        result[n] = getFibonacciNumByIndexRecursive(index)*getFibonacciNumByIndexRecursive(index) + \
                getFibonacciNumByIndexRecursive(index+1)*getFibonacciNumByIndexRecursive(index+1)
    else:
        index = (n-1)/2
        result[n] = getFibonacciNumByIndexRecursive(index)*getFibonacciNumByIndexRecursive(index-1) + \
    getFibonacciNumByIndexRecursive(index)*getFibonacciNumByIndexRecursive(index+1)
    return result[n]

def getFibonacciIndex(n):
    indexList = [n]
    while n > 5:
        if n == 0:
            return None
        if n%2 == 0:
            n = n - 1
        index = (n-1)/2

        indexList = [index+1] + indexList
        indexList = [index] + indexList
        indexList = [index-1] + indexList
        n = index
    print(indexList)


index = 1000000
getFibonacciNumByIter(index)

# s_time = datetime.datetime.now()
# getFibonacciNumByIndexRecursive(index)
# e_time = datetime.datetime.now()
# print(e_time - s_time)
# print(len(str(result.get(index))))

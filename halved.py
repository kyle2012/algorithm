def halvedQuery(array, start, end, keyword):
    middle = int((start + end)/2)
    if middle == start or middle == end:
        if array[middle] == keyword:
            return middle
        else:
            print('not found')
            return - 1
    print(start, end, middle)
    if keyword == array[middle]:
        if keyword == array[middle - 1]:
            halvedQuery(array, start, middle - 1, keyword)
        # if keyword == array[middle + 1]:
            # halvedQuery(array, middle + 1, end, keyword)
        else:
            print('founded at index:', middle)
            return middle
    elif keyword < array[middle]:
        halvedQuery(array, start, middle, keyword)
    else:
        halvedQuery(array, middle, end, keyword)



exampleArray = [1,2,3,4,5,6,7,8,9,10,100,100,100,100,100,1000,10000]
halvedQuery(exampleArray, 0, len(exampleArray), 10000)

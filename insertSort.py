def insertSort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            # array[j] = temp
            j = j - 1

        # if j != i - 1: #if not self
        array[j+1] = temp
    print(array)

def binaryInsertSort(array):

    print(array)

insertSort([6,9,2,1,3,10])

from __future__ import print_function

def printByCount(n):
    if n == 0:
        return;
    if n > 0:
        strList = [str(x) for x in range(1, 10)]
        resMap = {1: strList}
        for i in range(1, n):
            resMap[i+1] = getList(resMap.get(i), i)

        for key, arr in resMap.iteritems():
            for val in arr:
                tmp = val
                if len(val) < n:
                    tmp = val + " "*(n-len(val))
                print(tmp, end=" ")

def getList(strList, index):
    newArr = []
    for s in strList:
        for i in range(0, 10):
            tmp = s + str(i)
            newArr.append(tmp)
    return newArr


printByCount(3)

class SudoSolver:
    def main():
        self.init = [
                [5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9],
                ]
        solve()

    def solve():
        for j in range(0, 3):
            rows_begin = j * 3
            for i in range(0, 3):
                cols_begin = i * 3
                seeds = getSeeds(cols_begin, rows_begin)
                for f in range(0, 3):
                    y = rows_begin + f
                    for g in range(0, 3):
                       x = cols_begin + g
                       index = 0
                       while index < len(seeds):
                           fill = seeds[index]
                           if not self[x][y]:
                               self[x][y] = fill
                               if isValid(x, y):
                                   index = index + 1


    def fillRow(x, y, f):
        while f < 10:
            self.init[x][y] = f
            if isValid(x, y):
                break
            f = f + 1
        if f >= 10:
            return False
        else:
            return True

    def getSeeds(x, y):
        row_begin = y/3 * 3
        cols_begin = x/3 * 3
        exists = set()
        for i in range(3):
            for j in range(3):
                exists.add(self.init[rows_begin+i][cols_begin+j])
        all_seeds = set([x for x in range(1, 10)])
        return list(all_seeds - exists)

    def isValid(x, y):
        return isValidSqt(x, y) and isValidRows(x, y) and isValidCols(x, y)


    def isValidRows(x, y):
        sum = 0
        duplicates = {}
        for i in (1, 10):
            sum = sum + self.init[y][i]
            if i != 0:
                if duplicates.get(i):
                    return False
                duplicates[i] = 1
        if sum > 45:
            return False
        return True

    def isValidCols(x, y):
        sum = 0
        duplicates = {}
        for i in (1, 10):
            sum = sum + self.init[i][x]
            if i != 0:
                if duplicates.get(i):
                    return False
                duplicates[i] = 1
        if sum > 45:
            return False
        return True

    def isValidSqt(x, y):
        sum = 0
        row_begin = y/3 * 3
        cols_begin = x/3 * 3
        for i in range(3):
            for j in range(3):
                sum = self.init[row_begin+i][cols_begin+j]

        if sum > 45:
            return False
        return True

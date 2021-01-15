a = [
    [3, 0, 4, 0, 9, 0, 1, 6, 0],
    [8, 6, 0, 0, 0, 2, 4, 0, 9],
    [0, 0, 9, 7, 6, 4, 0, 0, 0],

    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 4, 9, 0, 0, 0],
    [0, 0, 0, 0, 5, 6, 0, 9, 0],

    [0, 5, 8, 4, 0, 0, 9, 1, 0],
    [0, 0, 2, 0, 1, 0, 6, 8, 0],
    [9, 0, 7, 6, 8, 0, 2, 5, 4]
]


class Su:
    def __init__(self, s):
        self.s = s
        self.prnt()
        self.solve()
        self.prnt()

    def prnt(self):
        for i in range(1,10):
            for j in range(1,10):
                print(self.s[i - 1][j - 1], end=" ")

                if j % 3 == 0 and not j == (0 or 9):
                    print("|", end=" ")
                
            print(end="\n")

            if i % 3 == 0 and not i == 9:
                print("----------------------")
        
        print("")

    def solve(self):
        Found, row, column = self.find()

        if not Found:
            return True

        else:
            for num in range(1, 10):
                if self.check(num, row, column):
                    self.s[row][column] = num

                    if self.solve():
                        return True
                    else:
                        self.s[row][column] = 0

        return False

    def find(self):
        for i in range(len(self.s)):
            for j in range(len(self.s)):
                if self.s[i][j] == 0:
                    return True, i, j
                
        return False, 0, 0

    def check(self, num, row, column):
        #Checking row
        for i in self.s[row]:
            if num == i:

                return False

        #Checking column 
        for i in range(len(self.s)):
            if self.s[i][column] == num:

                return False

        #Checking box
        for i in range((row//3) * 3, (row//3) * 3 + 3):
            for j in range((column//3) * 3, (column//3) * 3 + 3):
                if self.s[i][j] == num:

                    return False

        return True
      
 
s = Su(a)


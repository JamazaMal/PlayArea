import csv

def readboard():
    c = 0
    res = []
    with open("096.txt", 'r') as myFile:
        for i in csv.reader(myFile, delimiter=','):
            if c > 0:
                res.append([int(j) for j in i[0]])
            c += 1
            if c > 9:
                c = 0
                yield res
                res = []


def box(row, column):
    br = row // 3
    bc = column // 3
    return br + (3 * bc)


class Block:
    column = 0
    row = 0
    box = 0  # Small 3X3 area
    possible = []
    value = 0

    def __init__(self):
        self.possible = [1,2,3,4,5,6,7,8,9]


class Board:
    blocks = []

    def __init__(self):
        for i in range(81):
            self.blocks.append(Block())
            self.blocks[i].column = i % 9
            self.blocks[i].row = i // 9
            self.blocks[i].box = box(self.blocks[i].row, self.blocks[i].column)
            self.blocks[i].value = 0
            self.blocks[i].possible = [1,2,3,4,5,6,7,8,9]

    def __eq__(self,other):
        return self.row == other.row and self.column == other.column

    def __ne__(self,other):
        return not self.__eq__(other)

    def reset(self):
        self.blocks = []
        self.__init__()

    def row(self, row):
        for block in self.blocks:
            if block.row == row:
                yield block

    def column(self, column):
        for block in self.blocks:
            if block.column == column:
                yield block

    def box(self, box):
        for block in self.blocks:
            if block.box == box:
                yield block

    def makemove(self, row, column, value):
        for blk in self.row(row):
            if value in blk.possible:
                blk.possible.remove(value)

        for blk in self.column(column):
            if value in blk.possible:
                blk.possible.remove(value)

        for blk in self.box(box(row, column)):
            if value in blk.possible:
                blk.possible.remove(value)

        self.block(row, column).value = value
        self.block(row, column).possible = []

    def block(self, row, column):
        for block in self.blocks:
            if block.row == row and block.column == column:
                return block

    def oneoption(self):
        for block in self.blocks:
            if len(block.possible) == 1:
                return block
        return False

    def stripone(self):
        blk = self.oneoption()
        if not blk:
            return False
        self.makemove(blk.row, blk.column, blk.possible[0])
        return True

    def striponly(self):
        for blk in self.blocks:
            for value in blk.possible:
                found = False
                # --- Rows
                for bk in self.row(blk.row):
                    if bk != self:
                        if value == bk.value:
                            found = True
                            break
                if not found:
                    self.makemove(blk.row, blk.column, value)
                    return True
                # --- Column
                for bk in self.column(blk.column):
                    if bk != self:
                        if value == bk.value:
                            found = True
                            break
                if not found:
                    self.makemove(blk.row, blk.column, value)
                    return True
                # --- Box
                for bk in self.box(box(blk.row, blk.column)):
                    if bk != self:
                        if value == bk.value:
                            found = True
                            break
                if not found:
                    self.makemove(blk.row, blk.column, value)
                    return True
        return False

def showme(board):
    for r in range(9):
        print([blk.value for blk in board.row(r)])

    for blk in board.blocks:
        print(blk.row, blk.column, blk.value, blk.possible)


def main():
    res = 0
    brd = Board()
    for i, b in enumerate(readboard()):
        for row in range(9):
            for column in range(9):
                if b[row][column] != 0:
                    brd.makemove(row, column, b[row][column])

        while brd.stripone() or brd.striponly():
            pass

        if i == 1:
            print(" {} ------------------".format(i+1))
            showme(brd)

        res += (brd.block(0, 0).value * 100) + (brd.block(0, 1).value * 10) + brd.block(0, 2).value
        brd.reset()
    print(res)



from testBoard import *

class Sudoku:
  def __init__(self, boardText=None):
    self.board = []
    if boardText is not None:
      self.parse(boardText)
    else:
      self.parse(".........\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........")

  def __repr__(self):
    out_string = ""
    for row in self.board:
      for cell in row:
        if cell is None:
          out_string += "."
        if cell in {1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '!'}:
          out_string += str(cell)
      out_string += '\n'
          
    return out_string

  def parse(self, board):
    def process_char(c):
      try:
        if int(c) in {1,2,3,4,5,6,7,8,9}:
          return int(c)
        else:
          return None
      except:
        return None

    board = board.split('\n')

    self.board = []
    for line in board:
      self.board.append(([process_char(c) for c in line]))
  
  def box(self,i,j):
    box = []
    rows = [j - (j % 3), j + 1 - (j % 3), j + 2 - (j % 3)]
    columns = [i - (i % 3), i + 1 - (i % 3), i + 2 - (i % 3)]
    for x in rows:
      for y in columns:
        box.append(self.board[x][y])
    return box
  
  def poss(self,i,j):
    possVals = {1,2,3,4,5,6,7,8,9}
    
    for item in self.board[j]:
      if item in possVals:
        possVals.remove(item)
    
    for row in self.board:
      if row[i] in possVals:
        possVals.remove(row[i])

    for item in self.box(i, j):
      if item in possVals:
        possVals.remove(item)

    return possVals

  def logicFill(self):
      change = 1
      while change != 0:
        change = 0
        for i in range(9):
          for j in range(9):
            if self.board[j][i] not in {1,2,3,4,5,6,7,8,9}:
              L = self.poss(i,j)
              if len(L) == 1:
                self.board[j][i] = L.pop()
                change +=1
              elif len(L) == 2:
                self.board[j][i] = '+'
              elif len(L) == 0:
                self.board[j][i] = '!'




  def checkSolve(self):
    for j in range(9):
      for i in self.board[j]:
        if i not in {1,2,3,4,5,6,7,8,9}:
          return False
    return True

  def findPlus(self):
    for i in range(9):
      for j in range(9):
        if self.board[i][j] == '+':
          return [i, j], self.poss(j,i)
    return False

  def findError(self):
    for j in range(9):
      for i in range(len(self.board[j])):
        if self.board[j][i] == '!':
          return True
    return False
  
  def actSolve(self):
    backup = self.board
    testBoard = self
    print("self", self)
    testBoard.logicFill()
    if testBoard.checkSolve():
      return
    elif testBoard.findError():
      print("found error")
      return 
    else:
      self.board = backup
      spot, poss = self.findPlus()
      for i in poss:
        testBoard.board = backup
        print("loop", testBoard)
        print("guess", spot, i)
        testBoard.board[spot[0]][spot[1]] = i
        print("testboard pre-solve", testBoard)
        extra = testBoard
        extra.actSolve()
        print("testboard post-solve", extra)
        if not extra.findError():
          self.board = extra.board
          return
          
        
      
      
      
    

def main():
  testBoard1 = Sudoku(testBoardMedium)
  testBoard1.logicFill()
  print(testBoard1)
  testBoard2 = Sudoku(testBoardMedium)
  testBoard2.actSolve()
  print("final", testBoard2)
  print(testBoard2.checkSolve())
  print(testBoard2.findPlus())

if __name__ == '__main__':
  main()
from hashlib import new
import re
from turtle import st
col_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def getRows(position):
  #gets a position array and returns it as an array of rows
  rows = [[],[],[],[],[],[],[],[]]
  for i in range(8):
    rows[i] = position[i*8:(i+1)*8]
  return rows

def showBoard(position):
  rows = getRows(position)
  i=8
  for row in rows:
    prettyrow = f'{i}| '+' | '.join(row)+' |'
    print(prettyrow)
    print('  --------------------------------')
    i-=1
  print('   '+'   '.join(col_names))
  print(' ')

def FEN2Board(position):
  rows = position.split('/')
  board = []
  for row in rows:
    #find all empty squares in the row
    num_empty_squares = re.findall('\d',row)
    #signal empty squares by \s (in FEN numbers give total of consecutive empty squares) 
    newrow=row
    for empt in num_empty_squares:
      newrow = re.sub(r'\d', ' '*int(empt),newrow, 1)
    #board is an array of all squares
    board = board + re.findall(r'.',newrow)

  return board   
  

def Board2FEN(position):
  rows = getRows(position)
  fen = ''
  introws = ['','','','','','','','']
  for i,row in enumerate(rows):
    introws[i] = ''.join(row)
  fen = '/'.join(introws)
  return fen 
  
def make_move(board, move):
  new_board = board
  #move in format e2-e4. 0-0=e1-g1

  alg_squares = move.split('-')
  start_col = col_names.index(alg_squares[0][0])
  start_row = 8-int(alg_squares[0][1])
  target_col = col_names.index(alg_squares[1][0]) 
  target_row = 8 -int(alg_squares[1][1])
  #check move validity
  piece = board[8*start_row + start_col]
  #delete origin square
  new_board[8*start_row+start_col] = ' '
  #write target square
  new_board[8*target_row + target_col] = piece
  return new_board
if __name__=='__main__':
  #different tests
  startingfen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
  startBoard = FEN2Board(startingfen)
  showBoard(startBoard)
  #first couple moves of italian game
  newBoard = make_move(startBoard,'e2-e4')
  
  #print(startBoard, len(startBoard))
  showBoard(newBoard)
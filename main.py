from typing import List

def draw_board(grid: List):
   print(" _ _ _ ")
   for i in range(len(grid)):
       for j in range(len(grid[i])):
           if grid[i][j] == "":
               print("|_", end="")    
           else:
               print("|" + grid[i][j], end="")
       print("|")

def check_board(grid: List):
   # Check horizontals
   for i in range(len(grid)):
       count_1 = grid[i].count('X')
       count_2 = grid[i].count('O')
       if count_1 == 3:
           return 1
       elif count_2 == 3:
           return 2

   # Check verticals
   for i in range(len(grid)):
       if grid[0][i] == 'X' and grid[1][i] == 'X' and grid[2][i] == 'X':
           return 1
       if grid[0][i] == 'O' and grid[1][i] == 'O' and grid[2][i] == 'O':
           return 2

   # Check diagonals
   i, y = 0, 0
   if grid[i][y] == grid[i + 1][y + 1] == grid[i + 2][y + 2] == 'X':
       return 1
   if grid[i][y + 2] == grid[i + 1][y + 1] == grid[i + 2][y] == 'X':
       return 1
   if grid[i][y] == grid[i + 1][y + 1] == grid[i + 2][y + 2] == 'O':
       return 2
   if grid[i][y + 2] == grid[i + 1][y + 1] == grid[i + 2][y] == 'O':
       return 2
   
   return 0

def getInput(grid: List):
   valid_inputs = ['1', '2', '3']
   row, col = '', ''

   valid = False
   while not valid:
       turn = input("Enter row and column separated by a whitespace: ")
       if len(turn) < 3:
           continue
       row = turn.strip().split(' ')[0]
       col = turn.strip().split(' ')[1]
       if row not in valid_inputs or col not in valid_inputs:
           continue
       else:
           if grid[int(row) - 1][int(col) - 1] != "":
               print("Place is taken already")
           else:
               valid = True

   return [row, col]

def main():
   grid = [
       ['', '', ''],
       ['', '', ''],
       ['', '', '']
   ]
   
   player = 1
   done = False
   player_names = ['X', 'O']

   while not done:
       draw_board(grid)
       winner = check_board(grid)
       if winner != 0:
           print(f"Player {winner} wins")
           done = True
           continue

       print("Current player:", player)
       row, col = getInput(grid)

       grid[int(row) - 1][int(col) - 1] = player_names[player-1]
       free = 9
       for i in range(len(grid)):
           for j in range(len(grid[i])):
               if grid[i][j] != "":
                   free -= 1

       if free == 0:
           print("Game is tied.")
           done = True

       if player == 1:
           player = 2
       else:
           player = 1

main()

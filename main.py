from tkinter import *

player_turn = 1;
player1_points = 0
player2_points = 0
marked_lines = []

    # The following will help track which lines belong to a box and determining if a box has been completed.
box0 = [[1,0],[2,1],[1,2],[0,1]]
box1 = [[3,0],[4,1],[3,2],[2,1]]
box2 = [[5,0],[6,1],[5,2],[4,1]]
box3 = [[7,0],[8,1],[7,2],[6,1]]
box4 = [[9,0],[10,1],[9,2],[8,1]]
box5 = [[1,2],[2,3],[1,4],[0,3]]
box6 = [[3,2],[4,3],[3,4],[2,3]]
box7 = [[5,2],[6,3],[5,4],[4,3]]
box8 = [[7,2],[8,3],[7,4],[6,3]]
box9 = [[9,2],[10,3],[9,4],[8,3]]
box10 = [[1,4],[2,5],[1,6],[0,5]]
box11 = [[3,4],[4,5],[3,6],[2,5]]
box12 = [[5,4],[6,5],[5,6],[4,5]]
box13 = [[7,4],[8,5],[7,6],[6,5]]
box14 = [[9,4],[10,5],[9,6],[8,5]]
box15 = [[1,6],[2,7],[1,8],[0,7]]
box16 = [[3,6],[4,7],[3,8],[2,7]]
box17 = [[5,6],[6,7],[5,8],[4,7]]
box18 = [[7,6],[8,7],[7,8],[6,7]]
box19 = [[9,6],[10,7],[9,8],[8,7]]
box20 = [[1,8],[2,9],[1,10],[0,9]]
box21 = [[3,8],[4,9],[3,10],[2,9]]
box22 = [[5,8],[6,9],[5,10],[4,9]]
box23 = [[7,8],[8,9],[7,10],[6,9]]
box24 = [[9,8],[10,9],[9,10],[8,9]]
boxes = [box0, box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13, box14, box15, box16, box17, box18, box19, box20, box21, box22, box23, box24]

size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
distance_between_dots = size_of_board/number_of_dots
dot_width = distance_between_dots/5
edge_width = distance_between_dots/10

player1_color = '#3D348B'
player1_color_light = '#7678ED'
player2_color = '#F18701'
player2_color_light = '#F7B801'
Green_color = '#4D8B31'

window = Tk()
window.title('Dots and Lines Game')
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack()
window.mainloop(30)

def draw_board(c):
  for n in range(50, 650, 100):
    canvas.create_line(50, n, 550, n, fill='grey', dash = (2,2)) #create 6 rows
    canvas.create_line(n, 50, n,    550, fill='grey', dash = (2,2)) #create 6 columns
  for i in range(6): #draw dots
    for j in range(6):
      start_x = i * 100 + 50
      end_x = j * 100 + 50
      canvas.create_oval(start_x - dot_width/2, end_x - dot_width/2, start_x + dot_width/2, end_x + dot_width/2, fill='grey', outline='grey')

def is_even(n): 
  return n % 2 == 0

def get_logical_position(x, y):
  xlog = (x - 25) // 50
  ylog = (y - 25) // 50
  pos = []
  direction = ''
  if is_even(xlog) == False and is_even (ylog) == True:
    direction = 'row'
    pos = [xlog, ylog]
  elif is_even(xlog) == True and is_even (ylog) == False:
    direction = 'col'
    pos = [xlog, ylog]
  return pos, direction

def mark_line(pos, direction):
  global player_turn
  x1 = 50 * pos[0] + 50
  y1 = 50 * pos[1] + 50
  if direction == 'row':
    x1 = x1 - 50
    x2 = 50 * pos[0] + 100
    y2 = y1
  elif direction == 'col':
    y1 = y1 - 50
    x2 = x1
    y2 = 50 * pos[1] + 100
  if player_turn == 1:
    canvas.create_line(x1, y1, x2, y2, width = 5, fill = player1_color)
    player_turn = 2
    return player_turn
  elif player_turn == 2:
    canvas.create_line(x1, y1, x2, y2, width = 5, fill = player2_color)
    player_turn = 1
    return player_turn

def handle_click(e):
  pos, direction = get_logical_position(e.x, e.y)
  if direction == '':
    return
  mark_line(pos, direction)

draw_board(canvas)
window.bind('<Button-1>', handle_click)


from tkinter import *

size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
distance_between_dots = size_of_board/number_of_dots
dot_width = distance_between_dots/5
edge_width = distance_between_dots/10

dot_color = '#15161E'
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

for n in range(50, 650, 100):
  canvas.create_line(50, n, 550, n, fill='grey', dash = (2,2)) #create 6 rows

for n in range(50, 650, 100):
  canvas.create_line(n, 50, n, 550, fill='grey', dash = (2,2)) #create 6 columns

for i in range(6):
  for j in range(6):
    start_x = i * 100 + 50
    end_x = j * 100 + 50
    canvas.create_oval(start_x - dot_width/2, end_x - dot_width/2, start_x + dot_width/2, end_x + dot_width/2, fill='grey', outline='grey')
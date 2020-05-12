class TicTacToe:
  def __init__(self):
    # board, current_turn,
    self.current_turn = "O"
    self.board = [".", ".", ".", ".", ".", ".", ".", ".", "."]

  def check_winner(self):
    check = self.current_turn
    # -, |
    for i in range(3):
      if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check \
          or self.get(0, i) == self.get(1, i) == self.get(2, i) == check:
        return check
    # \/
    if (self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check) \
        or (self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check):
      return check
    if not "." in self.board:
      return "d"

  def get(self, row, col):
    return self.board[(row * 3) + col]

  def set(self, row, col):
    if self.get(row, col) == ".":
      self.current_turn = "X" if self.current_turn == "O" else "O"
      self.board[(row * 3) + col] = self.current_turn

  def __str__(self):
    s = ""
    for i, v in enumerate(self.board):
      s += v
      if i % 3 == 2:
        s += "\n"
    return s


import tkinter
from tkinter import messagebox
import math


class GameManager_GUI:
  def __init__(self):
    CANVAS_SIZE = 300
    self.TILE_SIZE = CANVAS_SIZE / 3

    self.root = tkinter.Tk()
    self.root.title("틱택토")
    self.root.geometry(str(CANVAS_SIZE) + "x" + str(CANVAS_SIZE))
    self.root.resizable(width=False, height=False)
    self.canvas = tkinter.Canvas(self.root, bg="white", width=CANVAS_SIZE, height=CANVAS_SIZE)
    self.canvas.pack()
    self.images = dict()
    self.images["O"] = tkinter.PhotoImage(file="o.gif")
    self.images["X"] = tkinter.PhotoImage(file="x.gif")

    self.ttt = TicTacToe()
    self.canvas.bind("<Button-1>", self.click_handler)

  def click_handler(self, event):
    self.ttt.set(math.floor(event.y / self.TILE_SIZE), math.floor(event.x / self.TILE_SIZE))
    print(math.floor(event.y / self.TILE_SIZE), math.floor(event.x / self.TILE_SIZE))
    self.draw_board()
    # check_winner()
    self.winner = self.ttt.check_winner()
    if self.winner == "O":
      #  O:
      messagebox.showinfo("Game Over", "O가 이겼습니다.")
      self.root.quit()
    elif self.winner == "X":
      #  X:
      messagebox.showinfo("Game Over", "X가 이겼습니다.")
      self.root.quit()
    elif self.winner == "d":
      #  d:
      messagebox.showinfo("Game Over", "무승부입니다.")
      self.root.quit()

  def draw_board(self):
    # clear
    self.canvas.delete("all")

    SIZE = 100
    x = 0
    y = 0
    for i, v in enumerate(self.ttt.board):
      if v == ".":
        pass
      elif v == "O":
        self.canvas.create_image(x, y, anchor="nw", image=self.images["O"])
      elif v == "X":
        self.canvas.create_image(x, y, anchor="nw", image=self.images["X"])
      x += SIZE
      if i % 3 == 2:
        x = 0
        y += SIZE

  def play(self):
    self.root.mainloop()


if __name__ == '__main__':
  # gm = GameManager()
  gm = GameManager_GUI()
  gm.play()

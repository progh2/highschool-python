class TicTacToe:
    def __init__(self, start_turn):
        self.winner = '.'
        self.board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.game_end = False
        self.current_turn = start_turn

    def add(self, x, y, c):
        if self.game_end:
            return
        if self.current_turn != c:
            return
        if self.board[(x * 3) + y] != '.':
            return

        self.board[(x * 3) + y] = c
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'

        self.winner = self.check_winner()
        if self.winner == 'O' or self.winner == 'X':
            self.game_end = True
        elif self.winner == 'd':
            self.game_end = True
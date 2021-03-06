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

    def check_winner(self):
        for check in ['O', 'X']:
            for i in range(0, 3):
                if self.board[i * 3 + 0] == check and \
                   self.board[i * 3 + 1] == check and \
                   self.board[i * 3 + 2] == check:
                    return check

                if self.board[0 * 3 + i] == check and \
                   self.board[1 * 3 + i] == check and \
                   self.board[2 * 3 + i] == check:
                    return check

                if (self.board[0] == check and self.board[4] == check and self.board[8] == check) or \
                   (self.board[2] == check and self.board[4] == check and self.board[6] == check):
                    return check

        has_empty_cell = False
        for idx, val in enumerate(self.board):
            if val == '.':
                has_empty_cell = True
                break

        return '.' if has_empty_cell else 'd'

    def get_winner(self):
        return self.winner

    def get_current_turn(self):
        return self.current_turn

    def get(self, x, y):
        return self.board[(x * 3) + y]

    def show_board(self):
        for i in range(0, 9):
            print(self.board[i], end='')
            if (i + 1) % 3 == 0:
                print('')

import random

class Ludo:
    def __init__(self):
        self.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        self.board = {
            "red": [],
            "green": [],
            "blue": [],
            "yellow": []
        }
        self.current_player_index = 0
        self.finished_pieces = {player: 0 for player in self.players}
        self.dice = None

    def roll_dice(self):
        return random.randint(1, 6)

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def move_piece(self, player, piece, steps):
        if piece in self.board[player]:
            index = self.board[player].index(piece)
            new_index = index + steps
            if new_index >= len(self.board[player]):
                self.finished_pieces[player] += 1
                self.board[player].remove(piece)
            else:
                self.board[player][index], self.board[player][new_index] = self.board[player][new_index], piece

    def is_winner(self):
        return any(count >= 4 for count in self.finished_pieces.values())

    def play(self):
        while not self.is_winner():
            player = self.players[self.current_player_index]
            input(f"{player}'s turn, press enter to roll the dice...")
            self.dice = self.roll_dice()
            print(f"{player} rolled: {self.dice}")

            # Simulate moving a piece (just for demonstration)
            piece_to_move = random.choice(self.board[player])
            self.move_piece(player, piece_to_move, self.dice)

            print("Board Status:")
            print(self.board)
            print("Finished Pieces:")
            print(self.finished_pieces)

            self.switch_player()

        winner = [player for player, count in self.finished_pieces.items() if count >= 4][0]
        print(f"{winner} wins!")

if __name__ == "__main__":
    ludo_game = Ludo()
    ludo_game.play()

import numpy.matlib

SYMBOLS = ["X","O"]
ALLOWED_COORDINATE_CHARS='012'

class Game:
    field=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    players = []
    first_players_turn = True
    winner = None
    
    def __init__(self):
        self.players.append(input("Enter player 1 name: "))
        self.players.append(input("Enter player 2 name: "))
        print(f"{self.players[0]} plays with {SYMBOLS[0]}.")
        print(f"{self.players[1]} plays with {SYMBOLS[1]}.")
        self.print_field()

    def print_field(self):
        for i in range(len(self.field)): #row by row
            for j in range(len(self.field[i])): # column by column
                cell_string = " {} ".format(self.field[i][j])
                last_row_cell = not j < (len(self.field[i]) - 1)
                print(cell_string,end=('\n' if last_row_cell  else '|'))
            if i < (len(self.field) - 1): #number of rows:
                print("-----------")
        
    
    def check_winner(self):
        # horizontal checks
        if self.field[0][0] == self.field[1][0] == self.field[2][0] and self.field[2][0] != ' ':
            return self.field[2][0]
        elif self.field[0][1] == self.field[1][1] == self.field[2][1] and self.field[2][1] != ' ':
            return self.field[2][1]
        elif self.field[0][2] == self.field[1][2] == self.field[2][2] and self.field[2][2] != ' ':
            return self.field[2][2]

        # vertical checks
        elif self.field[0][0] == self.field[0][1] == self.field[0][2] and self.field[0][2] != ' ':
            return self.field[0][2]
        elif self.field[1][0] == self.field[1][1] == self.field[1][2] and self.field[1][2] != ' ':
            return self.field[1][2]
        elif self.field[2][0] == self.field[2][1] == self.field[2][2] and self.field[2][2] != ' ':
            return self.field[2][2]

        # diagonal checks    
        elif (self.field[0][0] == self.field[1][1] == self.field[2][2] or self.field[2][0] == self.field[1][1] == self.field[0][2]) and self.field[1][1] != ' ':
            return self.field[1][1]

    
    def prompt_input(self):
        player_index = 0 if self.first_players_turn else 1
        coordinate = input(f"{self.players[player_index]}'s turn. Enter coordinate where to place {SYMBOLS[player_index]}: ")
        if len(coordinate)!=2 or coordinate[0] not in ALLOWED_COORDINATE_CHARS or coordinate[1] not in ALLOWED_COORDINATE_CHARS:
            print("Coordinate must be in 'XY' format where X and Y are between 0 and 2")
            return

        y=int(coordinate[0])
        x=int(coordinate[1])
        if self.field[x][y] == ' ':
            self.field[x][y] = SYMBOLS[player_index]
        else:
            print('Field occupied. Select another one.')
            return

        self.print_field()

        winner = self.check_winner()
        if winner is not None:
            self.announce_winner(winner)
        else:
            self.first_players_turn = not self.first_players_turn

    def announce_winner(self, winner):
        winner = self.players[0] if winner == SYMBOLS[0] else self.players[1]
        self.winner=winner
        if winner in self.players:
            print(f"{winner} wins!")
            other_player = self.players.pop()
            print(f"{other_player if other_player != winner else self.players.pop()} is a sad loser!")


g = Game()
while g.winner is None:
    g.prompt_input()
#! /usr/bin/env python3

class Player:
    def __init__(self, name, dice, num_dice):
        self.name = name
        self.dice = dice
        self.num_dice = num_dice
        
    def roll_dice(self):
        self.dice = []
        for x in range(0,self.num_dice):
            self.dice.append(x+1)
            

            


class Game:
    def __init__(self, players, num_dice):
        self.players = []
        self.num_dice = num_dice
        self.round_num = 0
        self.turn_num = 0
        self.dice = []
        for x in range(0, self.num_dice):
            self.dice.append(x)
        for name in players:
            self.players.append(Player(name, self.dice, self.num_dice))
        self.current_bet = []
        
    def start_round(self):
        self.round_num += 1
        for player in self.players:
            player.roll_dice();

class Engine:
    def __init__(self, random_number_generator):
        self._games = {}
        self._next_id = 1
        self._rng = random_number_generator
        

    def create_game(self, players, num_dice):
        id = self._next_id
        self._next_id += 1

        
        self._games[id] = Game(players, num_dice)
        return self._games[id]
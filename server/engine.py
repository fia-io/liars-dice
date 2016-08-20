#! /usr/bin/env python3

class Player:
    def __init__(self, name, dice):
        self.name = name
        self.dice = dice


class Game:
    def __init__(self, players, num_dice):
        self.players = []
        for name in players:
            self.players.append(Player(name, []))


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
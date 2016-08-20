#! /usr/bin/env python3

#Player persists through at least one game
#contains info about name, number of dice, current dice values
#should it have bid info??
class Player:
    def __init__(self, name, num_dice):
        self.name = name
        self.num_dice = num_dice
        self.dice = []
        
    def roll_dice(self):
        self.dice = []
        for x in range(0,self.num_dice):
            self.dice.append(x+1)
            
#Round will receive info about the players
#One round consists of dice roll, successive bids, turn_num
#validate allowable bid
#resolves challenge
#tells losing player to adjust dice_num
#checks for player_out
#checks for player_win
#ends at challenge

class Round:
    def __init__(self, players, round_num):
        self.players = players
    
        
    #everybody rolls dice
    def start_round(self):
        self.bids = []
        for player in self.players:
            player.roll_dice()
        self.current_player = self.players[0]
            
    def take_bid(self, player, bid):
        if player != self.current_player:
            return False
        else:
            if (validate_bid(bid)):
                current_bid = bid
                self.bids.append(bid)
                self.current_player = self.findNextPlayer(self.current_player)
                self.turn_num += 1
                return True
    
    #check new bid against current bid
    #return false if bad bid
    #maybe bid contains info about which player did it?
    #if good bid, increment turn_num, return true
    def validate_bid(self, bid):
        pass
    
    #check current bid against all dice
    #if bid exceeds total, decrement bidder's dice_num
    #end round, check for player-out, player-win, begin next
    #return true
    #else decrement challenger's dice_num
    #end round, check for player-out, player-win, begin next
    #return false
    def win_challenge(self, player):
        pass
        
            

#Game contains info about players, starting dice number
#starts with status of not_playing
#will need to add info about starting
#current round and current turn within round (?)
#also a complete list of the current dice values (?)
class Game:
    def __init__(self, players, start_dice):
        self.players = []
        self.start_dice = start_dice
        self.round_num = 0
        self.turn_num = 0
        self.dice = []
        self.status = 'not_started'
        
        for name in players:
            self.players.append(Player(name, self.start_dice))
        self.current_bid = []
        
    #okay, this is a bit redundant right now
    def start_round(self):
        self.current_round = Round(self.players, self.round_num)
        self.current_round.start_round()
        
    def current_player(self):
        return self.current_round.current_player.name
        
    def get_bids(self):
        return self.current_round.bids
        
    def take_bid(self, player, bid):
        return self.current_round.take_bid(player, bid)


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
        
    def game_status(self, game_id):
        return [game_id, self._games[game_id].status, self._games[game_id].round_num] 
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
            self.dice.append(2)
            
    def set_dice(self, dice):
        self.num_dice = len(dice)
        self.dice = dice
        
#Round will receive info about the players
#One round consists of dice roll, successive bids, turn_num
#validate allowable bid
#resolves challenge
#tells losing player to adjust dice_num
#checks for player_out
#checks for player_win
#ends at challenge

class Round:
    def __init__(self, players, round_num=None):
        self.players = players
        self.start_round()
    
    def get_current_player(self):
        return self.current_player.name
    
    #everybody rolls dice
    def start_round(self):
        self.turn_num = 0
        self.current_bid = ['default',0,1]
        self.bids = []
        self.status = 'current'
        self.bids.append(self.current_bid)
        for player in self.players:
            player.roll_dice()
        self.current_player = self.players[0]
            
    def take_bid(self, bid):
        if bid[0] != self.current_player.name:
            return False
        else:
            if (self.validate_bid(bid)):
                self.current_bid = bid
                self.bids.append(bid)
                self.current_player = self.findNextPlayer(self.current_player.name)
                self.turn_num += 1
                return True
            else: 
                return False
    
    #find the next player who's still in the game
    def findNextPlayer(self, player_name):
        x = 0
        while self.players[x].name != player_name:
            x += 1
        x += 1
        if x >= len(self.players):
            x = 0
        while self.players[x].num_dice == 0 and self.players[x].name != player_name:
            x += 1
            if x >= len(self.players):
                x = 0
        return self.players[x]    
        
            
        
        
    #check new bid against current bid
    #return false if bad bid
    #maybe bid contains info about which player did it?
    #if good bid, increment turn_num, return true
    #bid format is [player name, number of dice, face number]
    def validate_bid(self, bid):
        if bid[2] > 6 or bid[2] < 1 or bid[1] < 1:
            return False
        if bid[1] < self.current_bid[1]:
            return False
        if bid[1] == self.current_bid[1]:
            if bid[2] <= self.current_bid[2]:
                return False
            else:
                return True
        else:
            return True
            

    
    #check current bid against all dice
    #if bid exceeds total, decrement bidder's dice_num
    #end round, check for player-out, player-win, begin next
    #return true
    #else decrement challenger's dice_num
    #end round, check for player-out, player-win, begin next
    #return false
    def process_challenge(self, player_name):
        if self.current_player.name == player_name:
            bidder, num_dice, die = self.current_bid
            num = 0
            play = 0
            while play < len(self.players) and num < num_dice:
                for x in range(0, self.players[play].num_dice):
                    if self.players[play].dice[x] == die:
                        num += 1
                play += 1
            if num >= num_dice:
                self.punish(player_name)
            else:
                self.punish(bidder)
            self.status='ended'
        return self.status
        
    def punish(self, player_name):
        x = 0
        while (self.players[x].name != player_name):
            x += 1
        self.players[x].num_dice -= 1
        self.players[x].dice.pop()

        
    def set_dice(self, player, dice):
        x = 0
        while (self.players[x].name != player):
            x += 1
        self.players[x].set_dice(dice)

    def round_status(self):
        result = []
        for x in self.players:
            result.append(self.current_player.name)
            result.append(x.name)
            result.append(x.dice)
        return result

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
        self.status = 'playing'
        for name in players:
            self.players.append(Player(name, self.start_dice))
        self.current_bid = []
        self.start_round()
        
    #okay, this is a bit redundant right now
    def start_round(self):
        self.current_round = Round(self.players, self.round_num)
 #       self.current_round.start_round()
        
    def current_player(self):
        return self.current_round.current_player.name
        
    def get_player_dice(self, player_name):
        x = 0
        while self.players[x].name != player_name:
            x += 1
        return self.players[x].dice
        
    def get_bids(self):
        return self.current_round.bids
        
    def take_bid(self, bid):
        return self.current_round.take_bid(bid)
        
    def challenge(self, player_name):
        if self.current_round.process_challenge(player_name) == 'ended':
            if self.check_for_win():
                self.status = 'ended'
            else:
                self.round_num += 1
                self.start_round()
        
    def check_for_win(self):
        active = 0
        for y in self.players:
            if y.num_dice > 0:
                active += 1
        if active > 1:
            return False
        else:
            return True
        
    def game_status(self, game_id, player_name):
        return [game_id, self.status, self.round_num, self.current_player() == player_name, self.get_player_dice(player_name), self.current_round.bids]
        
    def poll_dice(self):
        d = []
        for x in self.players:
            for y in x.dice:
                d.append(y)
        return d

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
        
    def game_status(self, game_id, player_name):
        return self._games[game_id].game_status(game_id, player_name)

    def challenge(self, game_id, round_num, player_name):
        if self._games[game_id].round_num == round_num:
            self._games[game_id].challenge(player_name)
        return self.game_status(game_id, player_name)

    def get_bids(self, game_id):
        return self._games[game_id].get_bids()
        
    def bid(self, game_id, round_num, bid):
        if self._games[game_id].round_num != round_num:
            return False
        else:
            return self._games[game_id].take_bid(bid)
            
    def set_dice(self, game_id, round_num, player, dice):
        if self._games[game_id].round_num == round_num:
            self._games[game_id].current_round.set_dice(player, dice)
        
            
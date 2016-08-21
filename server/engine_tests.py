#! /usr/bin/env python3

import unittest
import engine

class TestRound(unittest.TestCase):
    def test_create_round(self):
        round = engine.Round([engine.Player('me', 2), engine.Player('you', 1)])
        self.assertEqual('me', round.get_current_player())

    def test_one_bid(self):
        round = engine.Round([engine.Player('me', 2), engine.Player('you', 1)])
        self.assertEqual('me', round.get_current_player())
        round.take_bid(('me', 2, 1))
        self.assertEqual('you', round.get_current_player())

    def test_cannot_challenge_before_bids(self):
        round = engine.Round([engine.Player('me', 2), engine.Player('you', 1)])
        self.assertEqual('me', round.get_current_player())
        round.process_challenge('me')
        self.assertEqual('me', round.get_current_player())

    def test_cannot_challenge_out_of_turn(self):
        round = engine.Round([engine.Player('me', 2), engine.Player('you', 1)])
        self.assertEqual('me', round.get_current_player())
        round.take_bid(('me', 2, 1))
        self.assertEqual('you', round.get_current_player())
        round.process_challenge('me')
        self.assertEqual('you', round.get_current_player())

    def test_challenge_correct_bid(self):
        me = engine.Player('me', 2)
        you = engine.Player('you', 1)
        round = engine.Round([me, you])
        
        me.set_dice([1, 1])
        you.set_dice([1])
        
        self.assertEqual('me', round.get_current_player())
        round.take_bid(('me', 3, 1))
        self.assertEqual('you', round.get_current_player())
        round.process_challenge('you')
        
        self.assertEqual(2, me.num_dice)
        self.assertEqual(0, you.num_dice)

    def test_challenge_incorrect_bid(self):
        me = engine.Player('me', 2)
        you = engine.Player('you', 1)
        round = engine.Round([me, you])
        
        me.set_dice([1, 1])
        you.set_dice([2])
        
        self.assertEqual('me', round.get_current_player())
        round.take_bid(('me', 3, 1))
        self.assertEqual('you', round.get_current_player())
        round.process_challenge('you')
        
        self.assertEqual(1, me.num_dice)
        self.assertEqual(1, you.num_dice)


class TestEngine(unittest.TestCase):

    def test_create_engine(self):
        rng = (x for x in [1, 1, 1, 2, 2, 2])
        e = engine.Engine(rng)
        game = e.create_game(['me', 'you'], 3)

        self.assertEqual('me', game.players[0].name)
        self.assertEqual('you', game.players[1].name)
        self.assertEqual(3, game.start_dice)
        self.assertEqual(0, game.turn_num)
        self.assertEqual(0, game.round_num)
        
        game.start_round()
        
#        e.set_dice(1, 0, 'me', [1, 4, 4])
#        e.set_dice(1, 0, 'you', [2, 6, 6])
#        self.assertEqual([1, 4, 4, 2, 6, 6], game.poll_dice())
#        self.assertEqual([], game.current_bid)
        
        #currently don't have way to check whose turn it is
#        self.assertEqual([1, 'playing', 0, True, [1, 4, 4, 2, 1], [['default', 0, 1]]], e.game_status(1, 'me'))
        

        self.assertEqual(0, game.round_num)
        self.assertEqual('me', game.current_player())
        self.assertEqual(['default', 0, 1], e.get_bids(1)[0])
        
        self.assertEqual(True, e.bid(1, 0, ['me', 2, 4]))
        '''
        self.assertEqual(['default', 0, 1], game.get_bids()[0])
        self.assertEqual(True, game.take_bid(['me', 2, 4]))
        self.assertEqual(True, game.take_bid(['you', 2, 5]))
        e.challenge(1, 0, 'me')
        print(game.game_status(1, 'you'))
        self.assertEqual(True, game.take_bid(['me', 2, 4]))
        self.assertEqual(True, game.take_bid(['you', 2, 5]))
        e.challenge(1, 1, 'me')
        print(game.game_status(1, 'you'))
        self.assertEqual(True, game.take_bid(['me', 2, 4]))
        self.assertEqual(True, game.take_bid(['you', 2, 5]))
        e.challenge(1, 2, 'me')
        print(game.game_status(1, 'you'))
        '''

if __name__ == '__main__':
    unittest.main()
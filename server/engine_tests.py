#! /usr/bin/env python3

import unittest
import engine

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
        self.assertEqual([], game.current_bid)
        self.assertEqual(3, game.players[0].num_dice)
        
        #currently don't have way to check whose turn it is
        self.assertEqual([1, 'not_started', 0], e.game_status(1))
        

        self.assertEqual(0, game.round_num)
        self.assertEqual(3, game.players[0].dice[2])
        self.assertEqual('me', game.current_player())
        self.assertEqual([], game.get_bids())
        
        self.assertEqual(True, game.take_bid('me', [2, 4]))

if __name__ == '__main__':
    unittest.main()
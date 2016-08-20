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
        self.assertEqual(3, game.num_dice)
        self.assertEqual(0, game.turn_num)
        self.assertEqual(0, game.round_num)
        self.assertEqual(0, game.players[0].dice[0])
        self.assertEqual([], game.current_bet)
        self.assertEqual(3, game.players[0].num_dice)
        
        game.start_round()
        self.assertEqual(1, game.round_num)
        self.assertEqual(3, game.players[0].dice[2])

if __name__ == '__main__':
    unittest.main()
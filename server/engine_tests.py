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

if __name__ == '__main__':
    unittest.main()
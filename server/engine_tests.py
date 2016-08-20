#! /usr/bin/env python3

import unittest
import engine

class TestEngine(unittest.TestCase):

    def test_create_engine(self):
        e = engine.Engine()
        game = e.create_game(['me', 'you'], 3)

        self.assertEqual('me', game.players[0].name)
        self.assertEqual('you', game.players[1].name)

if __name__ == '__main__':
    unittest.main()
'''
Test modeul
'''
import unittest
import game


class GameTest(unittest.TestCase):
    '''
    Game Test for game unit test.
    '''

    def setUp(self):
        pass

    def test_random_pick(self):
        '''Test random pick a number in range [1, 3]'''
        assert all(game.random_pick() in range(1, 4) for i in range(20))

    def test_validate_user_choice(self):
        '''Test validate user choice is of '1', '2', '3' '''
        input_list = ['', 'a', 'ABC', '12', '0', '1', '2', '3']
        result_list = [False, False, False, False, False, True, True, True]

        assert all(game.validate_user_choice(input_list[i]) ==
                   result_list[i] for i in range(len(result_list)))

    def test_compare_choice(self):
        '''Test compare computer choice and user choice'''
        choice_list = [(game.ROCK, game.SCISSOR),
                       (game.ROCK, game.ROCK),
                       (game.ROCK, game.PAPER),
                       (game.SCISSOR, game.SCISSOR),
                       (game.SCISSOR, game.ROCK),
                       (game.SCISSOR, game.PAPER),
                       (game.PAPER, game.SCISSOR),
                       (game.PAPER, game.ROCK),
                       (game.PAPER, game.PAPER)]
        result_list = [1, 0, 2, 0, 2, 1, 2, 1, 0]

        assert all(game.compare_choice(choice_list[i][0], choice_list[i][1])
                   == result_list[i] for i in range(len(result_list)))


if __name__ == '__main__':
    unittest.main()

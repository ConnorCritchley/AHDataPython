# Connor Critchley
# Day 12 Lab

import unittest
import cards

class MyTestCase(unittest.TestCase):
    # Test for numerical helper function
    def test_numerical_1(self):
        self.assertEqual(cards.numerical('S2'), 2)
    def test_numerical_2(self):
        self.assertEqual(cards.numerical('S3'), 3)
    def test_numerical_3(self):
        self.assertEqual(cards.numerical('S4'), 4)
    def test_numerical_4(self):
        self.assertEqual(cards.numerical('S5'), 5)
    def test_numerical_5(self):
        self.assertEqual(cards.numerical('S6'), 6)
    def test_numerical_6(self):
        self.assertEqual(cards.numerical('S7'), 7)
    def test_numerical_7(self):
        self.assertEqual(cards.numerical('S8'), 8)
    def test_numerical_8(self):
        self.assertEqual(cards.numerical('S9'), 9)
    def test_numerical_9(self):
        self.assertEqual(cards.numerical('S10'), 10)
    def test_numerical_10(self):
        self.assertEqual(cards.numerical('SJ'), 11)
    def test_numerical_11(self):
        self.assertEqual(cards.numerical('SQ'), 12)
    def test_numerical_12(self):
        self.assertEqual(cards.numerical('SK'), 13)
    def test_numerical_13(self):
        self.assertEqual(cards.numerical('SA'), 14)


    # Tests for check_straight
    def test_straight_1(self):  # basic case
        self.assertEqual((cards.check_straight('S2', 'S3', 'S4')), 4)
    def test_straight_2(self):  # incorrect case
        self.assertEqual((cards.check_straight('S2', 'S5', 'SK')), 0)
    def test_straight_3(self):  # flush case
        self.assertEqual((cards.check_straight('SQ', 'SK', 'SA')), 14)
    def test_straight_4(self):  # mixing letter and face
        self.assertEqual((cards.check_straight('S9', 'S10', 'SJ')), 11)
    def test_straight_5(self): # incorrect mixing letter and face
        self.assertEqual((cards.check_straight('S9', 'SJ', 'SQ')), 0)
    def test_straight_6(self):  # wraparound
        self.assertEqual((cards.check_straight('S2', 'SK', 'SA')), 0)


    # test for 3ofaKind
    def test_3Kind_1(self):  # basic case
        self.assertEqual((cards.check_3ofa_kind('S2', 'S2', 'S2')), 2)
    def test_3Kind_2(self):  # higher case
        self.assertEqual((cards.check_3ofa_kind('S10', 'S10', 'S10')), 10)
    def test_3Kind_3(self):  # highest case
        self.assertEqual((cards.check_3ofa_kind('SA', 'SA', 'SA')), 14)
    def test_3Kind_4(self):  # incorrect case
        self.assertEqual((cards.check_3ofa_kind('S2', 'S4', 'S2')), 0)
    def test_3Kind_5(self):  # mixed inccorect
        self.assertEqual((cards.check_3ofa_kind('S9', 'S4', 'SJ')), 0)
    def test_3Kind_6(self):  # close to correct incorrect
        self.assertEqual((cards.check_3ofa_kind('SQ', 'SQ', 'SJ')), 0)


    # tests for flush
    def test_flush_1(self):  # basic
        self.assertEqual((cards.check_royal_flush('SQ', 'SK', 'SA')), 14)
    def test_flush_2(self):  # incorrect but close
        self.assertEqual((cards.check_royal_flush('SQ', 'SK', 'S2')), 0)
    def test_flush_3(self):  # incorrect, in different spot
        self.assertEqual((cards.check_royal_flush('SJ', 'SK', 'SA')), 0)
    def test_flush_4(self):  # regular flush
        self.assertEqual((cards.check_royal_flush('S2', 'S3', 'S4')), 0)
    def test_flush_5(self):  # shifted back 1
        self.assertEqual((cards.check_royal_flush('SJ', 'SQ', 'SK')), 0)


    # Tests for play cards
    def test_cards_1(self):  # dual stright, right higher
        self.assertEqual((cards.play_cards('S2', 'S3', 'S4',
                                           'S5', 'S6', 'S7')), 1)
    def test_cards_2(self):  # 3kind vs straight, right wins
        self.assertEqual((cards.play_cards('S2', 'S2', 'S2',
                                           'S5', 'S6', 'S7')), 1)
    def test_cards_3(self):  # s3kind vs straight ,left win
        self.assertEqual((cards.play_cards('S2', 'S3', 'S4',
                                           'S2', 'S2', 'S2')), -1)
    def test_cards_4(self):  # flush vs straight, left win
        self.assertEqual((cards.play_cards('SQ', 'SK', 'SA',
                                           'S5', 'S6', 'S7')), -1)
    def test_cards_5(self): # flush vs straight, right win
        self.assertEqual((cards.play_cards('S2', 'S3', 'S4',
                                           'SQ', 'SK', 'SA')), 1)
    def test_cards_6(self):  # 3kind draw
        self.assertEqual((cards.play_cards('S4', 'S4', 'S4',
                                           'S4', 'S4', 'S4')), 0)
    def test_cards_7(self):  #  dual straight, left higher
        self.assertEqual((cards.play_cards('S6', 'S7', 'S8',
                                           'S5', 'S6', 'S7')), -1)
    def test_cards_8(self):  # dual flush, draw
        self.assertEqual((cards.play_cards('SQ', 'SK', 'SA',
                                           'SQ', 'SK', 'SA')), 0)
    def test_cards_9(self):  # dual straight, draw
        self.assertEqual((cards.play_cards('S4', 'S5', 'S6',
                                           'S4', 'S5', 'S6')), 0)
    def test_cards_10(self):  # 3kind vs flush, right win
        self.assertEqual((cards.play_cards('S10', 'S10', 'S10',
                                           'SQ', 'SK', 'SA')), 1)
    def test_cards_11(self):  # 3kind vs nothing, left win
        self.assertEqual((cards.play_cards('SQ', 'SQ', 'SQ',
                                           'SQ', 'SK', 'S2')), -1)
    def test_cards_12(self):  # dual 3kind, right win
        self.assertEqual((cards.play_cards('SQ', 'SQ', 'SQ',
                                           'SA', 'SA', 'SA')), 1)
    def test_cards_13(self):  # nothing vs nothing, draw
        self.assertEqual((cards.play_cards('SQ', 'SK', 'S2',
                                           'S2', 'SK', 'SA')), 0)





if __name__ == '__main__':
    unittest.main()

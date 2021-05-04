import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame()
    
    def test_check_for_ace(self):
       new_card= Card("Clubs", 1) 
       self.assertEqual(True, self.game.check_for_ace(new_card))

    def test_highest_card(self):
        card1 = Card("Hearts", 4)
        card2 = Card("Spades", 10)
        self.assertEqual(card2, self.game.highest_card(card1, card2))

    def test_cards_total(self):
        card1 = Card("Hearts", 4)
        card2 = Card("Spades", 10)
        cards = [card1, card2]
        self.assertEqual("You have a total of 14", self.game.cards_total(cards))
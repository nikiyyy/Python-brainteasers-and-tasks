import unittest
import cardsSort

class TestCardSort(unittest.TestCase):
    
    def test_gamerule1_positive(self):
        Deck = [cardsSort.Card("pika","queen"),cardsSort.Card("karo","king"),cardsSort.Card("kupa","10"),cardsSort.Card("spatiq","7")]
        for i,j in zip(["7", "queen", "king" , "10"],cardsSort.sortByRules1(Deck)):
            self.assertEqual(i,j.getter_name())

    def test_gamerule1_negative(self):
        Deck = [cardsSort.Card("pika","queen"),cardsSort.Card("karo","king"),cardsSort.Card("kupa","10"),cardsSort.Card("spatiq","7")]
        for i,j in zip(["10", "king", "queen" , "7"],cardsSort.sortByRules1(Deck)):
            self.assertFalse(i == j.getter_name())
        
if __name__ == "__main__":
    unittest.main()

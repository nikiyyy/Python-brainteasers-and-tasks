import unittest
import OldPhone

class TestOP(unittest.TestCase):
    def test_num_to_char_PositiveT_Smoketest(self):
        self.assertEqual(OldPhone.convert_nums_to_chars("8 44 33 1 77 88 444 222 55 1 22 777 666 9 66 1 333 666 99 1 5 88 6 7 33 3 1 666 888 33 777 1 8 44 33 1 555 2 9999 999 1 3 666 4 "), "the quick brown fox jumped over the lazy dog")
        
    def test_num_to_char_NegativeT_Invalid_input_numbers(self):
        self.assertEqual(OldPhone.convert_nums_to_chars("uhf"), "None")
        
    
    def test_char_to_num_PositiveT_Smoketest(self):
        self.assertEqual(OldPhone.convert_chars_to_nums("the quick brown fox jumped over the lazy dog"), "8 44 33 1 77 88 444 222 55 1 22 777 666 9 66 1 333 666 99 1 5 88 6 7 33 3 1 666 888 33 777 1 8 44 33 1 555 2 9999 999 1 3 666 4 ")
        
    def test_char_to_num_NegativeT_Invalid_input_numbers(self):
        self.assertEqual(OldPhone.convert_chars_to_nums("556"), "ERROR")
    
if __name__ == "__main__":
    unittest.main()
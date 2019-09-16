from HighCard1 import HighCard
from CardType import CardType
import unittest
import random
import constant
class Solution(object):

    ### generate testcase ###
    ### useless!for we have to judge personlly!
    ### actually,there exists some small problem ,using set would be better!###

    def generate_testcase(self):
        #random.seed(50)
        return_value = []
        for i in range(5):
            temp_number = random.randint(0,3)
            if temp_number == 0:
                temp_char = 'a'
            elif temp_number == 1:
                temp_char = 'b'
            elif temp_number == 2:
                temp_char = 'c'
            else:
                temp_char = 'd'
            temp_number = random.randint(2,14)
            return_value.append((temp_char,temp_number))
        return return_value

    ##if card1 < card2    then:  return  True##
    ##if card1 > card2    then:  return  False##
    ##if card1 = card2    then:  return  Equal##
    def compare(self,list1,list2):
        cardtype1 = HighCard.check_Card_Type(self,list1)   
        cardtype2 = HighCard.check_Card_Type(self,list2)
        return CardType.compare_after_every_card_type_got(self,cardtype1,cardtype2)

class SolutionSuit(unittest.TestCase):
    def test_should_print_testcase(self):
        print(Solution.generate_testcase(self))
    
    def test_should_judge_for_two_testcase(self):
        testcase1 = [('b',3), ('c',5), ('d', 4), ('d', 6), ('d', 7)]
        testcase2 = [('b',8), ('c',5), ('d', 4), ('d', 6), ('d', 7)]
        self.assertEqual(Solution.compare(self,testcase1,testcase2),True)

    def test_should_judge_for_two_equal_testcase(self):
        testcase1 = [('b',3), ('c',5), ('d', 4), ('d', 6), ('d', 7)]
        testcase2 = [('b',3), ('c',5), ('d', 4), ('d', 6), ('d', 7)]
        self.assertEqual(Solution.compare(self,testcase1,testcase2),constant.EQUAL)
    
if __name__   =='__main__':
     unittest.main()
     SystemExit

import constant
from Help import Help 
import unittest
from CardType import CardType

            

class HighCard(object):
    def check_Card_Type(self,list1):
        temp_result_1 = HighCard.check_whether_is_ROYAL_FLUSH(self,list1)
        temp_result_2 = HighCard.check_whether_is_STRAIGHT_FLUSH(self,list1)
        temp_result_3 = HighCard.check_whether_is_FOUR_OF_A_KIND(self,list1)
        temp_result_4 = HighCard.check_whether_is_FULL_HOUSE(self,list1)
        temp_result_5 = HighCard.check_whether_is_FLUSH(self,list1)
        temp_result_6 = HighCard.check_whether_is_STRAIGHT(self,list1)
        temp_result_7 = HighCard.check_whether_is_THREE_OF_A_KIND(self,list1)
        temp_result_8 = HighCard.check_whether_is_TWO_PAIRS(self,list1)
        temp_result_9 = HighCard.check_whether_is_ONE_PAIR(self,list1)
        temp_result_10 = HighCard.check_whether_is_HIGH_CARD(self,list1)
        if temp_result_1[0] == True:
            return CardType(constant.ROYAL_FLUSH,temp_result_1[1])
        elif temp_result_2[0] == True:
            return CardType(constant.STRAIGHT_FLUSH,temp_result_2[1])
        elif temp_result_3[0] == True:
            return CardType(constant.FOUR_OF_A_KIND,temp_result_3[1],temp_result_3[2])
        elif temp_result_4[0] == True:
            return CardType(constant.FULL_HOUSE,temp_result_4[1],temp_result_4[2])
        elif temp_result_5[0] == True:
            return CardType(constant.FLUSH,temp_result_5[1],temp_result_5[2])
        elif temp_result_6[0] == True:
            return CardType(constant.STRAIGHT,temp_result_6[1])
        elif temp_result_7[0] == True:
            return CardType(constant.THREE_OF_A_KIND,temp_result_7[1],temp_result_7[2],temp_result_7[3])
        elif temp_result_8[0] == True:
            return CardType(constant.TWO_PAIRS,temp_result_8[1],temp_result_8[2],temp_result_8[3])
        elif temp_result_9[0] == True:
            return CardType(constant.ONE_PAIR,temp_result_9[1],temp_result_9[2],temp_result_9[3],temp_result_9[4])
        else :
            return CardType(constant.HIGH_CARD,temp_result_10[1],temp_result_10[2],temp_result_10[3] \
            ,temp_result_10[4],temp_result_10[5])
    
    #tonghuadashun
    def check_whether_is_ROYAL_FLUSH(self,list1):
        return_value = []
        if Help.check_whether_is_the_same_color(self,list1) == False \
          or Help.check_is_straight(self,list1) == False:
            return_value.append(False)
            return return_value
        else:
            list_sorted = sorted(list1,key = lambda x:(x[1],x[0].lower()))
            if list_sorted[-1][-1] == constant.ACE:
                return_value.append(True)
            else:
                return_value.append(False)
            return return_value
            
    #tonghuashun
    def check_whether_is_STRAIGHT_FLUSH(self, list1):
        return_value = []
        if Help.check_whether_is_the_same_color(self,list1) == False \
          or Help.check_is_straight(self,list1) == False:
            return_value.append(False)
            return return_value
        else:
            list_sorted = sorted(list1,key = lambda x:(x[1],x[0].lower()))
            return_value.append(True)
            return_value.append(list_sorted[-1][-1])
            return return_value

    #sitiao
    def check_whether_is_FOUR_OF_A_KIND(self, list1):
        return_value = []
        number_dict = {}
        number_dict = Help.count_numbers(self,list1)
        testcase_is_four_of_a_kind = False
        temp_record_number_occurs_four_times = constant.ZERO
        for  key in number_dict:
            if(number_dict.get(key) == constant.LENGTH_FOUR):
                testcase_is_four_of_a_kind = True
                temp_record_number_occurs_four_times = key
        
        return_value.append(testcase_is_four_of_a_kind)
        return_value.append(temp_record_number_occurs_four_times)
        return return_value

        
    #mantanghong
    def check_whether_is_FULL_HOUSE(self, list1):
        return_value = []
        number_dict = {}
        number_dict = Help.count_numbers(self,list1)
        testcase_is_full_house  = False
        card_number_occurr_three_times = constant.ZERO
        card_number_occurr_two_times = constant.ZERO
        for  key in number_dict:
            if number_dict.get(key) == constant.LENGTH_THREE:
                testcase_is_full_house = True
                card_number_occurr_three_times = key
            if number_dict.get(key) == constant.LENGTH_TWO:
                card_number_occurr_two_times = key

        return_value.append(testcase_is_full_house)
        return_value.append(card_number_occurr_three_times)
        return_value.append(card_number_occurr_two_times)
        return return_value
        
    #tonghua
    def check_whether_is_FLUSH(self, list1):
        return_value,number_list = [],[]
        number_list  = Help.get_number_list(self,list1)
        color_dict =  Help.count_color(self,list1)
        testcase_is_flush = False
        if len(color_dict) == constant.LENGTH_ONE:
            testcase_is_flush = True
        return_value.append(testcase_is_flush)
        return_value.append(number_list[-1])
        return_value.append(number_list[-2])
        return_value.append(number_list[-3])
        return_value.append(number_list[-4])
        return_value.append(number_list[-5])
        return return_value
        
    #shunzi
    def check_whether_is_STRAIGHT(self, list1):
        return_value,number_list = [],[]
        number_list = Help.get_number_list(self,list1)
        testcase_is_straight = Help.check_is_straight(self,list1)
        return_value.append(testcase_is_straight)
        return_value.append(number_list[-1])
        return return_value

    #santiao
    def check_whether_is_THREE_OF_A_KIND(self, list1):
        return_value,number_list = [],[]
        number_list  = Help.get_number_list(self,list1)
        number_dict = Help.count_numbers(self,list1)
        testcase_is_three_of_a_kind = False
        testcase_has_three_pair = False
        card_number_occurr_three_times  = constant.ZERO
        for key in number_dict:
            if number_dict.get(key) == constant.LENGTH_THREE:
                testcase_has_three_pair = True
                card_number_occurr_three_times = key
        if testcase_has_three_pair:
            testcase_is_three_of_a_kind = True
        
        return_value.append(testcase_is_three_of_a_kind)
        return_value.append(card_number_occurr_three_times)
        temp_number_list = []
        for key in number_list:
            if key == card_number_occurr_three_times:
                pass
            else:
                temp_number_list.append(key)
        return_value.append(temp_number_list[1])
        return_value.append(temp_number_list[0])
        return return_value
            
    def check_whether_is_TWO_PAIRS(self, list1):
        return_value = []
        number_dict = Help.count_numbers(self,list1)
        temp_record_number_occurs_two_times = []
        temp_record_number_occurs_only_one_time = constant.ZERO
        number_equals_two_when_has_two_pairs = constant.ZERO
        for key in number_dict:
            if number_dict.get(key) == constant.LENGTH_TWO:
                number_equals_two_when_has_two_pairs = \
                  number_equals_two_when_has_two_pairs + 1
                temp_record_number_occurs_two_times.append(key)
            else:
                temp_record_number_occurs_only_one_time = key
        
        if number_equals_two_when_has_two_pairs == constant.LENGTH_TWO:
            return_value.append(True)
            if temp_record_number_occurs_two_times[0] > temp_record_number_occurs_two_times[1]:
                return_value.append(temp_record_number_occurs_two_times[0])
                return_value.append(temp_record_number_occurs_two_times[1])
            else:
                return_value.append(temp_record_number_occurs_two_times[1])
                return_value.append(temp_record_number_occurs_two_times[0])
            return_value.append(temp_record_number_occurs_only_one_time)
        else:
            return_value.append(False)
        return return_value

    def check_whether_is_ONE_PAIR(self, list1):
        return_value = []
        testcase_has_one_one_pair = False
        temp_record_number_occurs_twice = constant.ZERO
        number_dict = Help.count_numbers(self,list1)
        if len(number_dict) == constant.LENGTH_FOUR:
            testcase_has_one_one_pair = True
        for key in number_dict:
            if number_dict.get(key) == constant.LENGTH_TWO:
                temp_record_number_occurs_twice = key
        return_value.append(testcase_has_one_one_pair)
        return_value.append(temp_record_number_occurs_twice)
        number_list = Help.get_number_list(self,list1)
        if testcase_has_one_one_pair == True:
            number_list.remove(temp_record_number_occurs_twice)
            number_list.remove(temp_record_number_occurs_twice)
        number_list.reverse()
        for key in number_list:
            return_value.append(key)
        return return_value

    def check_whether_is_HIGH_CARD(self, list1):
        return_value = []
        number_dict = Help.count_numbers(self,list1)
        testcase_is_high_card = False
        if len(number_dict) == constant.LENGTH_FIVE:
            testcase_is_high_card = True
        return_value.append(testcase_is_high_card)
        number_list = Help.get_number_list(self,list1)
        number_list.reverse()
        for key in number_list:
            return_value.append(key)
        return return_value

class HighCardSuit(unittest.TestCase):
    # def test_should_print_testcase(self):
    #     print(Solution.generate_testcase(self))
    
    # def test_should_judge_whether_is_straight_or_not(self):
    #     testcase = [('b',3), ('c',5), ('d', 4), ('d', 6), ('d', 7)]
    #     self.assertEqual(Help.check_is_straight(self,testcase),True)
    
    def test_should_judge_whether_is_royal_flush(self):
        testcase = [('d',10), ('d',11), ('d', 12), ('d', 13), ('d', 14)]
        self.assertEqual(HighCard.check_whether_is_ROYAL_FLUSH(self,testcase),[True])

    def test_should_judge_whether_is_straight_flush(self):
        testcase = [('d',10), ('d',11), ('d', 12), ('d', 13), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_STRAIGHT_FLUSH(self,testcase),[True,13])
    
    def test_should_judge_whether_is_four_of_a_kind(self):
        testcase = [('d',10), ('c',10), ('a', 10), ('b', 10), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_FOUR_OF_A_KIND(self,testcase),[True,10])

    def test_should_judge_whether_is_full_house(self):
        testcase = [('d',10), ('c',10), ('a', 10), ('b', 9), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_FULL_HOUSE(self,testcase),[True,10,9])
    
    def test_should_judge_whether_is_flush(self):
        testcase = [('d',10), ('d',7), ('d', 12), ('d', 4), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_FLUSH(self,testcase),[True,12,10,9,7,4])

    def test_should_judge_whether_is_straight(self):
        testcase = [('d',10), ('c',7), ('d', 8), ('d', 6), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_STRAIGHT(self,testcase),[True,10])

    def test_should_judge_whether_is_three_of_a_kind(self):
        testcase = [('d',6), ('c',6), ('d', 8), ('a', 6), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_THREE_OF_A_KIND(self,testcase),[True,6,9,8])

    def test_should_judge_whether_is_two_pairs(self):
        testcase = [('d',6), ('c',6), ('d', 8), ('a', 8), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_TWO_PAIRS(self,testcase),[True,8,6,9])

    def test_should_judge_whether_is_one_pair(self):
        testcase = [('d',6), ('c',6), ('d', 4), ('a', 8), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_ONE_PAIR(self,testcase),[True,6,9,8,4])    

    def test_should_judge_whether_is_high_card(self):
        testcase = [('d',4), ('c',6), ('d', 10), ('a', 8), ('d', 9)]
        self.assertEqual(HighCard.check_whether_is_HIGH_CARD(self,testcase),[True,10,9,8,6,4]) 

    def test_should_return_card_type(self):
        testcase = [('d',6), ('c',6), ('d', 8), ('a', 8), ('d', 9)]
        self.assertEqual(HighCard.check_Card_Type(self,testcase),CardType(constant.TWO_PAIRS,8,6,9))

if __name__   =='__main__':
    unittest.main()
    SystemExit
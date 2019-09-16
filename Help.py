from collections import Counter
import unittest

class Help(object):
    def count_numbers(self,list1):
        number_list = []
        number_dict = {}
        for key in list1:
            number_list.append(key[-1])
        number_dict = Counter(number_list)
        return number_dict
    
    def count_color(self,list1):
        color_list = []
        color_dict = {}
        for key in list1:
            color_list.append(key[0])
        color_dict = Counter(color_list)
        return color_dict
    
    def get_number_list(self,list1):
        number_list,return_value = [],[]
        for key in list1:
            number_list.append(key[-1])
        return_value = sorted(number_list)
        return return_value

    def check_is_straight(self,list1):
        number_list = Help.get_number_list(self,list1)
        min_number = number_list[0]
        if number_list [1] == min_number + 1 and number_list[2] == min_number + 2 \
            and number_list[3] == min_number + 3 and number_list[4] ==min_number + 4 :
            return True
        else:
            return False

    def check_whether_is_the_same_color(self, list1):
        list_one = []
        for key in list1:
            list_one.append(key[0])
        dict1  = {}
        dict1 = Counter(list_one)
        return len(dict1) == 1
        
class HelpSuit(unittest.TestCase):
    # def test_should_print_testcase(self):
    #     print(Solution.generate_testcase(self))
    
    def test_should_judge_whether_is_straight_or_not(self):
        testcase = [('b',3), ('c',5), ('d', 4), ('d', 6), ('d', 7)]
        self.assertEqual(Help.check_is_straight(self,testcase),True)
    
if __name__   =='__main__':
    unittest.main()
    SystemExit


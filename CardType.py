import constant
class CardType(object):
    def __init__(self,cardtype=constant.HIGH_CARD  \
    ,card1 = constant.ZERO ,card2 = constant.ZERO,card3 = constant.ZERO \
    ,card4 = constant.ZERO ,card5 = constant.ZERO):
        ##type is a neccesary choice!##
        ##card1~5 are alterative which is decided by the cardtype
        ##for example:
        #    when is STRAIGHT,we only need (type,card1) to record (the card type,the maximum nubmer in the STRAIGHT)
        #    that is enough for comparing##
        self.type = cardtype
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
        self.card5 = card5
    

    ###True means case1 < case2 ###
    def compare_after_every_card_type_got(self, cardtype1,cardtype2):
        if cardtype1.type < cardtype2.type:
            return True
        elif cardtype1.type > cardtype2.type:
            return False
        else:
            ##only when the same card type goes here!##
            ##value_1,value_2 represents their relative value##
            ##they are valid only when they are the same type!!###
            value_1 = cardtype1.card1 * 13**4 + cardtype1.card2 *13**3  + cardtype1.card3 * 13**2 + \
                cardtype1.card4 * 13**1 + cardtype1.card5 * 1
            value_2 = cardtype2.card1 * 13**4 + cardtype2.card2 * 13**3 + cardtype2.card3 * 13**2 + \
                cardtype2.card4 * 13**1 + cardtype2.card5 * 1
            if value_1 > value_2:
                return False
            elif value_1 < value_2:
                return True
            else :
                return constant.EQUAL
    
    def __eq__(self,other):
        if isinstance(other,self.__class__) and self.type == other.type \
            and self.card1 == other.card1 and self.card2 == other.card2 \
            and self.card3 == other.card3 and self.card4 == other.card5 \
            and self.card5 == other.card5:
            return True
        else:
            return False
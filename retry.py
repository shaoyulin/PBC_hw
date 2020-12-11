'''
有A  -- 1分
對子 -- 2分
同花 -- 3分 (五章同花色)
順子 -- 5分
葫蘆 -- 10分
鐵支 -- 20分
同花順 -- 100分
'''

# retry
suitlist = "S,H,D,C".split(",")
ranklist = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")

class Card:
    def __init__(self, suit, rank, setlist):
        self.suit = suit
        self.rank = rank
        self.setlist = setlist
    
    def ace(self):
        return self.rank.count('A')

    def pair(self):
        pair_cnt = 0
        for x in ranklist:
            if self.rank.count(x) >= 2:
                pair_cnt += 1
        return pair_cnt
    
    def straight(self):
        straightStr = ''
        for x in ranklist:
            if self.rank.count(x) != 1:
                continue
            if x in self.rank:
                straightStr += x
        # return straightStr
        rankStr = "A23456789JQKA23456789"
        no_straight_cnt = 0
        if len(straightStr) == 5:
            for i in range(len(rankStr)):
                if straightStr == rankStr[i:i+5]:
                    return True
                else:
                    no_straight_cnt += 1
            if no_straight_cnt == len(rankStr):
                return False
        else:
            return False
    
    def flush(self):
        no_flush_cnt = 0
        for x in suitlist:
            if self.suit.count(x) == 5:
                return True
            else:
                no_flush_cnt += 1
        if no_flush_cnt == 4:
            return False
    
    def quads(self):
        for x in ranklist:
            quads_cnt = 0
            no_quads_cnt = 0
            for i in range(len(self.setlist)):
                if self.setlist[i][1] == x:
                    quads_cnt += 1
                    if quads_cnt == 4:
                        return True
            if quads_cnt != 4:
                return False

    def gourds(self):
        for x in ranklist:
            no_gourds_cnt = 0
            if self.rank.count(x) == 3:
                left = self.rank.replace(x,"")
                # return left
                for y in ranklist:
                    if left.count(y) == 2:
                        return True
                    else:
                        no_gourds_cnt += 1
                if no_gourds_cnt == 13:
                    return False
            else:
                return False



suits = input()
ranks = input()
suit_name = suits.split(',')
rank_name = ranks.split(',')

nameList = []
for i in range(5):
    nameList.append([suit_name[i], rank_name[i]])

name = Card(suits, ranks, nameList)
# print(name.suit, name.rank)
# print(name.setlist)     # 牌型
# print(name.quads())     # 鐵支
# print(name.gourds())    # 葫蘆
# print(name.flush())     # 同花
# print(name.straight())  # 順子
# print(name.pair())      # 對子
# print(name.ace())       # Ace

if (name.straight() == True) and (name.flush() == True):
    print(100)
else:
    if (name.quads() == True):
        if ranks.count('A') == 1:
            print(21)
        else:
            print(20)
    else:
        if (name.gourds() == True):
            print(10)
        else:
            if (name.flush() == True):
                print(5)
            else:
                if (name.pair() == 2):
                    if ranks.count('A') == 1:
                        print(5)
                    else:
                        print(4)
                else:
                    if (name.straight == True):
                        print(3)
                    else:
                        if (name.ace() == 3):
                            print(3)
                        else:
                            if (name.pair() == 1):
                                if ranks.count('A') == 1:
                                    print(3)
                                else:
                                    print(2)
                            else:
                                if (name.ace() == 1):
                                    print(1)
                                else:
                                    print(0)


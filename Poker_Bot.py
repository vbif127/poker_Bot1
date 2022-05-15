import random as rd
from bank import Bank
f""" 3 -> 1 -> 2; 3 = BTN ; 2 = BB ; 1 = SB
    3 -> 3=2 -> 1 -> 1=3 -> 2 -> 2=1
    2 -> 3 -> 1
    2 -> 1 -> 3
    
"""
g = ["Hand1", "Hand2",]
j = ["🧑", "🐻"]
reis = {}
class Poker_Bot:
    def __init__(self, pr, ct):
        self.settings = pr
        self.ct = ct
        self.count = 1


    def random(self):
        cards = []
        int_card = ["2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "T.", "J.", "Q.", "K.", "A."]
        masti = ["\U0001f537", "\u2764\ufe0f ", "\u2618\ufe0f ", "\U0001f5a4"]
        for b in int_card:
            for a in masti:
                cards.append(b + a)
        settings = {
            "board": [],
            "Bot  ": {"v": [], "b": 0},# BTN ; BB ; SB
            "Hand1": {"v": [], "b": 0},# SB ; BTN ; BB
            "Hand2": {"v": [], "b": 0},# BB ; SB ; BTN
            # "Hand3": {"v": [], "b": 0},
            # "Hand4": {"v": [], "b": 0},
        }
        for i in range(5):
            flop_2 = rd.choice(cards)
            cards.remove(flop_2)
            settings["board"].append(flop_2)
        def hand(name):
            for i in range(2):
                flop_1 = rd.choice(cards)
                cards.remove(flop_1)
                settings[f"{name}"]["v"].append(flop_1)
            return settings[f"{name}"]["v"]
        return hand("Bot  "), hand("Hand1"), hand("Hand2"), settings["board"]
    def blaynd(self, string):
        name = rd.randint(1, 3)
        self.settings[f"{self.ct['revers1'][name]}"]["b"] = "3"
        if self.settings["Bot  "]["b"] == "3":
            string += "3 1 2"
            self.settings["Hand1"]["b"] = "1"
            self.settings["Hand2"]["b"] = "2"
        elif self.settings["Hand1"]["b"] == "3":
            string += "2 3 1"
            self.settings["Bot  "]["b"] = "1"
            self.settings["Hand2"]["b"] = "2"
        elif self.settings["Hand2"]["b"] == "3":
            string += "1 2 3"
            self.settings["Hand1"]["b"] = "1"
            self.settings["Bot  "]["b"] = "2"
        return string
    def print_hand(self, a):
        s = self.settings
        # a = self.blaynd("")
        print(f"Раздача: № {self.count}")
        b = a
        a = a.replace("3", "BTN")
        a = a.replace("2", "BB_")
        a = a.replace("1", "SB_")
        list_ = a.split(' ')
        rdc = self.random()
        for i in g:
            if i == "Hand1":
                emoji = j[0]
                hand = rdc[1]
            elif i == "Hand2":
                emoji = j[1]
                hand = rdc[2]
            else:
                emoji = j[2]
                hand = rdc[0]
            if self.settings[f"{i}"]["fishki"] < 100:
                print(' --------------------------------')
                print('|           ------ ------',f'{self.settings[f"{i}"]["fishki"]}     |')
            else:
                print(' --------------------------------')
                print('|           ------ ------',f'{self.settings[f"{i}"]["fishki"]}    |')
            print(f'| {i}{emoji}:','|',hand[0],'|',hand[1],'|', '      |')
            print(f'|           ------ ------',f'{list_[self.ct["revers2"][f"{i}"]]}    |')
            print(' --------------------------------')
            input()
            s = "\n"
            print(f"{s*0}")
        self.print_flop(rdc, b)
    def rd2(self, string):
        if string == "3 1 2":
            self.print_hand("2 3 1")
            self.settings["Bot  "]["b"] = "2"
            self.settings["Hand1"]["b"] = "3"
            self.settings["Hand2"]["b"] = "1"
        elif string == "2 3 1":
            self.print_hand("1 2 3")
            self.settings["Bot  "]["b"] = "1"
            self.settings["Hand1"]["b"] = "2"
            self.settings["Hand2"]["b"] = "3"
        elif string == "1 2 3":
            self.print_hand("3 1 2")
            self.settings["Bot  "]["b"] = "3"
            self.settings["Hand1"]["b"] = "1"
            self.settings["Hand2"]["b"] = "2"
    def print_flop(self, rdc, b):
        bank = self.bank(b)
        bank.start_preflop()
        board = rdc[3]
        print(' --------------------------------')
        print('|          ------ ------ ------  |')
        print('|''  ','Flop:','|',board[0],'|',board[1],'|',board[2],'|','|' )
        print('|          ------ ------ ------  |')
        print(' --------------------------------')
        input()
        s = "\n"
        print(f"{s*1}")
        bank.start_preflop()
        self.print_turn(rdc, b, bank)

    def print_turn(self, rdc, b, bank):
        board = rdc[3]
        print(' -------------------------------- ------------------ '                           )
        print('|          ------ ------ ------  |         ------   |'                           )
        print('|''  ','Flop:','|',board[0],'|',board[1],'|',board[2],'|', f'|  Turn: | {board[3]} |  |' )
        print('|          ------ ------ ------  |         ------   |'                           )
        print(' -------------------------------- ------------------',                           )
        input()
        s = "\n"
        print(f"{s*1}")
        self.print_river(rdc, b)
        
    def print_river(self, rdc, b):
        board = rdc[3]
        print(' -------------------------------- ------------------ -------------------'                                          )
        print('|          ------ ------ ------  |         ------   |          ------   |'                                         )
        print('|''  ','Flop:','|',board[0],'|',board[1],'|',board[2],'|', f'|  Turn: | {board[3]} |  |  River: | {board[4]} |  |' )
        print('|          ------ ------ ------  |         ------   |          ------   |'                                         )
        print(' -------------------------------- ------------------ -------------------',                                         )
        input()
        self.count += 1
        input()
        s = "\n"
        print(f"{s*1}")
        self.print_bot(rdc, b)
    def print_bot(self, rdc, b):
        hand = rdc[0]
        print(' ---------------------------'                )
        print('|           ------ ------','  |'             )
        print('| Bot 🤖:','|',hand[0],'|',hand[1],'|', '  |')
        print('|           ------ ------','  |'             )
        print(' ---------------------------'                )
        # t = input("yes/no:")
        t = "y"
        if t == "y":
            self.rd2(b)
            s = "\n"
            print(f"{s*1}")
    def bank(self, str):
        pisful = [["Chek"], ["Coll"], []]
        medium = [["Chek"], ["Coll"], [], []]
        hard =   [["Chek"], ["Coll"], [], [], []]
        fishki = self.settings["Bot  "]["fishki"]
        for i in range(1, 1001):
            reis[f"Rais({i})"] = i
        for i in range(1, fishki + 1):
            pisful[2].append(f"Rais({i})")
        for i in range(1, fishki + 1):
            medium[2].append(f"Rais({i})")
            medium[3].append(f"Rais({i})")
        for i in range(1, fishki + 1):
            hard[2].append(f"Rais({i})")
            hard[3].append(f"Rais({i})")
            hard[4].append(f"Rais({i})")
        bank = Bank(self.settings, reis, pisful, str)
        return bank
import random as rd


class Bank:
    def __init__(self, players, reis, dificalti, str):
        self.players = players
        self.reis = reis
        self.dificalti = dificalti
        self.str = str
        self.fishki = 0
    def start_preflop(self):
        i = self.str.split(" ")
        if i[0] == "1":
            if self.players["Bot  "]["do"] != "Fold":
                self.players["Bot  "]["fishki"] -= 1
                self.fishki += 1
        elif i[1] == "1":
            if self.players["Hand1"]["do"] != "Fold":
                self.players["Hand1"]["fishki"] -= 1
                self.fishki += 1
        elif i[2] == "1":
            if self.players["Hand2"]["do"] != "Fold":
                self.players["Hand2"]["fishki"] -= 1
                self.fishki += 1
        if i[0] == "2":
            if self.players["Bot  "]["do"] != "Fold":
                self.players["Bot  "]["fishki"] -= 2
                self.fishki += 2
        elif i[1] == "2":
            if self.players["Hand1"]["do"] != "Fold":
                self.players["Hand1"]["fishki"] -= 2
                self.fishki += 2
        elif i[2] == "2":
            if self.players["Hand2"]["do"] != "Fold":
                self.players["Hand2"]["fishki"] -= 2
                self.fishki += 2
        self.stavki("preflop", self.dificalti)
    def stavki(self, stadiya, dificalti):
        i = self.str.split(" ")
        if stadiya == "preflop":
            if i[1] == "3":
                do_players = input("Сделайте ход Hand1:")
                try:
                    do_players = do_players.split(" ")
                    do_players = int(do_players[1])
                    if do_players == 1:
                        do_players = "Fold"
                        self.players[f'Hand1']['do'] = "fold"
                        self.players[f'Hand1']['v'] = []
                    if do_players >= self.players[f'Hand1']['fishki']:
                        do_players = self.players[f'Hand1']['fishki']
                    self.players["Hand1"]["fishki"] -= do_players
                    self.fishki += do_players
                    print(f"Hand1: {self.players[f'Hand1']['fishki']}")
                    print(f"Bank: {self.fishki}")
                    print(f'Bot  : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
                except:
                    if do_players[0] != "fold":
                        print("Rais $2")
                        self.players["Hand1"]["fishki"] -= 2
                        self.fishki += 2
                        print(f"Hand1: {self.players[f'Hand1']['fishki']}")
                        print(f"Bank: {self.fishki}")
                        print(f'Bot  : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
                    else:
                        print(f"Hand1: {self.players[f'Hand1']['fishki']}")
                        print(f"Bank: {self.fishki}")
                        print("Fold")
                        self.players[f'Hand1']['do'] = "Fold"
                        self.players[f'Hand1']['v'] = []
                        print(f'Bot  : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
            if i[2] == "3":
                do_players = input("Сделайте ход Hand2:")
                try:
                    do_players = do_players.split(" ")
                    do_players = int(do_players[1])
                    if do_players == 1:
                        do_players = "Fold"
                        self.players[f'Hand2']['do'] = "Fold"
                        self.players[f'Hand2']['v'] = []
                    if do_players >= self.players[f'Hand2']['fishki']:
                        do_players = self.players[f'Hand2']['fishki']
                    self.players["Hand2"]["fishki"] -= do_players
                    self.fishki += do_players
                    print(f"Hand2: {self.players[f'Hand2']['fishki']}")
                    print(f"Bank: {self.fishki}")
                    print(f'Bot  : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
                except:
                    if do_players[0] != "fold":
                        print("Rais $2")
                        self.players["Hand2"]["fishki"] -= 2
                        self.fishki += 2
                        print(f"Hand2: {self.players[f'Hand2']['fishki']}")
                        print(f"Bank: {self.fishki}")
                        print(f'Bot  : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
                    else:
                        print("Fold")
                        print(f"Hand1: {self.players[f'Hand2']['fishki']}")
                        print(f"Bank: {self.fishki}")
                        self.players[f'Hand2']['do'] = "Fold"
                        self.players[f'Hand2']['v'] = []
                        print(f'Bot  : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
        if i[0] == "3":
            dificalti.pop(0)
            dificalti = dificalti.pop(1)
            if len(dificalti) > 2:
                dificalti.pop(0)
                do = rd.choice(dificalti)
                # do = rd.choice(do)
                self.players["Bot  "]["do"] = do
                self.players["Bot  "]["fishki"] -= int(self.reis[do])
                self.fishki += int(self.reis[do])
                print(f'Bot : {self.players["Bot  "]["do"]}')
                print(f"Bot : {self.players[f'Bot  ']['fishki']}")
                print(f"Bank: {self.fishki}\n")
                print(f'Bot : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
                # print(self.players)
            else:
                self.players["Bot  "]["do"] = "Fold"
                print(f'Bot : {self.players["Bot  "]["do"]}')
                print(f"Bot : {self.players[f'Bot  ']['fishki']}")
                print(f"Bank: {self.fishki}")
                print(f'Bot  : ${self.players["Bot  "]["fishki"]},\nHand1: ${self.players["Hand1"]["fishki"]},\nHand2: ${self.players["Hand2"]["fishki"]}\n')
        if self.players["Bot  "]["fishki"] <= 0:
            self.players["Bot  "]["do"] = "Fold"
        elif self.players["Hand1"]["fishki"] <= 0:
            self.players["Hand1"]["do"] = "Fold"
        elif self.players["Hand2"]["fishki"] <= 0:
            self.players["Hand2"]["do"] = "Fold"

    def start_flop_(self):
        i = self.str.split(" ")
        if i[0] == "1":
            self.players["Bot  "]["fishki"] -= 1
            self.fishki += 1
        elif i[1] == "1":
            self.players["Hand1"]["fishki"] -= 1
            self.fishki += 1
        elif i[2] == "1":
            self.players["Hand2"]["fishki"] -= 1
            self.fishki += 1
        if i[0] == "2":
            self.players["Bot  "]["fishki"] -= 2
            self.fishki += 2
        elif i[1] == "2":
            self.players["Hand1"]["fishki"] -= 2
            self.fishki += 2
        elif i[2] == "2":
            self.players["Hand2"]["fishki"] -= 2
            self.fishki += 2
        self.stavki("flop", self.dificalti)
from Poker_Bot import Poker_Bot, rd


cards = []
int_card = ["2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "T.", "J.", "Q.", "K.", "A."]
masti = ["\U0001f537", "\u2764\ufe0f ", "\u2618\ufe0f ", "\U0001f5a4"]
for b in int_card:
    for a in masti:
        cards.append(b + a)

ct = ""
pisful = [["Chek"], ["Coll"], []]
medium = [["Chek"], ["Coll"], [], []]
hard =   [["Chek"], ["Coll"], [], [], []]
g = []

settings = {
    "Bot  ": {
        "v": [],
        "b": "", 
        "do":"", 
        "fishki": 100},# BTN ; BB ; SB
    "Hand1": {
        "v": [],
        "b": 0, 
        "do":"", 
        "fishki": 100},# SB ; BTN ; BB
    "Hand2": {
        "v": [],
        "b": 0, 
        "do":"", 
        "fishki": 100},# BB ; SB ; BTN
    # "Hand3": {"v": [], "b": 0},
    # "Hand4": {"v": [], "b": 0},
}
revers ={
    "revers1":{
            1:"Bot  ",
            2:"Hand1",
            3:"Hand2",
        },
    "revers2":{
        "Bot  ":0,
        "Hand1":1,
        "Hand2":2,
    }
}
# settings["Bot  "]["fishki"] = 100
# settings["Bot  "]["fishki"] = int(input("Введите моё количество фишек:"))
fishki = settings["Bot  "]["fishki"]
0
def main():
    bot = Poker_Bot(pr= settings, ct= revers)
    bot.random()
    ce = bot.blaynd(string=ct)
    bot.print_hand(ce)
if __name__ == "__main__":    
    main()

from infos import *
from monster import *
from temp import *
from action_select import *

player1 = Infos(["jm", 10, 10, 10, 10])
player2 = Infos(["jm2", 20, 20, 20, 20])
monster1 = MonsterInfo("서채연")
monster2 = MonsterInfo("이정현")
player1.infos()
monster1.infos()
player1.attack(monster1)
monster1.infos()


players_info = [player1, player2]
monsters_info = [monster1, monster2]
players = ["player1", "player2"]
monsters = ["monster1", "monster2"]
skills = ["공격", "마법"]
dmonsters_info = action_array_select(
    players, players_info, skills, monsters, monsters_info)

monster1.infos()

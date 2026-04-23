import random as r
import os

import funcs
from funcs import restart

steps = 0
Coins = 1
Hp = 3
Atk = 2
Mp = 10

platform_clear = '';platform_clear = funcs.choose_platform(platform_clear)
cheats = input('\n                   Добро пожаловать в RPG игру,Нажми ENTER,чтобы продолжить\n')

Hp,Coins,Atk,Mp,steps = funcs.type_cheats(cheats,Hp,Coins,Atk,Mp,steps)


funcs.start(platform_clear, Hp, Atk, Mp, Coins, steps)
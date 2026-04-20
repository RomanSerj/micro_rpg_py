import os
from pathlib import *
def choose_platform(pl):
    platform = input('\nНа какой платформе ты играешь?'
                     '\nLinux - L'
                     '\nWindows - W'
                     '\n')

    platform = platform.lower()

    if platform == 'l' :
        pl = 'clear'
    elif platform == 'w':
        pl = 'cls'
    else:
        print('\n Плафторма была указана некорректно, назначена платформа по умолчанию(Windows)')
        pl = 'cls'
        input()
    os.system(pl)
    return pl
def type_cheats(cheats,hp,coins,atk,mp,steps):
    if cheats == '2208':
        hp += 9999
        print('Ты активировал чит на здоровье')
    elif cheats == '2008':
        coins += 9999
        print('Ты активировал чит на монеты')
    elif cheats == '0901':
        atk += 9999
        print('Ты активировал чит на атаку')
    elif cheats == '1707':
        mp += 9999
        print('Ты активировал чит на ману')
    elif cheats == '2828':
        steps += 200
        print('Ты активировал чит на шаги')
    elif cheats == '2106':
        hp += 9999
        coins += 9999
        atk += 9999
        mp += 9999
        steps += 200
        print('Ты активировал универсальный чит')

    return hp,coins,atk,mp,steps

def save(hp,coins,atk,mp,steps):
    name = str(input('\nВведите название для сохранения без ".txt"'
                     '\nили нажмите Enter для сохранения файла с названием по умолчанию'
                     '\n*название по умлочанию - sv'
                     '\n!ПРИ СОХРАНЕНИИ ФАЙЛА С НАЗВАНИЕМ ПО УМОЛЧАНИЮ СТАРОЕ СОХРАНЕНИЕ С ТАКИМ ИМЕНЕМ ПЕРЕЗАПИСЫВАЕТСЯ'
                     '\n'))

    if name == '':
        name = 'sv'

    save_folder = 'save'
    os.makedirs(save_folder, exist_ok=True)
    file_path = os.path.join(save_folder, name + '.txt')
    with open(file_path,'w') as f:
        f.write(f'{str(hp)}')
        f.write(f'\n{str(atk)}')
        f.write(f'\n{str(mp)}')
        f.write(f'\n{str(coins)}')
        f.write(f'\n{str(steps)}')

    print('Сохранено!')
    input('Продолжить-> ')


def load(hp,atk,mp,coins,steps):

    folder = Path('save')
    count = 0
    saves = []
    for file in folder.glob('*.txt'):
        saves.append(file.name)
        count +=1
    print(f'\nДоступно {count} сохранений')
    for i,save in enumerate(saves,start=1):
        print(f'{i})',save)

    choose_load = (input('\nВыберите сохранение написав соответствующий ему номер:'
                            '\n'))

    if str(choose_load) == '':
        return hp,atk,mp,coins,steps
    f = open(f'{folder}/{saves[int(choose_load)-1]}','r').readlines()
    hp,atk,mp,coins,steps = map(int,f)

    return hp,atk,mp,coins,steps

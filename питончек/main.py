
from random import randint
from time import sleep
from data import *
from functions import *
name = input('Введи свое имя,игрок')
player['name'] = name 

current_enemy = 0
while True:
        action = input('''
1 - В бой!
2 - Тренировка
3 - Магазин
4 - Показать инвентарь
5 - информация об игроке
6 - информация о противнике
                       ''')
        if action == "1":
                current_enemy = fight(current_enemy)
                if current_enemy == 3:
                        break
        elif action == "2":
                training_type = input('''
1- Тренировать атаку
2 - Тренировать оборону                                      
''')
                training(training_type)
        elif action == '3':
                shop()
        elif action == '4':
                display_inventory()
        elif action == '5':
                display_player()
        elif action == '6':
                display_enemy(current_enemy)
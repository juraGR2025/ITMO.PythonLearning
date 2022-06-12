from random import randint
import time
def player_names():
    global a
    a = input('Enter the name of the player ')
    return (a)

#2. Создайте функцию, реализующий ядро игры.
def core_of_the_game(player_nam_1, player_nam_2):
    #Моделирование бросания кубика первым играющим
    nV1 = 0
    nV2 = 0
    print('Dice rolls', player_nam_1)
    time.sleep(3)
    for i in range(5):
        #Моделирование бросания кубика первым играющим
        n1 = randint(1, 6)
        nV1 = nV1+n1
        print('Dropped out:', nV1)
    time.sleep(3)
    print('Dice rolls', player_nam_2)
    for i in range(5):
        #Моделирование бросания кубика вторым играющим
        n2 = randint(1, 6)
        nV2 = nV2+n2
        print('Dropped out:', nV2)
    time.sleep(3)
    if nV1 > nV2:
        print('Won', player_nam_1)
    elif nV1 < nV2:
        print('Won', player_nam_2)
    else:
        print('No one won')
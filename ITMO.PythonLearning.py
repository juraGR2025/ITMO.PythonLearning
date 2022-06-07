from random import randint
import time
#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')
#Моделирование бросания кубика первым играющим
print('Кубик бросает', igrok1)
time.sleep(2)
nV1 = 0
nV2 = 0
for i in range(5):
    #Моделирование бросания кубика первым играющим
    n1 = randint(1, 6)
    nV1 = nV1+n1
    print('Выпало:', nV1)
#Моделирование бросания кубика вторым играющим
print('Кубик бросает', igrok2)
time.sleep(2)
for i in range(5):
    #Моделирование бросания кубика первым играющим
    n2 = randint(1, 6)
    nV2 = nV2+n2
    print('Выпало:', nV2)
#Определение результата (3 возможных варианта)
if nV1 > nV2:
    print('Выиграл', igrok1)
elif nV1 < nV2:
    print('Выиграл', igrok2)
else:
    print('Ничья')

#Обработка модулей выполняется двумя инструкциями:
#import – позволяет клиентам (импортерам) получать модуль целиком.
#from – позволяет клиентам получать определенные имена из модуля.
import math
import statistics
from random import randint
#1. С помощью справочной информации изучите состав модулей math и 
#statistics.
#print(help(math))
#print(help(statistics))
#2. Напишите программу, в которой создайте список из десяти целых чисел.
mylist = [randint(1,100) for x in range(10)]# 10 чисел, сгенерированных случайным образом в диапазоне (1, 100)
print(mylist)
#3. Затем реализуйте подсчет суммы чисел списка, среднего значения, 
#медианы (median) и стандартного отклонения (stdev), предварительно 
#импортировав соответствующие модули.
print('Summa:', sum(mylist))
print('Average value:', sum(mylist)/len(mylist))
print('Median:', statistics.median(mylist))
print('Standard deviation:', statistics.stdev(mylist))
#4. Реализуйте программу, в которой генерируется случайное число на 
#интервале от 1 до 100. Для генерации числа используйте функцию randint
#модуля random.
print('random number:', randint(1,100))



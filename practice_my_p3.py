#��������� ������� ����������� ����� ������������:
#import � ��������� �������� (����������) �������� ������ �������.
#from � ��������� �������� �������� ������������ ����� �� ������.
import math
import statistics
from random import randint
#1. � ������� ���������� ���������� ������� ������ ������� math � 
#statistics.
#print(help(math))
#print(help(statistics))
#2. �������� ���������, � ������� �������� ������ �� ������ ����� �����.
mylist = [randint(1,100) for x in range(10)]# 10 �����, ��������������� ��������� ������� � ��������� (1, 100)
print(mylist)
#3. ����� ���������� ������� ����� ����� ������, �������� ��������, 
#������� (median) � ������������ ���������� (stdev), �������������� 
#������������ ��������������� ������.
print('Summa:', sum(mylist))
print('Average value:', sum(mylist)/len(mylist))
print('Median:', statistics.median(mylist))
print('Standard deviation:', statistics.stdev(mylist))
#4. ���������� ���������, � ������� ������������ ��������� ����� �� 
#��������� �� 1 �� 100. ��� ��������� ����� ����������� ������� randint
#������ random.
print('random number:', randint(1,100))



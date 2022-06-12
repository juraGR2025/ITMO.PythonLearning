import time
# Задаем исходные данные.
n = 24
S = 0
i = 1
# Задаем список
list1 = list()
# Создаем цикл
for j in range(n+1):

    if i <= n:
        print(j)
        T = float(input('Enter the number '))
        S = S + T
        list1.append(T)
        i +=1
    else:
        time.sleep(3)
        Mid = S/(i-1)
        print('Variable Mid:',"{:8.3f}".format(Mid))
        print(list1)

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = input()
m = input()
list1 = input()
list2 = input()
list3 = set()

for i in list1:
    if i in list2:
        list3.add(i)

print(*sorted(list3))

# К сожалению, моя программа не работает с двузначными числами. Почему не смогла разобраться.


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты 
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке 
# растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из 
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий 
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

list1 = [1,2,3,4]
res = 0
for i in range(len(list1)):
    max = list1[i-1] + list1[i] + list1[i-len(list1)+1]
    if max > res:
        res = max

print(res)
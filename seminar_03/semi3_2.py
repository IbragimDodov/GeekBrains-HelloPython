# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.

list = [10, 8, 11, 777, 13, 19, 7, 3]
n = input('Введите искомое число ')
count = 0
for i in list:
    i = str(i)
    if n in i:
        print("Да есть")
        count = 1
        break
if count == 0:
    print("Отсутствует")

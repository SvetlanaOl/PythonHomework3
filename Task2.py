#Напишите программу, которая найдёт
#произведение пар чисел списка.
#Парой считаем первый и последний
#элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
i = 0
list2 = []

while i < len(list1)/2:
    k = list1[i]*list1[len(list1)-i-1]
    list2.append(k)
    i += 1
print(list2)
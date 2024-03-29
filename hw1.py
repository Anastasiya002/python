# '''''
# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# '''''
# a = int(input())
# b = (a // 100) + (a % 100 // 10) + (a % 10)
# print(f'{a} -> {b}')
# '''''
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# '''''
# summa = int(input())
# x = summa // 6
# y = 2 * 2 * x
# print(f'{summa} -> {x} {y} {x}')

# '''''
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой 
# билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
# '''''
# a = int(input())
# b = a // 1000
# c = a % 1000
# d = (b // 100) + (b % 100 // 10) + (b % 10)
# e = (c // 100) + (c % 100 // 10) + (c % 10)
# if d == e:
#     print(f'{a} -> YES')
# else:
#     print(f'{a} -> NO')

'''''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no
'''''
n = int(input())
m = int(input())
k = int(input())
if n * m < k or n * m == k:
    print(f'{n} {m} {k} -> NO')
elif k % m == 0 or k % n == 0:
    print(f'{n} {m} {k} -> YES')
else:
    print(f'{n} {m} {k} -> NO')

#Write a program that takes an integer x and determines whether a given number belongs to a specified interval.
#Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанному промежутку. 

x = int(input())
if -1 < x < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

#Write a program that takes an integer xx and determines whether this number belongs to the specified intervals.
#Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.

x = int(input())
if -9999999 <= x <= -3 or 7 <= x <= 99999999:
    print("Принадлежит")
else:
    print("Не принадлежит")

#Write a program that takes an integer xx and determines whether this number belongs to the specified intervals.
#Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.

x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")
    
#Let's call a number beautiful if it is four-digit and is divided entirely by 77 or by 1717. Write a program that determines whether the entered number
#is beautiful. The program should output "YES" if the number is beautiful, or "NO" otherwise.
#Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. Напишите программу, определяющую, является ли введённое
#число красивым. Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.

x = int(input())
if (1000 <= x <= 9999) and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")
    
#Write a program that takes three positive numbers and determines whether there is a non-degenerate triangle with such sides.
#Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

a, b, c = int(input()),  int(input()),  int(input())
if a < b + c and b < a + c and c < a + b:
    print("YES")
else:
    print("NO")

#Write a program that determines whether the year with a given number is a leap year. If the year is a leap year, then output "YES", otherwise output "NO".
#Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES», иначе выведите «NO».

x = int(input())
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("YES")
else:
    print("NO")




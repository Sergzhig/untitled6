# функция которая принимает список любой длинны, состоящий из строк и чисел,
# и из этого списка удаляет все элементы являющиеся строками.
# 1way
def del_string(L):
    for i in L:
        if type(i) == str: L.remove(i)
    return L


# 2way generator
def del_string2(L):
    return [i for i in L if type(i) != str]

print('#1')
print(del_string([1, 'DDD', 2, 3, 'gfh', 5, 5]))
print('#1-2')
print(del_string2([1, 'DDD', 2, 3, 'gfh', 5, 5]))
###############################

#функцию, принимает на вход значение n, и создает список из n чисел Фибоначчи.
def Fibonachi(n):
    if n==0:return []
    elif n==1:return [0]
    else:
        L = [0, 1]
        i = 2
        while i<n:
            L.append(L[-1]+L[-2])
            i+=1
    return L
print('#2')
print (Fibonachi(4))
################################
# функцию, принимает на вход значение n, и создает список каждый элемент которого равен квадрату своего номера.
def Square1(n):
    return [i**2 for i in range(n)]
print('#3-1')
print (Square1(5))

def Square2(n):
    i=0
    L=[]
    while i<n:
        L.append(i**2)
        i+=1
    return L
print('#3-1')
print(Square2(5))
################################
#функция, принимает на вход значение n, и создает список из n элементов. Каждый элемент это случайное число от 1 до n.
from random import randint

def Random(n):
    return [randint(1,n) for i in range(n)]
print('#4')
print(Random(5))
#################################
# функция, которая принимает на вход список, и находит сумму четных чисел этого списка.
def Sum_chetnyh(L):
    S = 0
    for i in L:
        if i % 2 == 0:
            S += i
    return S
print('#5')
print(Sum_chetnyh([4,5,6,6,5]))
###############################
#функция, которая принимает на вход список, и находит в нем наибольший элемент. (Не используя max)
def Max(L):
    n=L[0]
    i=0
    while i<len(L)-1:
        if L[i+1]>=n:
            n=L[i+1]
        i+=1
    return n
print('#6')
print (Max([5,5,56,5,5,5]))





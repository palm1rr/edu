# a = int(input('a = '))
# b = int(input('b = '))
# print(a % b)

# a = int(input('a = '))
# print(a % 10 + (a // 10) % 10 + a // 100 )

# a = int(input('a = '))
# summ = 0
# while a > 0:
#     summ += a % 10
#     a //= 10
# print(summ)

# a = int(input())
# b = [2, 3, 5, 7]
# cnt = 0
# while a > 0:
#     if a % 10 in b:
#         cnt += 1
#     a //= 10
# print(cnt)

# a = int(input())
# print(bin(a))

# a = int(input())
# b = ''
# while a > 0:
#     b += str(a % 2)
#     a //= 2
# print(b[::-1])

def my_bin(a: int) -> str:
    """ возвращает бинарную запись числа """
    b = ''
    while a > 0:
        b += str(a % 2)
        a //= 2
    return b[::-1]


# print(my_bin(10))

def convert_numb(a: int, b: int = 2) -> str:
    """
    Возвращает в виде строки число a в с.с. b

    :param a: целое неотрицательное число
    :param b: натуральное число <= 10
    :return: строка
    """
    assert a >= 0, 'вы даун а косяк'
    assert 1 < b <= 10, ' вы дебил б косяк'
    c = ''
    while a > 0:
        c += str(a % b)
        a //= b
    return c[::-1]


# print(convert_numb(256, 8))

# l = [1, 3, 4, 2, 5, 6, 1]
# maxx = l[0]
# minn = l[0]
# с помощью индексации по массиву
# for i in range(len(l)):
#     if l[i] > maxx:
#         maxx = l[i]
#     elif l[i] < minn:
#         minn = l[i]
# с помощью прохода по массиву
# for i in l:
#     if i > maxx:
#         maxx = i
#     elif i < minn:
#         minn = i
# print(minn, maxx)

def mult_min_max(a: list[int]) -> int:
    """ произведение мин макс в списке """
    maxx = a[0]
    minn = a[0]
    for i in a:
        if i > maxx:
            maxx = i
        if i < minn:
            minn = i
    return minn * maxx


l = [1, 3, 4, 2, 5, 6, 1]

print(mult_min_max(l))

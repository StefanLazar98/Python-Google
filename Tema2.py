# def my_function(list_param):
#     suma = 0
#     for i in list_param:
#         if isinstance(i, int) is True or isinstance(i, float) is True:
#             suma += i
#     return suma
#
# my_list = [1, 5, -3, 'abc', [12, 56, 'cad']]
#
# print(my_function(my_list))

# def recursive_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + recursive_sum(n-1)
#
#
# print(recursive_sum(5))

# def recursive_odd_sum(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     elif n % 2 == 0:
#         return recursive_odd_sum(n-1)
#     elif n % 2 == 1:
#         return n + recursive_odd_sum(n-2)
#
# print(recursive_odd_sum(5))

# def recursive_even_sum(n):
#     if n == 0:
#         return 0
#     elif n % 2 == 0:
#         return n + recursive_even_sum(n-2)
#     elif n % 2 == 1:
#         return recursive_even_sum(n-1)
#
# print(recursive_even_sum())


x = float(input())


def another_function(x):
    try:
        if x - int(x) != 0:
            return 0
        else:
            return int(x)
    except ValueError as e:
        print("Please insert a valid number", e)


print(another_function(x))

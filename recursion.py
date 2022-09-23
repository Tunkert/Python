# def decrementor(num):
#     start = num
#     print(start)
#     start -= 1
#     if start == 0:
#         return None
#     return decrementor(start)
#
#
# decrementor(9)
#
#
# def increment_to_100(num):
#     print(num)
#     start = num + 1
#     if start == 101:
#         return None
#     return increment_to_100(start)
#
#
# increment_to_100(9)

# def decrement_to_0(num):
#     print(num)
#     return decrement_to_0(num - 1) if num > 0 else None
#
#
# decrement_to_0(100)
#
#
# def increment_to_100(num):
#     print(num)
#     return increment_to_100(num + 1) if num < 100 else None
#
#
# increment_to_100(10)

def decrementor(top, bottom):
    if top < bottom:
        return
    print(top)
    decrementor(top - 1, bottom)


decrementor(100, 20)
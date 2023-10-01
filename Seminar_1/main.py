# 1-я задача
# n = 123
# res = 0
# while n > 0:
#     x = n % 10
#     res = res + x
#     n = n // 10
# print(res)

# 3-я задача
# n = 123456
# sum_left = 0
# sum_right = 0
# for i in range(6):
#     if i<3:
#         sum_right += n // 10**i % 10
#     else:
#         sum_left  += n // 10**i % 10 
# if sum_left == sum_right:
#     print('yes')
# else:
#     print('no')

# 4-я задача
a = 3
b = 2
c = 1
if c < b * a and ( c % b == 0 or c % a == 0):
    print('yes')
else:
    print('no')

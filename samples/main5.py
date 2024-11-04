
d = {'a':{'b':5,'c':{'d':"Hello",'e':10}},'e':[1,2,3]}

d = {
    'a': {
        'b': 5,
        'c': {
            'd': "Hello",
            'e': 10
        }
    },
    'e': [1, 2, 3]
}

flattened_dict = {}
stack = [((), d)]  # Start with an empty key path and the root dictionary

while stack:
    path, current = stack.pop()
    if isinstance(current, dict):
        for k, v in current.items():
            stack.append((path + (k,), v))
    else:
        flattened_dict[".".join(path)] = current

print(flattened_dict)







# fact=lambda n:1 if n==0 else n*fact(n-1)
# n=input('enter number')
# print('special') if int(n)==sum([fact(int(i)) for i in n]) else print('nope')

#
# for i in range(3, 0, -1):
#     for s1 in range(2,i*2):
#         print('-',end='')
#     for j in range(3, i - 1, -1):
#         print(chr(96+j), end='')
#         if j!=i:
#             print('-',end='')
#     for k in range(i+1,4):
#         print('-',end='')
#         print(chr(96+k),end='')
#     for s2 in range(2, i * 2):
#         print('-', end='')
#     print()
# for i in range(2,4):
#     for s1 in range(2,i*2):
#         print('-',end='')
#     for j in range(3,i-1,-1):
#         print(chr(96 + j), end='')
#         if j != i:
#             print('-', end='')
#     for k in range(i,3):
#         print('-',end='')
#         print(chr(97+k),end='')
#     for s2 in range(2,i*2):
#         print('-',end='')
#     print()


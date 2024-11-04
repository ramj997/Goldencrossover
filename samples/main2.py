

for i in range(2):



# def abc(n):
#     for i in range(1,n):
#         for k in range(n-1,i,-1):
#             print(' ',end=' ')
#         for j in range(1,i*2):
#             print(chr(j+64),end=' ')
#         print()
# abc(5)

# for i in range(1,6):
#     if(i%2!=0):
#         c=1
#     else:
#         c=0
#     for j in range(1,i+1):
#         print(c,end=' ')
#         c=c^1
#     print()

# def hollowDiamond(n):
#     for i in range(1,n):
#         for k in range(n-1,i,-1):
#             print(' ',end=' ')
#         for j in range(1,i*2):
#             if j==1 or j==i*2-1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()
#     for i in range(n-2,0,-1):
#         for k in range(n-1,i,-1):
#             print(' ',end=' ')
#         for j in range(1,i*2):
#             if j==1 or j==i*2-1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()
#
# hollowDiamond(5)
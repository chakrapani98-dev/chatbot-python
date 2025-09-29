# """

# *****
# *****
# *****
# *****
# *****

# define two variable one for row and column increment
# increment outer loop i from 0 to 4
# for every iteration of i loop have inner j loop print * by iterating 5 times
# process repeats till outer loop exits ,each iteration goes to second line

# for loop 5 times
#     for loop 5 times
#         print("*")
#     print("\)
    
# function(parameter)
# paremeter is a int, will take n
    
# """

# # def printStar(n:int):
# #     for x in range(n):
# #         for y in range(n):
# #             print("*",end="")
# #         print("\n")

# # printStar(7)

# """
# problem 2 :
# *
# **
# ***
# ****
# *****

# print a star
# now need to print 2 stars
# so loop number = number of stars
# so outer loop needs to increment to give inner loop range
# all stars need to print in same line and manually break at end of loop

# for loop range 5
# for loop range n
# print(*,end="")

# """
# def pyramid(n:int):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*",end="")
#         for j in range(n-i-1):
#             print(" ",end="")
#         print("\n")
    
# def revPyr(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(2*n-(2*i+1)):
#             print("*",end="")
#         for j in range(i):
#             print(" ",end="")
# def demo(n:int):
#     for i in range(1,(2*n-1)+1):
#         if(i<6):
#             for j in range(i):
#                 print("*",end="")
#             print("\n")
#         else:
#             for k in range(2*n-i):
#                 print("*",end="")
#             print("\n")


# demo(5)

# def simplepattern(n):
#     for i in range (n,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print("\n")

# simplepattern(5)

# count =0
# def func():
#     global count
#     if(count==3):
#         return
#     print(count)
#     count+=1
#     func()

# func()
# count = 1
# def numbers(n):
#     global count
#     if (count==n+1):
#         return
#     print(count)
#     count+=1
#     numbers(n)

# numbers(5)

# def revNum(n):
#     count=n
#     if(count==0):
#         return
#     print(count)
#     revNum(count-1)
# revNum(5)

# def sumOfN(n,count=0):
#     if(count>n):
#         return 0
#     return count+sumOfN(n,count+1)

# print(sumOfN(5))

def factNum(n,count=1):
    if(count>n):
        return 1
    return count*factNum(n,count+1)

print(factNum(5))






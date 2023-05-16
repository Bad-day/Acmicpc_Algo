n = int(input()); sum=0;result=0
# for i in range(1, n+1):
#     if n % i == 0:
#         sum += i
#         result = sum
# print((result*5)-24) 
sum([i for i in range(1, n+1) if n % i == 0])
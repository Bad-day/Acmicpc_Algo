n = input().strip();num_list = [0] * 10

# for i in k:
#     num_list[i] += 1
# if num_list[6] >=2 or num_list[9] >=2:
#     result=round((max(num_list)/2))
#     if num_list[6]==num_list[9]:
#         result+=1
# else:
#     result = max(num_list)
# print(result)
for i in n:
    if i == '6' or i=='9':
        if num_list[6] <= num_list[9]:
            num_list[6]+=1
        else:
            num_list[9] +=1
    else:
        num_list[int(i)] +=1
print(max(num_list))
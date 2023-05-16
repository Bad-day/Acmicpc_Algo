# def count_alphabets(k):
#     alphabet_list = [0] * 26
#     for letter in k:
#         index = ord(letter.upper()) - ord('A')
#         alphabet_list[index] += 1
#     max_count = max(alphabet_list)  # 가장 큰 수
#     max_indices = [i for i, count in enumerate(alphabet_list) if count == max_count]
#     if len(max_indices) == 1: 
#         max_letter = chr(max_indices[0] + ord('A'))
#     else: 
#         max_letter = '?'
#     return max_letter

# k = input()
# result = count_alphabets(k)
# print(result)


# 1157

word=input().upper()
di={}
for i in word:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
max_word = [k for k,v in di.items() if max(di.values()) == v]
if len(max_word)>=2:
    print('?')
else:
    print(*max_word)
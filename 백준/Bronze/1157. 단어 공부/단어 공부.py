def count_alphabets(k):
    alphabet_list = [0] * 26
    for letter in k:
        index = ord(letter.upper()) - ord('A')
        alphabet_list[index] += 1
    max_count = max(alphabet_list)  # 가장 큰 수
    max_indices = [i for i, count in enumerate(alphabet_list) if count == max_count]
    if len(max_indices) == 1: 
        max_letter = chr(max_indices[0] + ord('A'))
    else: 
        max_letter = '?'
    return max_letter

k = input()
result = count_alphabets(k)
print(result)

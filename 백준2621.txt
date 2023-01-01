import sys
def check_color(_color,_num): #2621
  check = len(set(_color))
  if check == 1:
    return True, max(_num)
  return False, -1

def check_num(_num):
  _num = sorted(_num)
#  freq = sorted([(i, _num.count(i)) for i in range(1,10)] lambda x : x[1], reverse = True))
  freq = sorted([(i, _num.count(i)) for i in range(1, 10)], 
                     key=lambda x: x[1], reverse=True)
# freq =[][]
#  if freq[0][1] == 4:
#    return 4, freq[0][0]
#  if freq[0][1] == 3:
#    if freq[1][1] == 2:
#      return 3.2, freq[0][0]*10 +freq[1][0]
#    return 3 , freq[0][0]
#  if freq[0][1] == 2:
#    if freq[1][1] == 1:
#      return 2.2, freq[1][0] * 10 + freq[0][0]
#    return 2, freq[0][0]
#  return 0, freq[4][0]
  if freq[0][1] == 4:    #4개가 같은 상황
    return 4, freq[0][0]
  if freq[0][1] == 3:
    if freq[1][1] == 2:   #3개, 2개가 같은 상황
      return 3.2, freq[0][0] * 10 + freq[1][0]
    return 3, freq[0][0] #3개만 같은 상황
  if freq[0][1] == 2:
    if freq[1][1] == 2:   #2개, 2개가 같은 상황
      return 2.2, freq[1][0] * 10 + freq[0][0]
    return 2, freq[0][0]  #2개만 같은 상황
  return 0, freq[4][0]  #같은게 없는 상황


def check_st(_num):
  _num = sorted(_num)
  check = _num[0] - 1
  for num in _num:
    if check +1 != num:
      return False, -1
    check = num
  return True, check

colors = []
numbers = []

for _ in range(5):
  c,n= input().split()
  colors.append(c)
  numbers.append(int(n))
  

same_color, same_color_value = check_color(colors, numbers)
straight, straight_value = check_st(numbers)
state, state_value = check_num(numbers)

if same_color:
    if straight:
        print(900 + straight_value)
    else:
        print(600 + same_color_value)
elif straight:
    print(500 + straight_value)
else:
    if state == 4:
        print(800 + state_value)
    if state == 3.2:
        print(700 + state_value)
    if state == 3:
        print(400 + state_value)
    if state == 2.2:
        print(300 + state_value)
    if state == 2:
        print(200 + state_value)
    if state == 0:
        print(100 + state_value)


    

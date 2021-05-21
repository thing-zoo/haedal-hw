#과제: 슬라이드 7쪽 터틀코드 수정하기
# t.shape('turtle')
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(90)
# t.right(90)
# t.forward(90)

import turtle as t

with open('text.txt', 'r') as f:
    lines = f.readlines()
    values = list(map(int, lines))

t.shape('turtle')
n = len(values)

for i in range(0, n-1, 2):
    t.forward(values[i])
    t.right(values[i+1])
    
t.forward(values[-1])
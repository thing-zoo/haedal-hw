#과제: 다이아몬드 출력하기
star = "*"
n = 9
for i in range(1, 10, 2):
    s = star*i
    blank = int((n - i)/2)*" "
    print(blank, s, blank)

for i in range(7, 0, -2):
    s = star*i
    blank = int((n - i)/2)*" "
    print(blank, s, blank)
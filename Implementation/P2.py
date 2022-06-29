#왕실의 나이트 문제
#8X8 좌표 평면, 수평으로 2칸 수직 1칸, 수직 2칸 수평1칸

input_data = input()

x=int(input_data[1])
y=ord(input_data[0])-ord('a')+1

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0

for step in steps:
    next_x=x+step[0]
    next_y=y+step[1]

    if next_x>=1 and next_x<=8 and next_y>=1 and next_y<=8:
        result+=1

print(result)

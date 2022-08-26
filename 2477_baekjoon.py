# K: 제곱미터 당 참외의 개수
K = int(input())
# 반시계 방향으로 돌면서
# 변의 방향, 길이
# 1:동, 2:서, 3:남, 4:북

# 1, 2 - 가로 방향
# 3, 4 - 세로 방향
# 가로 길이의 최대 * 세로 길이의 최대 - 가로길이의 최소 * 세로길이의 최소
width = 501     # 가로 길이 최소 값 담을 변수
height = 501    # 세로 길이 최소 값 담을 변수
sum_length = [0]*5  # 방향별 길이 누적

for _ in range(6):
    d, length = map(int, input().split())
    sum_length[d] += length
    # 지금까지 등장한 가로방향의 최소값이면 갱신
    if d == 1 or d == 2:
        if length < width:
            width = length
    # 지금까지 등장한 세로방향의 최소값이면 갱신
    else:
        if length < height:
            height = length
# 가로최대 * 세로최대 - 가로최소*세로최소
max_width = 0
if sum_length[1] < sum_length[2]:
    max_width = sum_length[2]
else:
    max_width = sum_length[1]
max_height = 0
if sum_length[3] < sum_length[4]:
    max_height = sum_length[4]
else:
    max_height = sum_length[3]

print(((max_height*max_width)-(height*width))*K)
num_switch = int(input())
# 0번인덱스 비워두고
switch = [0] + list(map(int, input().split()))
num_stu = int(input())
for _ in range(num_stu):
    g, num = map(int, input().split())
    # 남학생이라면
    if g == 1:
        for i in range(num, num_switch+1, num):
            switch[i] = 1 - switch[i]
    # 여학생이라면
    else:
        # 현재 위치 바꾸고
        switch[num] = 1 - switch[num]
        # 좌우 대칭인지 확인 후 바꾸기
        # 현재 위치부터 1번인덱스까지
        for i in range(1, num):
            if num + i <= num_switch:
                if switch[num-i] == switch[num+i]:
                    switch[num-i] = 1 - switch[num-i]
                    switch[num+i] = 1 - switch[num+i]
# 출력하기
for i in range(1, num_switch + 1):
    print(switch[i], end=" ")
print()
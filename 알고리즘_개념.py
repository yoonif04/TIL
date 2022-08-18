# bubble 정렬
arr = [1, 3, 5, 4, 2, 1]
N = len(arr)

for i in range(N - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

# 선택정렬
arr = [1, 3, 5, 4, 2, 1]
N = len(arr)
for i in range(N - 1):
    minIdx = i
    for j in range(i + 1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)

# 카운팅 정렬
arr = [1, 3, 5, 4, 2, 1, 1]
N = len(arr)
k = max(arr)
counts = [0] * (k+1)
new = [0] * len(arr)
for i in range(len(arr)):
    counts[arr[i]] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i - 1]

for i in range(len(new) - 1, -1, -1):
    counts[arr[i]] -= 1
    new[counts[arr[i]]] = arr[i]

print(new)


# 2차원 배열
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]

# 행 순회
N, M = 5, 5
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()
# 열 순회
for j in range(M):
    for i in range(N):
        print(arr[i][j], end=" ")
    print()
# 지그재그 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j)*(i%2)], end=" ")
    print()
# 델타 이용 탐색
di = [-1, 1, 0, 0]      # 상,하,좌,우
dj = [0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        for k in range(4):
            for d in range(1, 3):
                ni = i + di[k]*d
                nj = j + dj[k]*d
                if 0<=ni<N and 0<=nj<M:
                    print(ni, nj)
# 전치 행렬
for i in range(N):
    for j in range(M):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# 왼쪽 대각선 합
sum_arr = 0
for i in range(N):
    sum_arr += arr[i][i]

# 오른쪽 대각선 합
sum_arr = 0
for i in range(N):
    sum_arr += arr[i][N-1-i]

# 왼쪽 대각선의 왼쪽, 오른쪽 영역의 합
sum_left, sum_right = 0, 0
for i in range(N):
    for j in range(N):
        if i < j:
            sum_right += arr[i][j]
        elif i > j:
            sum_left += arr[i][j]
for i in range(N):
    for j in range(i+1, N):
        sum_right += arr[i][j]
        sum_left += arr[j][i]

# 같은 사선 상의 합
N = 5
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]
s = [0]*(2*N-1)
for i in range(N):
    for j in range(N):
        s[i+j] = arr[i][j]

# 부분집합의 합
arr = [1, 2, 3]
n = 3
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=" ")
    print()


# 이진검색 - 반복문 이용
def binarySearch(arr, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

def binarySearch(arr, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == arr[middle]:
            return True
        elif key < arr[middle]:
            return binarySearch(arr, low, middle-1, key)
        else:
            return binarySearch(arr, middle+1, high, key)

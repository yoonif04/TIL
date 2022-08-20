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

# 셀렉션 알고리즘
def select(arr, k):
    for i in range(k):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr[k-1]

# 카운팅 정렬
arr = [1, 3, 5, 4, 2, 1, 1]
N = len(arr)
k = max(arr)
counts = [0] * (k + 1)
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
        print(arr[i][j + (M - 1 - 2 * j) * (i % 2)], end=" ")
    print()
# 델타 이용 탐색
di = [-1, 1, 0, 0]  # 상,하,좌,우
dj = [0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        for k in range(4):
            for d in range(1, 3):
                ni = i + di[k] * d
                nj = j + dj[k] * d
                if 0 <= ni < N and 0 <= nj < M:
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
    sum_arr += arr[i][N - 1 - i]

# 왼쪽 대각선의 왼쪽, 오른쪽 영역의 합
sum_left, sum_right = 0, 0
for i in range(N):
    for j in range(N):
        if i < j:
            sum_right += arr[i][j]
        elif i > j:
            sum_left += arr[i][j]
for i in range(N):
    for j in range(i + 1, N):
        sum_right += arr[i][j]
        sum_left += arr[j][i]

# 오른쪽 대각선의 왼쪽, 오른쪽 영역의 합
sum_left, sum_right = 0, 0
for i in range(N):
    for j in range(N-1-i):
        sum_left += arr[i][j]
        sum_right += arr[N-j-1][N-i-1]

# 같은 사선 상의 합
N = 5
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]
s = [0] * (2 * N - 1)
for i in range(N):
    for j in range(N):
        s[i + j] = arr[i][j]

# 부분집합의 합
arr = [1, 2, 3]
n = 3
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=" ")
    print()


# 이진검색 - 반복문 이용
def binarySearch(arr, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

# 이진검색 - 재귀함수 이용
def binarySearch(arr, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == arr[middle]:
            return True
        elif key < arr[middle]:
            return binarySearch(arr, low, middle - 1, key)
        else:
            return binarySearch(arr, middle + 1, high, key)


# 문자열 - strlen()함수 만들기
def strlen(a):
    idx = 0
    while a[idx] != "\0":
        idx += 1
    return idx


# 문자열 뒤집기 - 자기 문자열에서 뒤집기
def reverse(s):
    list_s = list(s)
    for i in range(len(s) // 2):  # -(i+1)과 len(s)-1-i 동일
        list_s[i], list_s[-(i + 1)] = list_s[-(i + 1)], list_s[i]
    new_s = "".join(list_s)
    return new_s


# 문자열 뒤집기 - 새로운 빈 문자열 만들기
def reverse(s):
    reverse = ""
    for i in range(len(s) - 1, -1, -1):
        reverse += s[i]
    return reverse


# 문자열 - 사전 순서
# def my_strcmp(str1, str2):


# 문자열 숫자 정수로 변환
def atoi(s):
    i = 0
    for word in s:
        i = i * 10 + ord(word) - ord('0')
    return i


# 정수를 문자열로 변환
def itoa(a):
    i = 10
    s = ""
    while a > 0:
        mod = a % i
        s += chr(ord("0") + mod)
        a //= 10
    return s


# 패턴 매칭
def BruteForce(p, t):
    idx_t, idx_p = 0, 0
    while idx_t < len(t) and idx_p < len(p):
        if t[idx_t] != p[idx_p]:
            idx_t -= idx_p
            idx_p = -1
        idx_t += 1
        idx_p += 1
    if idx_p == len(p):
        return idx_t - len(p)
    else:
        return -1


# 정수론
# 최대공약수 구하기
def gcd(a, b):
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# 최소공배수
def lcm(a, b):
    return int(a * b / gcd(a, b))


# 소수 구하기
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# 에라토스테네스의 체
def get_prime(n):
    arr = [True] * (n+1)
    m = int((n+1)**0.5)
    for i in range(2, m+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = False
    return [i for i in range(2, n+1) if arr[i] == True]


# 스택 구현
# 재귀 호출
# memoization
def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]
memo = [0, 1]
print(fibo1(4))

# dp
def fibo2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[n-1] + f[n-2])
    return f[n]

# 유클리드 호제법
# 최대공약수를 쉽게 구할 수 있는 알고리즘
# 두 수 a와 b (a > b)가 있다고 할 때, 
# a와 b의 최대공약수 G는 b와 a%b(a를 b로 나눈 나머지)의 최대 공약수 G'와 서로 같다!

# gcd(24, 18) = gcd(18, 6) = gcd(6, 0)

# b가 0이 되는 순간의 6이 바로 최대공약수

# 최소공배수(lcm) : a*b/gcd(a, b)

N, M = map(int, input().split())
n, m = N, M

while m != 0:
    n = n%m
    n, m = m, n

# gcd(a, b) = n
# lcm(a, b) = N*M/n
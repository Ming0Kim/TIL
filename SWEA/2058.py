A= int(input())
B= A//1000
C= A//100 -10*B
D= A//10 - 100*B - 10*C
E = A%10
print(B+C+D+E)
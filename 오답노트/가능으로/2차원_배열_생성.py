'''
3 4

0 1 0 0

0 0 0 0
0 0 1 0
'''


n,m=map(int, input().split())

#1
mylist=[0 for _ in range(n)]

for i in range(n):
    mylist[i]=list(map(int, input().split()))


#2
mylist=[]
for i in range(n):
    mylist.append(list(map(int, input().split())))


#3
mylist=[list(map(int, input().split())) for _ in range(n)]
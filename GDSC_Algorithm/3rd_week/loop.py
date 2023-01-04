#1
N= int(input())
for i in range(1,10):
    print(N,"*",i,"=",N*i)

#2
T=int(input())
for i in range(T):
    A,B=map(int,input().split())    
    print(A+B)


#3
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))
   
#4
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])

#5
for N in range(1,int(input())+1):
    print(N)


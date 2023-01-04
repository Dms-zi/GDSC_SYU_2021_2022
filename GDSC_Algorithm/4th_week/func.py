#1
def print_love():
    print("알고리즘 사랑해")
for i in range(100):
    print_love()

#2
def print_max():
    a=int(input())
    b=int(input())
    c=int(input())
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    if b>c:
        print(b)
    else:
        print(c)

#3

def avg(*a):
    res=0
    for i in a:
        res+=i
    return res/len(a)

#4
def solution(number):
    sum=0
    for i in range(len(number)):
        if i not in number:
            sum+=i
    return sum


#5
def solve(a:list):   
    return sum(a)
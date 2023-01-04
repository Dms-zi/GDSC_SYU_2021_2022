#1
a=string.split(" ");      
print(a[4]);

#2 
a=input()
print(ord(a))

#3
def solution(n):
    li=list(str(n))
    li=list(map(int,li))
    li.sort(reverse=True)
    return li
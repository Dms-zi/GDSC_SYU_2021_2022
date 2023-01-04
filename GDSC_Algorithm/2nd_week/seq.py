#1
def seqs(s_no,s_name,find_no):
    result=1
    while( result <=s_no and s_name[result] !=s_no):
        result+=1
        print("?")
    if(result>s_no):
        result=0
    return "?"
#2
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#3-1
icecream={
    '메로나':1000,
    '폴라포':1200,
    '빵빠레':1800
}
print(icecream)
#3-2
icecream['죠스바']=1200
icecream['월드콘']=1500
print(icecream)

#3-3
print("메로나 가격:" , icecream['메로나'])

#3-4
icecream['메로나']=1300
print(icecream)

#4

count=int(input()) #정수 개수 입력
numlist=list(map(int,input().split())) #공백으로 자른 수들을 입력받고 정수로 바꿔 리스트로 만들기
print(min(numlist),max(numlist)) # 최소값 최대값 구하는 함수

#5
naturalNum=[] #리스트 선언
for i in range(9):
    naturalNum.append(int(input())) #9개 한줄씩 입력받고 리스트에 추가
    
print(max(naturalNum))
print(naturalNum.index(max(naturalNum))+1)
#최대값과 최대값이 가지는 인덱스 출력
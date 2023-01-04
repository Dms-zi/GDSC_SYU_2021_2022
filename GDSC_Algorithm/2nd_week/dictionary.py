#1
inventory={
    '메로나':[300,20],
    '비비빅':[400,3],
    '죠스바':[250,100],}

#2
print(inventory['메로나'][0],"원")

#3
print(inventory['메로나'][1],"개")

#4
inventory['월드콘']=[500,7]

#5
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
a=list(icecream.keys())
print(a)

#6
b=list(icecream.values())
print(b)

#7
sum=0
for i in icecream.values():
    sum+=i
print(sum)
    
#8
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)

#9
result={}
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
for i in range(3):
    result[keys[i]]=vals[i]
print(result)

#10
close_table={}
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
for i in range(3):
    close_table[date[i]]=close_price[i]
print(close_table)


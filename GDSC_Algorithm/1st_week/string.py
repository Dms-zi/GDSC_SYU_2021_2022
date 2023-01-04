 #1
letters='python'
print(letters[0],letters[2])

#2
license_plate="24가 2210"
print(license_plate[4:])

#3
string="홀짝홀짝홀짝"
print(string[::2])

#4
string="PYTHON"
print(string[::-1])

#5
phone_number="010-1111-2222"
NoHyphen=phone_number.replace("-"," ")
print(NoHyphen)

#6
NoHyphenVoid=phone_number.replace("-","")
print(NoHyphenVoid)

#7
url="http://sharebook.kr"
SplitKr=url.split(".")
print(SplitKr[1])

#8
#error...

#9
string='abcdfe2a354a32a'
ReplaceA=string.replace("a","A")
print(ReplaceA)

#10
#abcd
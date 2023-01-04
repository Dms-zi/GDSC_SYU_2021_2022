#1
movie_rank=["닥터스트레인지","스플릿","럭키"]

#2
movie_rank.append("배트맨")
print(movie_rank)

#3
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#4
movie_rank.remove("럭키")
print(movie_rank)

#5
del movie_rank[2:]
print(movie_rank)

#6
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)

#7
nums = [1, 2, 3, 4, 5, 6, 7]
print("max:",max(nums),'\n'"min:",min(nums))

#8
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#9
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#10
nums = [1, 2, 3, 4, 5]
avg=sum(nums)/len(nums)
print(avg)
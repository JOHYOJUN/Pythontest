a = input()
b = list(map(int,input().split()))
b.sort()

result = 0 #그룹의 수
count = 0 #사람의 수
for i in b :
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)


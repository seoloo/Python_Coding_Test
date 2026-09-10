cnt = (int)(input())

li = []
for i in range(cnt):
    tmp = (int)(input())
    li.append(tmp)

m = 0
for i in li:
    if(m < i):
        m = i

li2 = []
for i in li:
    if(i < m):
        li2.append(i / m * 100)
    elif(i == m):
        li2.append(i)

sum = 0
for i in li2:
    sum += i

print(sum / cnt)


# ----------------------------------- 정답
"""
n에 과목의 수 입력
 mylist에 점수 정보 저장
 mymax에 mylist 정보 중 최댓값 저장
 sum에 mylist 모든 데이터 값 더하기
 num * 100 / mymax / n 출력
"""
n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)
print(sum * 100 / mymax / int(n))

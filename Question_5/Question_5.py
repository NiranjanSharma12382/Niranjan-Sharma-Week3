n,m=map(int.input().split())
answers_list=[]
sum=0

for i in range(n):
    answers_list.append(input())
mark_list=[]
for l in range(m):
    mark_list.append(int(input()))
for j in range(m):    
    question_list=[]
    for k in range(n):
       count=0
       for z in range(n): 
        (question_list).append((answers_list[z])[k])
        if count==m:
            break
       sum+=
n = int(input())
lst = list(map(int,input()))
new_lst=[]
for ele in lst :
    new_lst.append(lst.index(ele)+1)
print(new_lst)


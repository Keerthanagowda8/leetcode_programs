l1=[9,9,9,9,9,9,9]
l2=[9,9,9,9]
l3=[]
if len(l1)>len(l2):
    for i in range(len(l1)-len(l2)):
        l2.append(0)
elif len(l1)<len(l2):
    for i in range(len(l2)-len(l1)):
        l1.append(0)
l1.reverse()
l2.reverse()
list1=int(''.join(map(str, l1)))
list2=int(''.join(map(str, l2)))
res=list1+list2
res2=str(res)
for i in range(len(res2)):
     l3.append(res2[i])
l3.reverse()
int_list = list(map(int, l3))
print(int_list)

# output:[8, 9, 9, 9, 0, 0, 0, 1] 


lst=[1,3,2,3,4,5,3,2]

print(len(lst))
print(lst)
st=set(lst)
print(len(st))
print(st)

if(len(lst)!=len(st)):
    print("List have duplicate elements")
else:
    print("No duplicates")



lst1=[2,3,4,4,3,2,5,6,7,5,7]

newlst1=[]
duplicate=[]

for i in lst1:
    if i not in newlst1:
        newlst1.append(i)
    else:
        duplicate.append(i)
print(newlst1)
print(duplicate)
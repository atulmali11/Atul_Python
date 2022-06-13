
#1
str="I am Atul Mali"

j=len(str)-1
rev=" "
for i in str:
    rev=i+rev
print(rev)

#2
str1="ATUL"
output=" "
output=str1[::-1]
print(output)

#3
str3="Mali"
s1=reversed(str3)
output1=''.join(s1)
print(output1)

#4
str4="ATUL MALI BHOSE"
re=''
a=len(str4)-1

while a>=0:
    re=re+str4[a]
    a=a-1
print(re)


# count of lower and upper character
str5="I Am Atul Mali"
lower=0
upper=0
i=len(str5)
for i in str5:
    if(i.islower()):
        lower=lower+1
    elif(i.isupper()):
        upper=upper+1
print(upper)
print(lower)


#second way
str6="AAAbbbCCdd"
lo=0
up=0
for s in str6:
    if(s>='a' and s<='z'):
        lo=lo+1
    elif(s>='A' and s<='Z'):
        up=up+1
print(lo)
print(up)


str6="AAAAAAAAAAAvvvvvvvvmmvvv"
lo1=0
up1=0
for s in str6:
    if(ord(s) >= 97 and ord(s) <= 122):
        lo1=lo1+1
    elif(ord(s)>= 65 and ord(s)<= 90):
        up1=up1+1
print(lo1)
print(up1)


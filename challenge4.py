score=[]
n=int(input("enter the size of the list"))
score=[0]*n
for i in range(n):
    score[i]=int(input("enter the score"))
print(score)
valid_entries=0
valid_afterpersonalization=0
invalid_entries=0
low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]
for i in range(n):
    if score[i]>=0 and score[i]<=30:
        low_risk= low_risk+[score[i]]
        valid_entries=valid_entries+1
    elif score[i]>=31 and score[i]<=60:
        medium_risk= medium_risk+[score[i]]
        valid_entries=valid_entries+1
    elif score[i]>=61 and score[i]<100:
        high_risk=high_risk+[score[i]]
        valid_entries=valid_entries+1
    elif score[i]>=100:
        critical_risk=critical_risk+[score[i]]
        valid_entries=valid_entries+1
    else:
        invalid_entries=invalid_entries+1
        print(" ")
print("before personalization")
print("low-risk",low_risk)
print("medium-risk",medium_risk)
print("high-risk",high_risk)
print("critical_risk",critical_risk)
d=int(input("enter your last three digit of your register number"))
print( "register number",d)
sum=0
while d>0:
    sum= sum+d%10
    d=d//10
print("sum of the digits",sum)
if sum%2==0:
    removed=len(medium_risk)
    medium_risk=[]

else:
    removed=len(critical_risk)
    critical_risk=[]
print("after personalization")
print("low-risk",low_risk)
print("medium-risk",medium_risk)
print("high-risk",high_risk)
print("critical-risk",critical_risk)
print("final report")

print("total valid entries",valid_entries)
print("total ignored entries",invalid_entries)
print("removved due to personalization",removed)



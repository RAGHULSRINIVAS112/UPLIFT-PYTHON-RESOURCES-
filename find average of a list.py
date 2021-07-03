mylist=[2,4,6,7,8,9]
count=0
for i in mylist:
    count+=i
#here we are using the sum function to claculate the average
sum=sum(mylist)    
avg=sum/len(mylist)
#insted of count we can also use sum butn we are using count 
print(f"sum={count}")
print(f"average of my list is{avg}")
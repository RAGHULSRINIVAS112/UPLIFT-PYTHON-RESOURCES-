mylist=[77,78,2,6,9,99]
evenlist=[]
oddlist=[]
for i in range(len(mylist)):
    if(mylist[i]%2):
        evenlist.append(mylist[i])
    else:
        oddlist.append(mylist[i]) 
print(evenlist)
print(oddlist)
print(f"there where {len(evenlist)} in the even list and there where {len(oddlist)} in the odd list")          
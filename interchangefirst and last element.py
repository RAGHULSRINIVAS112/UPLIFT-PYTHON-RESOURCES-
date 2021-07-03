#to intercshange first and last element
#first approch is to find the length of list and then swap the elements
#for that we need to take a temp variable


#swapping first and last element using temp variable -3variables
def my_function(mylist):
    temp=mylist[0]
    mylist[0]=mylist[-1]
    mylist[-1]=temp
    return mylist
#swapping using 2variables    
def myfunction(mylist):
    mylist[0],mylist[-1]= mylist[-1],mylist[0]
    return mylist
#swapping using tuple variable approach by declaring * operator fror selecting rest of the elements and the first and last elements will swap    
def myfunctionstar(mylist):
    [a,*b,c]=mylist
    mylist=[c,*b,a]
    return mylist       
#function call by declaring a new list
newlist=[1,2,3,4,5]
print(my_function(newlist)) 
newlist=[1,2,3,4,5]
print(f"print using , search methord{(myfunction(newlist))}")
newlist=[1,2,3,4,5]
print(f"print using * search methord {(myfunctionstar(newlist))}")   
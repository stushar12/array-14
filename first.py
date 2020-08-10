n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)
arr.sort()


def binary(mid):
        if((arr[mid]!=arr[mid+1]) and (mid + 1)<n):
            return  1
        elif(arr[mid]!=arr[mid-1]):
            return 2
        elif(arr[mid]==arr[n-1]):
            return -2
        else:
            return -1


lower=0
upper=n-1
while(lower<upper):
    mid=lower + (upper-lower)//2
    a=binary(mid)
    if(a==-1):
        lower=mid+1
    elif(a==-2):
        upper=mid-1
    elif(a==1):
        print(f"Element is {mid+1}")
        break
    elif(a==2):
        print(f"Element is {mid}")
        break
if(a<0):
 print("Not possible")




#function to calculate the weight to be added.
def add(d):
    c = 0
    i=0
    while c < d:
        c = c + pow(3,i)
        i += 1
    return pow(3,i-1)
#main code 
val = int(input("Enter your value: "))
LeftArr=[]
RightArr=[]

if val != 1:
    RightArr.append(val)
    summ = 0
    i=0
    #calculates the highest power of 3 that is less than or equal to the input value.
    while summ <= val:
        summ = summ + pow(3,i)
        i += 1
    LeftArr.append(pow(3,i-1))
    #checks whether the sum of the weights on the left scale is less than or greater than the sum of the weights on the right scale. 
    while (True):
        if sum(LeftArr) < sum(RightArr):
            d=sum(RightArr) - sum(LeftArr)
            k=add(d)
            LeftArr.append(k)
        
        elif sum(LeftArr) > sum(RightArr):
            d=sum(LeftArr) - sum(RightArr)
            k=add(d)
            RightArr.append(k)
       
        if  sum(LeftArr) != sum(RightArr):
                continue
        else:
            break
else:
    print(LeftArr.append(val))
    print(RightArr.append(val))

print("Left scale weights are",LeftArr)
print("Right scale weights along with the input weight are",RightArr)
import math
import csv
with open("stddev.csv") as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]    
n= len(data)   
sum=0
for i in data:
     sum=sum+float(i)
mean=sum/n
print(mean) 
sqlist= []
for i in data:
    num=int(i)-mean
    num=num**2
    sqlist.append(num)  
total=0  
for i in sqlist:
    total=total+i
sd=math.sqrt(total/n)
print(sd)

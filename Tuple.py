#Radhe Radhe
#we have a datatype whichis a collection of elements but its immutable
a=(1,2,3,4)
print(type(a))
#This will giev tuple as the datatype in output

b=(1)
print(type(b))
#This will print datatype as integer in the output as the python interpreter takes it as an integer and not a tuple.

#To give a tuple with only a single element use the following method.
c=(1,)
print(type(c))
#This will give datatype as tuple in the output

#We can have a tuple with elements of more than one datatype.
d=(1,2,3,'tunnu',"munnu",False)
print(type(d))

print(d[0]) #output->The element at the '0' index

print(d[0:4]) #output->The elements from the index '0'to '3' will be printed.

#There are some methods to work on tuples.
#1)Count->returns the total number of occurences of an element in the tuple.
#2)Index->return the index value of the first occurence if a particular element in the tuple.

#1)count
e=(1,1,1,2,3,4,5,6)
print(e.count(1)) #Output=3

print(e.count(7)) #Output=0

#2)index
print(e.index(1)) #Output=0

# print(e.index(7)) #Output=Value Error.

#Concatenation
t1=(1,2,3)
t2=(6,7,8)
t3=t1+t2
print(t3) #output->(1,2,3,6,7,8)

#repetition
rep=t1*3
print(rep) #output->(1,2,3,1,2,3,1,2,3)

#len()
print(len(t1))  # Output: 3

#min() and max()
nums = (3, 7, 1)
print(min(nums))  # Output: 1
print(max(nums))  # Output: 7

#Sum()
print(sum(nums))  # Output: 11

#tuple conversion.
lst = [1, 2, 3]
converted = tuple(lst)  
print(converted) # Output: (1, 2, 3)

#membership testing (in) and (not in)
print(2 in nums)   # Output: True
print(5 not in nums)  # Output: True

#iterating through tuple 
for item in nums:
    print(item)
    #output:1
           #2
           #3

#Tuple unacking
p=("alice",19)
name,age=p #unpacking the tuple.
print(name) #output->alice
print(age) #output->19

#nested tuples
nested = ((1, 2), (3, 4))
print(nested[0][1])  # Output: 2
#visualise this:
#nested = ((1, 2), (3, 4))
#          ├── nested[0] -> (1, 2)
#               └── nested[0][1] -> 2



#Converting tuples.
#We usually use these methods to change the values in the original tuple.
t = (1, 2, 3)
lst = list(t)
lst[0] = 100
t = tuple(lst)  # Convert back to tuple
print(t) #output->(100,2,3)

#Radhe Radhe.











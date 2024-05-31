# List
a =[1,2,3,6,78,9]

# printing list
print(a)

# list method
l1=[1,6,4,5,8,3]

l1.append(45)#used to add another no in the end of the list
print(l1)
l1.insert(4,88)#used to add 88 in index 4
print(l1)
l1.pop(2)#removes element at index 2
print(l1)
l1.remove(3)#remove 3 from the list
print(l1)
l1.reverse()#used to arrange list in decending order
print(l1)



# Set
a= {1,2,3,4,5,1}
print (type(a))
print(a)

# create an empty set 
b= set ()
print (type (b))

# adding values to an empty set 
b.add(4)
b.add(3)
b.add(5)
b.add(4)
print(b)
 
print(len(b)) # print length of set
print(b)

b.remove(5) # remove 5 from set b
print (b)



# dictionary
myDict ={
    "fast" : "in a quick manner",
    "Harry" : "a coder"
}

print(myDict['fast']) #print value of key "fast"
print(myDict['Harry']) #print value of key "harry"
print(myDict.keys()) #print the keys of dictionary
print(type(myDict.keys())) #print the type of keys of dictionary
print(list(myDict.keys()))
print(myDict.values())
# to add word in dictionary
myDict["color"] = "red"
print(myDict)
# update dictionary
myDict.update({"color": "green"})
print(myDict)



# tuples 
t=(1,2,3,4,)
t1=()#empty turples
t1=(1,)#turples with single element
print(t1)
# type of methods
t=(1,2,3,1,4,7,1,9)
print(type(t))# print data type

print (t.count(1))
print(t.index(1))#tell in which index does 1 is


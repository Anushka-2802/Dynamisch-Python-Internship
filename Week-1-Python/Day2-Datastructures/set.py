#set is unordered collection of unique items 
#set is unchangable
s={"anushka",21,"black",8080579302,21,"anushka"}
print(s) #set remove duplicate value automatically
#create empty set
name={} 
print(type(name)) #this print type dict

#for empty set use set()
name=set()
print(type(name))

#Accessing items
for value in s:
    print(value)

#methods of set
s1={'Pink','Yellow','Green','Black','Red'}
s2={'Grey','Orange','Red','Purple','Yellow'}
print("Union: ",s1.union(s2)) #Return a set containing the union of sets
print("Intersection: ",s1.intersection(s2)) # Returns a set that is the intersection of two other sets
print("Symmetric Difference: ",s1.symmetric_difference(s2)) #Returns a set with the symmetric differences of two sets
print("Difference: ",s1.difference(s2)) #Returns a set containing the difference between two or more sets
print(s1.isdisjoint(s2)) # Returns True if nO items of this set is present in another set
print(s1.issuperset(s2)) # Returns True if all items of another set is present in this set
print(s1.issubset(s2))   # Returns True if all items of this set is present in another set
s1.add("Orange") # To add item
print(s1)
s1.remove('Red')
print(s1)
item=s1.pop() #Randomly remove item
print(item)
del item #delete entire set
#print(item)





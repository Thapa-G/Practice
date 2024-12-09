#set is immutable
#no index in set
set1={"apple","apple","Banana","Cherry"}
print(set1)



set1.add("mango")

print(set1)


# update

set2={"kiwi"}
set3=["kiwi","Jackfruit"]
set1.update(set2)
print(set1)


set1.update(set3)
print(set1)

set4={1,2,3,4,5,6,7,8}
set4.remove(3)
print(set4)

set4.discard(3)
print(set4)

# pop deletes random values


set4.pop()
print(set4)

set4.pop()
print(set4)


set1={"apple","apple","Banana","Cherry"}
set1.pop()
print(set1)

# del delete varible
# clear delete content

# Join Sets


jset1={1,2,3,4}
jset2={"a","b",1}
jset5={"*","/",3,1,"a"}

# union = |


jset3=jset1.union(jset2,jset5)
print(jset3)

jset4=jset1.intersection(jset2,jset5)
print(jset4)

jset6=jset1.difference(jset2,jset5)
print(jset6)


# symmetric difference

jset7=jset1.symmetric_difference(jset2)
print(jset7)
jset8=jset1 ^ jset2
print(jset8)


# methods


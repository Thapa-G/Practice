#mutable
a=[1,2,3,4,5,6]
fruits=["apple","banana","mango","grapes"]
mix=[1,2,"aashik","mango","1.5"]

print(a[5])
print(fruits[1])

# list slicing

print(fruits[1:3])


fruits[1]="helll"
print(fruits)
fruits[1:3]=["aaashik"]
print(fruits)


fruits.insert(2,"jane")
print(fruits)




fruits.append("mango")
print(fruits)



list1=["aashik","jane"]
list2=["aashik","lang"]
list1.extend(list2)
print(list1)




mix1=[1,2,"aashik","mango","1.5",3,4,5,6,7,8]
emp_list=[]
odd_list=[]
string_odd=[]
for i in range(len(mix1)):
    if type(mix1[i])==int and mix1[i]%2==0:
           emp_list.append(mix1[i])
    elif type(mix1[i])==int and mix1[i]%2!=0:
          odd_list.append(mix1[i])
    elif type(mix1[i])==str and len(mix1[i])%2==0:
             string_odd.append(mix1[i])
          
          
print(emp_list)
print(odd_list)
print(string_odd)


[emp_list.append(mix1[i]) for i in range(len(mix1)) if type(mix1[i])==int and mix1[i]%2==0]


thislist=["apple","banana","cherry","banana"]
thislist.remove("banana")
print(thislist)


thislist.pop()
print(thislist)


del thislist[0]
print(thislist)


#delete the whole variable
# del thislist
# print(thislist)


# clear list

lsit_w=[1,2,3,4,5]
lsit_w.clear()
print(lsit_w)



list2=["apple","banana","cherry","banana","banana","apple","grapes"]
list2.remove("banana")
list2.remove("banana")
list2.remove("banana")
list2.remove("apple")
list2.remove("apple")
print(list2)

list5=["apple","banana","cherry","banana","banana","apple","grapes"]
list4=[]
for x in list5:
      if x not in list4:
            list4.append(x)
print(list4)




list3=["apple","banana","cherry","banana","banana","apple","grapes"]
count=0
for x in list3:
      if x=="apple":
            count+=1
print(count)

print(list3.count("apple"))

even_list=[]
list111=[1,2,3,4,5,6,7,8,9]

[even_list.append(x) for x in list111 if x%2==0]

list222=[]

new_list=[x if x%2==0 else list222.append(x) for x in list111]
print(new_list)
print(list222)





# list methods

fruity=["Apple","Mango","Banana","cherry"]
# popped=fruity.pop()
# print(popped)

# sort function sort the capital letter first 

fruity.sort( reverse=True)
print(fruity)

# shortedd create new list
new_list1=sorted(fruity)
print(new_list1)

# copy list
lista=[1,2,3,4]
listj=[]
listj=lista #point too same location
listj.append(5)
print(listj, lista)



listja=lista.copy() #copy content
listja.append(6)
print(listja,lista)


list31=list(lista)
print(list31)


listaa=[5,6,7,8]
listaa.extend([1,2,3])
print(listaa)


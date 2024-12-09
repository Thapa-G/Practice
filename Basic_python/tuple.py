#tuples are immutable



thistupel=("apple","banana","cherru","grapes")
y=list(thistupel)
print(y)
y[1]="kiwi"
y.insert(2,"orange")
x=tuple(y)
print(x)




# unpacking

# * creates a list and stores all of it in the red after
# second item in the tuple because yellow would store banana 
(red,yellow,*reed)=thistupel
print(red)
print(reed)
print("hey")
(red,*yellow,reed)=thistupel
print(red)
print(yellow)
print(reed)

print("-------------")
(*red,yellow,reed)=thistupel
print(red)
print(yellow)
print(reed)


fruitsa=("a","b","c")
ra=fruitsa*3
print(ra)



task=((1,2),(2,3),(5,3),(2,1))
sum=0
tuple1x=0
for x,y in task:
    if x+y > sum:
        sum=x+y
        tuple1x=(x,y)

print(sum)
print(tuple1x) 
# String are immutable



a="hey" # single line string
b="""
hey there
how are u """# multiline string 
print(a)
print(b)


# escape characters

name="hello 'world "
print(name)



hey="how are you"
print(hey[0::2])# slicing the string
# String functions


count=0
for i in hey:
    count+=1
print(count)


count1=0
for i in range(len(hey)):
    if hey[i]=="e":
        count1+=1
    print(count1)


print(hey.upper())
print(hey.lower())


for char in hey:
    if(char.lower() == "e"):
        print("e found")


#replace
# lstrip
# strip
# rstrip
# lower
# upper
# split
# join
# isdigit
# islower
# issuper
# format

s="hello,{}"
print(s.format("world"))
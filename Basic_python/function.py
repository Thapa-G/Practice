def addd(a,b):
    result=a+b
    return result

x=addd(1,2)
print(x)

# return as tuple
def get_stats(numbers):
    mina=min(numbers)
    maxa=max(numbers)
    return mina,maxa

numbers=[1,2,3,4,5,6]
result=get_stats(numbers)
print(result)



#return as list



def get_stats(numbers):
    mina=min(numbers)
    maxa=max(numbers)
    return [mina,maxa]

numbersa=[1,2,3,4,5,6,7]
result=get_stats(numbersa)
print(result)



#retun as dictionary

def get_stats(numbers):
    mina=min(numbers)
    maxa=max(numbers)
    return {
        "min":mina,
        "max":maxa
        }
numberd=[1,2,3,4,5,6,7,8]
result=get_stats(numberd)
print(result.get('mis',"notfound"))



def addition():
    a=1
    b=2
    result=a+b
    return result
x=addition()
print(x)





def adddd(c,d=0):
    result=c+d
    return result
resultaa=adddd(1)
print(resultaa)




# local and global variable
y=20
def my_f():
    x=10
    print(x,y)
my_f()


z=2

def my_global():
    global z
    z=3
    print(z)

my_global()
print(z)



def rev(word):
    temp=word
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    return rev

def palindorm(word):
    if(type(word)==str and word==word[: :-1]):
        print("Palindorme")
    elif(type(word)==int and word==rev(word)):
        print("palindrom")
    else:
        print("not palindrom")
palindorm("aa")
palindorm(11011)

def armstrong(number):
    sum=0
    temp=number
    while temp>0:
        digit=temp%10
        sum=sum+digit**2
        temp=temp//10
armstrong(153)


def palindorom(word):
    if(type(word)==str and word==word[: :-1]):
        print("Palindorme")
    elif(type(word)==int):
        ra=str(word)
        if(ra==ra[::-1]):
          print("pm")
    else:
        print("not palindrom")
        
palindorm("aa")
palindorm(11011)
palindorom(123)
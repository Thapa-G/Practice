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
result=adddd(1)
print(result)
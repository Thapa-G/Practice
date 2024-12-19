


# Arguments
def fun(*kw):

    print("the values are" + kw[0])

fun("aashik","htpa")

# kwarz arguments
def fun1(**kww):
    print(kww)

fun1(name="aashik",age=20)


# both at a time


def fun2(*kw,**kww):
    print(kw)
    print(kww)

fun2("aashik", age=20,roll=1)

# lamda function
add=lambda a,b : print(a + b)
add(1,2)






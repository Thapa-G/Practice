dictt={
    "name":"aashik",
    "age":20,
    "city":"Kathamndu"
}

print(dictt["name"])

# if marks not found then print 123
print(dictt.get("markss",123))
# print(dictt["marks"])


dictt["marks"]=95
print(dictt)



# methods in dictionary


car={
    "brand":"Ford",
    "model":"mustang",
    "year":1999
}
x=car.keys()
print(x)
# x["age"]=200
car["color"]="white"
print(x)

y=car.values()
print(y)

z=car.items()
print(z)

count=0

# for x,y in car.items():
#     print(x,y)
for x,y in car.items():
    if x=="year":
        car["year"] = 1
   
print(car)

if car.get("phone")== None:
    car["phone"]=558
print (car)





# delete

car.pop("model")
# car.popitem() delete the last inserted
del car["color"]
car.clear()


carr=car.copy()
print(carr)



# nested

my_family={}
my_family["child1"]= {
    "name":"aashik",
    "year":19999
}
my_family["child2"]={
    "name":"jane",
    "year":1990
}
print(my_family)


# my_my = {}  # Initialize the dictionary

# for x in range(3):
#     name = input("Enter the name: ")
#     age = int(input("Enter the age: "))
#     my_my[f"child{x}"] = {
#         "name": name,
#         "age": age
#     } 

# print(my_my)


# student={}
# for x in range(3):
#     name=input("name = ")
#     age=int (input("age = "))
#     marks={}
#     for y in range(1):
#         english=int(input("english ="))
#         maths=int(input("maths="))
#         science=int(input("science ="))
#         marks={
#             "english":english,
#             "maths":maths,
#             "science" : science
#              }
#         student[f"student{x}"] = {
#              "name": name,
#             "age": age,
#              "marks": marks
#      }  
            

# print(student)

student={
    'student0': {
        'name': 'Alice',
        'age': 10,
        'marks': {'english': 85, 'maths': 90, 'science': 88}
    },
    'student1': {
        'name': 'Bob',
        'age': 12,
        'marks': {'english': 78, 'maths': 82, 'science': 80}
    },
    'student2': {
        'name': 'Charlie',
        'age': 11,
        'marks': {'english': 92, 'maths': 88, 'science': 89}
    }
}

suma={}
sumas=0
for x,y in student.items():
    for z in y:
        if z=="marks":
                sumas=sum(y[z].values())
                suma[x]=sumas
print(suma)




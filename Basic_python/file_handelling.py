# f=open("input.txt","r")
# value=f.read()
# print(type(value))
# print(f.read())
# print(f.readline())
# print(f.readline())# returns string

# print uusing loop

# for  i in f:
#     print(i)

# f.close()

# print(f.readlines())# gives lsit
# f=open("input.txt","r")
# value1=f.readline()
# print(value1)

# value2=f.readline([])
# print(value2)

# value3=f.readline()
# value4=value3.rstrip("!\n")
# print(value4)

# value5=f.readlines()
# print(value5)
# first_row=value5[0]
# first_row_list=first_row.split(" ")
# print(first_row_list[1])


# ----------------append mode ---------------

# f=open("input.txt","a")
# f.write("its me")
# f.close()

# f=open("input.txt","w")
# a=["hello\n","helo"]
# f.writelines(a)
# f.close()

import os
# os.remove("input.txt")


if os.path.exists("input.txt"):
    print("yes")
else:
    print("no")


# with open("input.txt","a") as f:
#     content=f.read()
#     print(content)


data=[
    ["alice",30,"loondon"],
     ["alice",30,"loondon"],
      ["alice",30,"loondon"]
]
import csv;
file_path="data.csv"
with open(file_path,mode='w',newline='') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(['name','age','city'])
    for rows in data:
        csv_writer.writerow(rows)

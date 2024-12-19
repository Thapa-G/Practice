import csv
file_path="data.csv"
# with open(file_path,mode='r') as file:
#     csv_reader=csv.reader(file)
#     header=next(csv_reader)
#     for row in csv_reader:
#         print(row)


# with open(file_path,mode='r') as f:
#     csv_reader=csv.DictReader(f)
#     header=next(csv_reader)
#     for row in csv_reader:
#         print(row['name'],row['age',row['city']])


data=[
    {'name':'jane','age':20, 'city':'bagmati'}
]
fieldnames=['name','age','city']
with open(file_path,mode='w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
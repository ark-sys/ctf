with open("subclasses", "r") as file:
    data = file.read()

# print(str(data))
datastr=str(data).split(",")
for i in data:
    print(i+'\n')
with open("../../../Data/example.txt", "r") as file:
    content = file.read()
    print(content)



with open("../../../Data/example.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("../../../Data/output.txt", "r") as file:
    content = file.read()
    print(content)
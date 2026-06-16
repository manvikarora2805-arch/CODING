with open("lesson14\lesson15\practice.txt", "w") as f:
    f.write("coding is super easy!!")
f.close()
with open("lesson14\lesson15\practice.txt", "r") as f:
    data=f.readlines()
    print(data)
    for i in data:
        print(i.split())
f.close()
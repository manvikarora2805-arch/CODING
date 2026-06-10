file=open("lesson14\\Code.txt","r")
file2=open("lesson14\\Code2.txt","w")
d=file.readlines()
#print(d)
#for i in d:
    #print(i)
for i in d:
    if not(i.startswith("stay")):
        print(i)
        file2.write(i)
file.close()

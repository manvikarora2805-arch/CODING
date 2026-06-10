file=open("lesson14\\Code.txt","r")
print(file.read())
file.close()





file=open("lesson14\\Code.txt","w")
file.write("\n stay away from the sun, its too hot")
file.close()





file=open("lesson14\\Code.txt","a")
file.write("\n stay in the house during the afternoon")
file.close()
fruits = ["mango","banana","apple","cherry","watermelon"]
print("fuits list", fruits)

print("Total fruits :", len(fruits))
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("First three:", fruits[:3])

fruits.append("dragon fruit")
print("\nAfter adding dragon fruit:", fruits)
fruits.remove("apple")
print("After removing apple:", fruits)
fruits.sort()
print("Sorted alphabetically:", fruits)
fruits.reverse()
print("Reversed:", fruits)
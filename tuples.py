mytuple = ("Ruth",)
print(type(mytuple))
details_tuple = ("Ruth", 27, "Malindi")
print(details_tuple)

mylist = ["Bananas", "Milk", "Honey"]
my_listtuple = tuple([mylist])

print((my_listtuple[-1]))
print(details_tuple[-1])

for i in details_tuple:
    print(i)


for i in details_tuple:
    if i == "Malindi":
        print("Malindi is in the list")

if "Malindi" in details_tuple:
    print("Malindi is in the list")
else:
    print("Malindi is not in the list")

print(len(details_tuple))

fruit = ("M", "A", "R", "A", "C", "U", "J", "A")

print(fruit.count("A"))

print(fruit.index("J"))

print(tuple(list(fruit)))

tuple2 = (fruit.index("R"), fruit.index("U"))


print(fruit[tuple2[0]: tuple2[1] + 1])
print(fruit[::-1])
# When it cmes to stepping we usually do the start:stop:step
print(fruit[::2])

name, age, city = details_tuple
print(city)
print(age)
print(name)


c1, *c2, c3, c4 = fruit
print(c1)
print(c2)
print(c3)
print(c4)




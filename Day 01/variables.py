a = 20

b = 22.5

c = -9.25e+2

d = 5j

e = ([1, "apple", 3.4])

f = ((2, "banana", True))

g = ({1, "orange", "orange"})

h = ({"name": "Alice", "age": 30})

i = True
j = False
k = None

# print(type(k))

# print(h)

name = h["name"]
age = h["age"]

# print(name)
# print(age)

# concatenate strings in Python

# print(f"His name is {name} and he is {age} years old.")


gretting = "His name is {} and he is {}".format(name, age)

# print(gretting)


list_of_words = ["What", "is", "your", "name?"]

upper_case = [word.lower() for word in list_of_words]


grettingJoin = " ".join(upper_case) # " " is the separator of or gap between word

# print(grettingJoin)

text = "mAINUL"

search_term = "MAINUL"


if search_term.lower() in text.lower() :
    print("Found")
else:
    print("Not Found")


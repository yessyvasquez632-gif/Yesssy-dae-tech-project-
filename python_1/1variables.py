name = "Alice"
age = 25
# Using % operator (old style)
print("My name is %s and I'm %d years old" % (name, age))
# Using str.format()
print("My name is {} and I'm {} years old".format(name, age))
# Using f-string
print(f"My name is {name} and I'm {age} years old")

# first we need to print the usable methods from the dictionary
print(list(filter(lambda x: not x.startswith("__"), dir(dict))))

help(dict.clear)
d = {"name": "John", "age": 36}
print(f"d: {d}")
d.clear()
print(f"d: {d}")

# copy example
help(dict.copy)
d = {"name": "John", "age": 36, "address": {"city": "New York", "state": "NY"}}
d2 = d.copy()
print(f"d: {d}, d2: {d2}")
d2["name"] = "James"
d["age"] = 37
print(f"d: {d}, d2: {d2}")

help(dict.fromkeys)
d = dict.fromkeys(["name", "age", "address"], "unknown")
print(f"d: {d}")

# get example
help(dict.get)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.get('name'): {d.get('name')}")

# get saves us the trouble of writing code like this:
if "address" in d:
    print(f"d['address']: {d['address']}")
else:
    print("d['address']: unknown")

# items example
help(dict.items)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.items(): {d.items()}")
for key, value in d.items():
    print(f"{key}: {value}")
d = {"James": "Bond", "John": "Doe", "Jane": "Doe", "Jill": "Doe", "Jerry": "Seinfeld", "Lucas": "Benjamin",
     "Luke": "Skywalker", "Leia": "Skywalker", "Han": "Solo"}

# print all the values that are not Doe from the keys that do not start with J
for key, value in d.items():
    if not key.startswith("J") and value != "Doe":
        print(f"{key}: {value}", end=" | ")


# keys example
help(dict.keys)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.keys(): {d.keys()}")
for key in d.keys():  # this is the exact same thing as doing "for key in d:..."
    print(f"{key}: {d[key]}")


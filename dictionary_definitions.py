d1 = {}  # empty dictionary (pay attention, this is not a set)
print(f"d1={d1}, type(d1)={type(d1)}")
d2 = dict()  # empty dictionary, another way to create an empty dictionary
print(f"d2={d2}, type(d2)={type(d2)}")
print(f"d1 == d2: {d1 == d2}")  # True  (same value)
print(f"d1 is d2: {d1 is d2}")  # False  (not the same ID)

d1 = {"one": "unu", "two": "doi", "three": "trei"}
d2 = {"one": "ehad", "two": "shteim", "three": "shalosh"}

# this is a complex dictionary, with different types of keys and values
d3 = {1: 1, 2: 2.0, 3.0: "3", "4": 4, True: "True", None: "whatever", "James": "Bond", (1, 2, 3): "tuple"}
# but not something like this:
# d4 = {[1, 2, 3]: "list", {1: 1, 2: 2}: 7}  # TypeError: unhashable type: 'list'

# let's combine d1 and d2 into a new dictionary
ro_to_hebrew = {}
hebrew_to_ro = {}
for k, v in d1.items():
    ro_to_hebrew[v] = d2[k]
    hebrew_to_ro[d2[k]] = v
print(ro_to_hebrew)
print(hebrew_to_ro)


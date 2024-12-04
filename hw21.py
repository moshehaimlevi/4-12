# SECTION NUMBER 1:
for x in range(12, 24+1):
    print(x, end= ", ")
print()

# SECTION NUMBER 2:
for x in range(7, 31+1):
    if x % 2 != 0:
        print(x, end= ", ")
print()

# SECTION NUMBER 3:
for x in range(-20, 10+1):
    if x % 2 == 0:
        print(x, end= ", ")
print()

# SECTION NUMBER 4:
for x in range(1, 45 + 1):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz', x, end=", ")
    elif x % 3 == 0:
        print('Fizz', x, end=", ")
    elif x % 5 == 0:
        print('Buzz', x, end=", ")
print()

# SECTION NUMBER 5:
def tot_num(l1) -> list:
    total = 0
    for num in l1:
        total += num
    return [total]
l1 = [1, 3, 5, 7, 8, 1, 3, 44, 55, 66]
print(tot_num(l1))

# SECTION NUMBER 6:

m_keys = []
m_values = []

def setdefault(key: str, value: str = None) -> None:
    if key not in m_keys:
        m_keys.append(key)
        m_values.append(value)
    else:
        print(f'Key "{key}" already exists.')

def get(key: str, msg: str = None) -> str:
    if key in m_keys:
        index = m_keys.index(key)
        return m_values[index]
    else:
        return msg

def items() -> list[tuple[str, str]]:
    return list(zip(m_keys, m_values))

def keys() -> list[str]:
    return m_keys

def values() -> list[str]:
    return m_values

thisdict = {
  "id": "32424552",
  "first name": "Moshe",
  "last name": "Haim-levy",
  "age" : "23",
  "country" : "Israel",
  "city" : "Ashdod",
}

for key, value in thisdict.items():
    setdefault(key, value)

print("Items:", items())
print("Get 'name':", get('first name', 'not exist'))
print("Get 'age':", get('age', 'not exist'))
print("Keys:", keys())
print("Values:", values())

# SECTION NUMBER 7:
m_keys = []
m_values = []

def setdefault(key: str, value: str) -> None:
    if key not in m_keys:
        m_keys.append(key)
        m_values.append(value)
    else:
        print(f'Key "{key}" already exists.')

def items() -> list[tuple[str, str]]:
    return list(zip(m_keys, m_values))

def keys() -> list[str]:
    return m_keys

def values() -> list[str]:
    return m_values

def get(key: str, msg: str = None) -> str:
    if key in m_keys:
        index = m_keys.index(key)
        return m_values[index]
    else:
        return msg

our_pets = [
    {
        "animal_type": "cat",
        "names": [
            "Meowzer",
            "Fluffy",
            "Kit-Cat"
        ]
    },
    {
        "animal_type": "dog",
        "names": [
            "Spot",
            "Bowser",
            "Frankie"
        ]
    }
]

for pet in our_pets:
    setdefault(pet["animal_type"], ", ".join(pet["names"]))

print("Get 'cat':", get('cat', 'not exist'))
print("Keys:", keys())
print("Items:", items())
print("Values:", values())


















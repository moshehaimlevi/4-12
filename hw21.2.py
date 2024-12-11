######################################### SECTION NUMBER 8:
### 1:
def items() -> list[tuple[str, str]]:
    s_keys = list(student.keys())
    s_values = list(student.values())
    return list(zip(s_keys, s_values))

### 2:
def check_hobby(student, hobby):
    while hobby not in student['hobbies']:
        student['hobbies'].append(hobby)
        print(f"'{hobby}' has been added to the hobbies list.")
    else:
        print(f"'{hobby}' is already in the hobbies list.")

### 3:
def upd_stud(student):
    s_keys = list(student.keys())
    s_values = list(student.values())
    return list(zip(s_keys, s_values))

### 4:
def remo_hob(student, hobby):
    if hobby in student['hobbies']:
        student['hobbies'].remove(hobby)
        print(f"{hobby} has been erased from hobbies list.")
    else:
        print(f"{hobby} is not in the hobbies list.")

### 5: function remo_hob

### 6:
def fam_name(student):
    student['Family name '] = 'Haim-Levi'


student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}
# 1
print("Items:", items())
print("Name:", student['name'])
print("Age:", student['age'])
print("Hobbies:", ', '.join(student['hobbies']))
# 2
check_hobby(student, '8ball')
check_hobby(student, 'reading')

# 3
print("updated",upd_stud(student))

# 4
remo_hob(student, 'reading')

# 5
print(student)

# 6
fam_name(student)
print(student)


################################### SECTION NUMBER 9:
def full_list(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

full_list(matrix)

############################## SECTION NUMBER 10:

def num_of_0(matrix1):
    count = 0
    for row in matrix1:
        for num in row:
            if num == 0:
                count += 1
    return count

matrix1 = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]

print('num of zeroes:',num_of_0(matrix1))

################ SECTION NUMBER 11:
def find_dup(arr):
    count = {}
    dups = []
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    dups = [key for key, value in count.items() if value > 1]
    return dups
arr = [4, 2, 34, 4, 1, 12, 1, 4]
print('the number who duplicate:',find_dup(arr))

############### SECTION NUMBER 12: הסתבכתי פה לגמרי

def tup_length(arr: tuple) -> int:
    return len(arr)
arr = [10, "what", 23, True, "cannot", False, "coding", 5, True]

sorted_arr = sorted(arr, key=lambda num: len(str(num)))
print(f"{sorted_arr}")

##################### SECTION NUMBER 13:
def add_up(first_arr, sec_arr):
    result = []
    for i in range(len(first_arr)):
        result.append(first_arr[i] + sec_arr[i])
    return result

first_arr = [5, 8, 11]
sec_arr = [2, 1, 3]

print(add_up(first_arr, sec_arr))

################### SECTION NUMBER 14:

def is_pali(s: str) -> bool:
    return s == s[::-1]


def check_pali(first_str: str, second_str: str):
    first_result = is_pali(first_str)
    second_result = is_pali(second_str)

    print(f"Is '{first_str}' a palindrome? {first_result}")
    print(f"Is '{second_str}' a palindrome? {second_result}")


first_str = "tacocat"
second_str = "melon"

check_pali(first_str, second_str)

################ SECTION NUMBER 15:

starter = 1
while starter < 100:
    print(starter, end= ', ')
    starter *= 2

################## SECTION NUMBER 16:
big_value = 900000

while big_value > 50:
    print(f"{big_value:.2f}", end= ', ')
    big_value /= 2

#################### SECTION NUMBER 17:

def find_duplicates(arr):
    count_dict = {}
    index = 0
    while index < len(arr):
        word = arr[index]
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
        index += 1
    duplicates = []
    index = 0
    while index < len(arr):
        word = arr[index]
        if count_dict[word] > 1 and word not in duplicates:
            duplicates.append(word)
        index += 1

    return duplicates
arr = ["laptop", "miracle", "fridge", "apple", "charger", "fridge"]
print(find_duplicates(arr))

################### SECTION NUMBER 18:
def no_dupl(list2: list[str]) -> list:
    result = []
    index = 0
    count_dict = {}
    while index < len(list2):
        item = list2[index]
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
        index += 1
    for item, count in count_dict.items():
        if count > 1:
            result.append(item)
    return result

list2 = ["code", "free", "keyboard", "code", "charger", "free"]
print(no_dupl(list2))

################ SECTION NUMBER 19:
def no_dups(names):
    result = []
    index = 0
    while index < len(names):
        item = names[index]
        if item != 'Pete' and item not in result:
            result.append(item)
        index += 1
    return result
names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(no_dups(names))


########################## SECTION NUMBER 21:

def validate_name (name: str) -> bool:
    if len(name.split()) == 2:
        return True
    else:
        return False

while True:
    user_name: str = input('user name? ')
    if validate_name(user_name):
        break

age: int = int(input('age? '))
email: str = input('email? ')
import re

while True:
    user_name: str = input('user name? ')
    if re.match("w^2", user_name):
        break
    pwd: str = input('user pwd? ')
    if re.match( r"^[A-Z](?=.*[!@#$%^&*(),.?\":{}|<>])[A-Za-z\d!@#$%^&*(),.?\":{}|<>]{7,}$", pwd):
        break




























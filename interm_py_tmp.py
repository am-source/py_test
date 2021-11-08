# LISTS
myList = [1, 3, "9", "11", 5]

print(myList)

a_list = [2,4,1,6,8,3,10]
b_list = [i*i for i in a_list]
c_list = [i*i if i%2 == 1 else i+i for i in a_list]
d_list = [i*i for i in a_list if i%2 == 0]
aa_list = sorted(myList, key=int)
# use "int()" function in key to convert str to int
print(aa_list)
listt = ["annie", "Patric", "Herlad", "jaz"]
print("Pnkwdw".lower())

#basically what the key here does is specify the search input, here we say look at all inputs (individually) in uppercase and sort them
print(sorted(listt, key= lambda x : x.upper()))
print(sorted(a_list, key= lambda i :  i%3))

##############  HASKELL higher ordder func  in PY
# MAPPING (like HASKELL)     map(func, seq)
a =[1,2,3,4,5,6,7]
b = map(lambda x : x*10, a)
print(f"mapping: {list(b)}")
print([x*10 for x in a])

# FILTER   filter(func,seq)
print(f"filtering: {list(filter(lambda x: x%2 == 0, a))}")
print([x for x in a if x%2==0])

# REDUCE  (fold)    reduce(func,seq)
from functools import reduce
product_a = reduce(lambda x, xs: x+xs, a)
print(product_a)

#-----------------------------------------------------------
#JSON   dump/load vs dumps/loads : with s if its a string, no s means from a file
import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print("JSON :")
print(personJSON)

# with open("person.json", mode="w") as file:
#     json.dump(person, file, indent=4)

with open("person.json", "r") as file:
    person_loaded = json.load(file)
print("LOADED JSON: ")
print(person_loaded)


class User:

    def __init__(self, age, name, hasChildren):
        self.name = name
        self.age = age
        self.hasChildren = hasChildren

user = User("Max", 29, False)

# to serialize as JSON we need an encode function (not necessarily in class
# o for object
def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, "hasChildren": o.hasChildren, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")
# default : (Any) -> Any , for encoding here
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

###   second method for encoding custom obj into JSON
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, "hasChildren": o.hasChildren, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)

userJSONNN = UserEncoder().encode(user)
print(userJSONNN)

## decode custom obj
from json import  JSONDecoder
class UserDecoder(JSONDecoder):

    def default(self, o):
        if User.__name__ in o:
            return User(name=o["name"], age=o["age"], hasChildren=o["hasChildren"])
        return o

user_decoded = UserDecoder().decode(userJSONNN)

###------------------------------------------
# DECORATOR PATTERN
print("----------------------------")
print("DECORATOR: ")
def start_end_decorator(func):

#  we can leave it empty,  (args and kwargs is convention, not neccessary) can pass as many args and keyword args as we want
    def wrapper(*args, **kwargs):
        print("Start")
        # if we put a return here we can use the wrapper function to give sth back
        # func here also need the args and kwargs
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper
# basically do sth before the func call and then do sth else after possibly and then return the func result and wrapper


# def print_name():
#     print("John")

# print_name is now a function/var with the functionality of wrapper, so if we call the var/func we call wrapper
# print_name = start_end_decorator(print_name)

# variant 2:
@start_end_decorator
def print_name():
    print("Max")

@start_end_decorator
def add_two_num(x):
    return x+1

print_name()
print("-----------")
result = add_two_num(5)
print(result)



















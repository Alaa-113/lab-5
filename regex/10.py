import re
def camelToSnake(string):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', string).lower()

string=input("enter a string ")
newstring=camelToSnake(string)
print(f"the string {string} after turning camel_to_snake is {newstring}")
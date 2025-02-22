import re
def insert_spaces(string):
    return re.sub(r'(?<=[a-z])(?=[A-Z])',' ', string)
string=input("enter a string ")
newstring=insert_spaces(string)
print(f"the string {string} after insertting spaces is {newstring}")
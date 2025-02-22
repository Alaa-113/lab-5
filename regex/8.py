import re
def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])',string)
string=input("enter a string ")
newstring=split_at_uppercase(string)
print(f"the string {string} after splitting is {newstring}")

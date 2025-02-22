import re
def replace(string):
    pattern=r'[ ,.]'
    result = re.sub(pattern,':', string)
    return result
string=input("enter a string ")
replaced= replace(string)
print(f"the string {string} after replacement is {replaced}")

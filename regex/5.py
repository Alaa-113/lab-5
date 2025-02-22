import re
def match_pattern(string):
    pattern=r'a.*b$'#r'a[^ab]*b$' we use thi sif we want to exclude having a or b in the middle 
    if re.match(pattern,string):
        return True
    return False
string=input("enter a string ")
result=match_pattern(string)
print(result)

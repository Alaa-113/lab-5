import re
def match_pattern(string):
    pattern=r'^[a-z]+_[a-z]+$'
    if re.match(pattern,string):
        return True
    return False
string=input("enter a string")
result=match_pattern(string)
print(result)

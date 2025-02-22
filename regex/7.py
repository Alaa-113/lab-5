def snake_to_camel(string):
    strings=string.split('_')
    camel_case = strings[0] + ''.join(string.capitalize() for string in strings[1:])
    
    return camel_case
string=input("enter a string ")
newstring=snake_to_camel(string)
print(f"the string {string} after turning snakeToCamel is {newstring}")
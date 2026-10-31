# 3.
def is_isogram(string):
    string = string.lower()

    seen_letters = ""
    
    for char in string:
        if char in seen_letters:
            return False
        
        seen_letters = seen_letters + char
        
    return True

print(is_isogram("tbilisi"))

# 4.
def get_middle(s):
    length = len(s)
    middle = length // 2
    
    if length % 2 == 0:
        first_char = s[middle - 1]

        second_char = s[middle]
        
        return first_char + second_char
    else:
        return s[middle]

print(get_middle("testing"))
print(get_middle("middle"))
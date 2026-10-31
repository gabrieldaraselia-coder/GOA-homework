# 2.
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    
    result = ""
    
    for char in string_:
        if char not in vowels:
            result = result + char
            
    return result

# 3.
def is_isogram(string):
    string = string.lower()
    
    seen_letters = ""
    

    for char in string:
        if char in seen_letters:
            return False
        
        seen_letters = seen_letters + char
        
    return True

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

# 5.
def xo(s):
    s = s.lower()
    
    count_x = s.count('x')
    count_o = s.count('o')
    
    return count_x == count_o

# 6.
# ვერ გავიგე

# 7.
def friend(x):
    friends_list = []
    
    for name in x:
        if len(name) == 4:
            friends_list.append(name)
            
    return friends_list

# 8.
def reverse_words(text):
    words = text.split(' ')
    
    reversed_words = []
    

    for word in words:
        reversed_word = word[::-1]
        
        reversed_words.append(reversed_word)
        
    return ' '.join(reversed_words)

# 9.
def capitals(word):
    indices = []
    
    for i in range(len(word)):
        if word[i] == word[i].upper():
            indices.append(i)
            
    return indices

# 10.
# ვერ გავიგე
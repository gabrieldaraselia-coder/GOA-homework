# 1. 
def powers_of_two(n):
    result = [] 
    
    for i in range(n + 1):  
        power = 2 ** i     
        result.append(power)  
        
        
    return result  

# 2.
def reverse_words(s):
    words = s.split()
    
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# 3.
def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False
    
# 4.
def correct(s):
    s = s.replace("5", "S")
    s = s.replace("0", "O")
    s = s.replace("1", "I")
    return s

# 5.
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

# 6.
def odd_count(n):
    return n // 2

# 7.
def find_multiples(integer, limit):
    result = []
    current = integer
    
    while current <= limit:
        result.append(current)
        current = current + integer
        
    return result

# 8.
def solution(a, b):
    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a
        
    return short + long + short

# 9.
def is_palindrome(s):
    cleaned_string = s.lower()
    reversed_string = cleaned_string[::-1]
    
    if cleaned_string == reversed_string:
        return True
    else:
        return False

# 10.
def square_or_square_root(arr):
    result = []
    
    for number in arr:
        root = number ** 0.5
        if root % 1 == 0:
            result.append(int(root))
        else:
            result.append(number ** 2)
            
    return result
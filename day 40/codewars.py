# 1.
def positive_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            sum += arr[i] 
    return sum        

# 2.
def repeat_str(repeat, string):
    result = "" 
    for i in range(repeat):
        result += string  
    return result 

print(repeat_str(3, "hello"))  

# 3.
def remove_char(s):
    return s[1:-1]

# 4.
def square_sum(numbers):
    total = 0
    for x in numbers:
        total += x**2  

# 5.
def find_smallest_int(arr):
    return min(arr)

# 6.
def summation(num):
    return (num * (num + 1)) // 2

# 7.
def count_sheeps(sheep):
    return sheep.count(True)

# 8.
def no_space(x):
    return x.replace(" ", "")

# 9.
def litres(time):
    return int(time * 0.5)

def century(year):
    return (year - 1) // 100 + 1
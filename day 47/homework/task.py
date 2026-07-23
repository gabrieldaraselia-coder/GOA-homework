# 1.
def capitalize(s):
    even_result = ""
    odd_result = ""

    for i in range(len(s)):
        if i % 2 == 0:
            even_result = even_result + s[i].upper()
            odd_result = odd_result + s[i].lower()
        else:
            even_result = even_result + s[i].lower()
            odd_result = odd_result + s[i].upper()

    return [even_result, odd_result]

# 2.
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    sq_1 = age_1 * age_1
    sq_2 = age_2 * age_2
    sq_3 = age_3 * age_3
    sq_4 = age_4 * age_4
    sq_5 = age_5 * age_5
    sq_6 = age_6 * age_6
    sq_7 = age_7 * age_7
    sq_8 = age_8 * age_8

    
    total_sum = sq_1 + sq_2 + sq_3 + sq_4 + sq_5 + sq_6 + sq_7 + sq_8

   
    square_root = total_sum**0.5

   
    divided = square_root / 2

  
    result = int(divided)

    return result

# 3.
def even_numbers(arr, n):
    all_evens = []


    for number in arr:
        if number % 2 == 0:
            all_evens.append(number)


    while len(all_evens) > n:
        all_evens.pop(0)

    return all_evens

# 4.
def generate_shape(n):
    one_line = ""
    for i in range(n):
        one_line = one_line + "+"

    result = one_line

    for i in range(1, n):
        result = result + "\n" + one_line

    return result

# 5.
def sort_gift_code(code):
    letters = list(code)

    letters.sort()

    result = ""
    for char in letters:
        result = result + char

    return result


# 6.
def remove_duplicate_words(s):
    words = s.split(" ")

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    result = unique_words[0]

    for i in range(1, len(unique_words)):
        result = result + " " + unique_words[i]

    return result

# 7.
def words_to_marks(s):
    total_sum = 0

    for char in s:
        position = ord(char) - 96

        total_sum = total_sum + position
        
    return total_sum

# 8.
def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    result = []

    position = 1

    for letter in word:
        if letter in vowels:
            result.append(position)

        position = position + 1

    return result

# 9.
def largest_pair_sum(numbers):
    first_max = max(numbers)

    numbers.remove(first_max)

    second_max = max(numbers)

    result = first_max + second_max

    return result

# 10.
def sort_my_string(s):
    evens = ""
    odds = ""

    for i in range(len(s)):
        if i % 2 == 0:
            evens = evens + s[i]
        else:
            odds = odds + s[i]
    result = evens + " " + odds

    return result
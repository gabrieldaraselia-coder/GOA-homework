# ახსენით რას აკეთებს `return` ბრძანება ფუნქციაში და მოიყვანეთ მარტივი მაგალითი.
# აბრუნებს პასუხს მაგალითად
def number(number1, number2):
    result = number1 + number2
    return result
n = number(23, 56)
print(n)

# შექმენით ფუნქცია `greet()`, რომელიც აბრუნებს (return) ტექსტს: `"Hello, World!"`. გამოიძახეთ ფუნქცია და დაპრინტეთ შედეგი.
def greet():
    word = "Hello, World!"
    return word
print(greet())

# შექმენით ფუნქცია `square(number)`, რომელიც აბრუნებს რიცხვის კვადრატს. შეამოწმეთ რამდენიმე მნიშვნელობაზე.
def square(number):
    number_square = number ** 2
    return number_square
print(square(30))

# შექმენით ფუნქცია `add(a, b)`, რომელიც აბრუნებს ორი რიცხვის ჯამს. მომხმარებელს შემოატანინეთ ორი რიცხვი და გამოიყენეთ ფუნქცია.
def add(a, b):
    result = a + b
    return result
print(add(int(input("Enter number here: ")), int(input("Enter number here: "))))

# შექმენით ფუნქცია `is_even(number)`, რომელიც აბრუნებს `True`-ს თუ რიცხვი ლუწია და `False`-ს თუ კენტია.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
result = is_even(15)
print(result)

# შექმენით ფუნქცია `count_vowels(text)`, რომელიც აბრუნებს სტრინგში ხმოვანი ასოების რაოდენობას.
def count_vowels(text):
    text = str(text)
    text = text.upper()
    vowels = "AEIOU"
    count = 0
    for word in (text):
        if word in vowels:
            count = count + 1
    return count
print(count_vowels("gamarjoba"))
# 7) შექმენით ფუნქცია `largest(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს ყველაზე დიდ ელემენტს.
def largest_word(numbers):
    largest = 0
    for i in range(len(numbers)):
        if len(numbers) > largest:
            largest = numbers[i]
    return(largest)
print(largest_word([7, 3, 4]))


# 8) შექმენით ფუნქცია `sum_list(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს ყველა ელემენტის ჯამს.
def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total
total_numbers = sum_list(34,67,90)
print(total_numbers)


# 9) შექმენით ფუნქცია `count_letter(text, letter)`, რომელიც აბრუნებს რამდენჯერ გვხვდება კონკრეტული ასო სტრინგში.
def count_letter(text, letter):
    count = 0
    text = text.lower()
    letter = letter.lower
    for word in text:
        if word == letter:
            count = count + 1
    return count
total = count_letter("gabo", "o")
print(total)


# 10) შექმენით ფუნქცია `filter_even(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს მხოლოდ ლუწი რიცხვების სიას.
def filter_even(numbers): 
    even = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even.append(numbers[i])
    return even
even = filter_even(12, 34, 68, 90)
print(even)


# 11) მომხმარებელს შემოატანინეთ სახელი. შექმენით ფუნქცია `format_name(name)`, რომელიც აბრუნებს სახელს title ფორმატში (პირველი ასო დიდი, დანარჩენი პატარა).
def format_name(name):
    name = name.title()
    return name
Name = input("Enter your name here: ")
name = format_name(Name)
print(name)


# 13) შექმენით ფუნქცია `remove_duplicates(numbers)`, რომელიც მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც დუბლიკატები აღარ იქნება.
# მაგალითი: 
# [1, 2, 2, 3, 1, 4] → [1, 2, 3, 4]
def remove_duplicates(numbers): 
    list = []
    for i in range(len(numbers)): 
        if numbers[i] not in list:
            list.append(numbers[i])
    return list
# 14) შექმენით ფუნქცია `second_largest(numbers)`, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს მეორე ყველაზე დიდ რიცხვს.
# მაგალითი:
# [4, 7, 2, 9, 5] → 7
# 18) შექმენით ფუნქცია `count_occurrences(numbers, target)`, რომელიც მიიღებს სიას და რიცხვს.
# ფუნქციამ უნდა დააბრუნოს რამდენჯერ გვხვდება ეს რიცხვი სიაში.
# `count()` მეთოდის გამოყენება აკრძალულია.
# 19) შექმენით ფუნქცია `merge_lists(list1, list2)`, რომელიც მიიღებს ორ სიას და დააბრუნებს ახალ სიას, სადაც ჯერ იქნება პირველი სიის ელემენტები, შემდეგ კი მეორე სიის ელემენტები.
# # ამისთვის არ გამოიყენოთ `+` ოპერატორი და არც `.extend()` მეთოდი.
# 20) შექმენით ფუნქცია `analyze_numbers(numbers)`, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სიას შემდეგი მონაცემებით:
# - ყველაზე დიდი რიცხვი
# - ყველაზე პატარა რიცხვი
# - ელემენტების ჯამი
# - ელემენტების რაოდენობა
# - საშუალო არითმეტიკული
# მაგალითი:
# [4, 8, 2, 6] # argument
# შედეგი:
# [8, 2, 20, 4, 5] # result
# ესენი ვერ გავიგე
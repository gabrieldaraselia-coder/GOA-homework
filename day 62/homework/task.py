# შექმენით ფუნქცია get_even_numbers, რომელიც მიიღებს რიცხვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს მხოლოდ ლუწ რიცხვებს და დააბრუნეთ იგი.
def get_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


# შექმენით ფუნქცია get_positive_numbers, რომელიც მიიღებს რიცხვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს მხოლოდ დადებით რიცხვებს და დაბეჭდეთ იგი.
def get_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    print(positive_numbers)


# შექმენით ფუნქცია square_numbers, რომელიც მიიღებს რიცხვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, სადაც თითოეული რიცხვი ჩანაცვლებული იქნება მისი კვადრატით და დააბრუნეთ ახალი list.
def square_numbers(numbers):
    squared = [num**2 for num in numbers]
    return squared


# შექმენით ფუნქცია get_long_words, რომელიც მიიღებს სიტყვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს მხოლოდ იმ სიტყვებს, რომელთა სიგრძეც 5-ზე მეტია და დაბეჭდეთ იგი.
def get_long_words(words):
    long_words = [word for word in words if len(word) > 5]
    print(long_words)


# შექმენით ფუნქცია double_numbers, რომელიც მიიღებს რიცხვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, სადაც თითოეული რიცხვი გაორმაგებული იქნება და დააბრუნეთ იგი.
def double_numbers(numbers):
    doubled = [num * 2 for num in numbers]
    return doubled


# შექმენით ფუნქცია get_odd_numbers, რომელიც მიიღებს რიცხვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს მხოლოდ კენტ რიცხვებს.
def get_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers


# შექმენით ფუნქცია word_lengths, რომელიც მიიღებს სიტყვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს თითოეული სიტყვის სიგრძეს და დაბეჭდეთ იგი.
def word_lengths(words):
    lengths = [len(word) for word in words]
    print(lengths)


# შექმენით ფუნქცია get_numbers_greater_than, რომელიც მიიღებს რიცხვების list-ს და რიცხვს limit. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს მხოლოდ იმ რიცხვებს, რომლებიც limit-ზე მეტია და დააბრუნეთ იგი.
def get_numbers_greater_than(numbers, limit):
    result = [num for num in numbers if num > limit]
    return result


# შექმენით ფუნქცია positive_squares, რომელიც მიიღებს რიცხვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს მხოლოდ დადებითი რიცხვების კვადრატებს.
def positive_squares(numbers):
    result = [num**2 for num in numbers if num > 0]
    return result


# შექმენით ფუნქცია get_even_squares, რომელიც მიიღებს რიცხვების list-ს. List comprehension-ის გამოყენებით შექმენით ახალი list, რომელიც შეიცავს მხოლოდ ლუწი რიცხვების კვადრატებს და დაბეჭდეთ იგი.
def get_even_squares(numbers):
    even_squares = [num**2 for num in numbers if num % 2 == 0]
    print(even_squares)


# შექმენით ფუნქცია filter_students, რომელიც მიიღებს მოსწავლეების dictionary-ს, სადაც key არის მოსწავლის სახელი, ხოლო value — მისი ქულა. List comprehension-ის გამოყენებით შექმენით მოსწავლეების სახელების list, რომელთა ქულაც 50-ზე მეტია და დააბრუნეთ იგი.
# ვერ გავიგე


# შექმენით ფუნქცია get_expensive_products, რომელიც მიიღებს პროდუქტების dictionary-ს, სადაც key არის პროდუქტის სახელი, ხოლო value — ფასი. List comprehension-ის გამოყენებით შექმენით პროდუქტების სახელების list, რომელთა ფასიც 100-ზე მეტია.
# ვერ გავიგე
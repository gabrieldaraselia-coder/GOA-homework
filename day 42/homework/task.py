# 1) ახსენით რა არის `tuple` და რით განსხვავდება ის `list`-ისგან.
# tuple არის კორტეჟი და მისი შეცვლა არ შეიძლება ხოლო list-ის შეცვლა შეიძლება

# 2) მოიფიქრეთ, რომელ რეალურ სიტუაციებში გამოიყენებდით `tuple`-ს `list`-ის ნაცვლად.
# tuple-ს იმ დროს გამოვიყენებდი როცა არ მინდა რომ შემთხვევით რამე დავამატო მიმდევრობაში

# 3) შექმენით ფუნქცია first_and_last(items), რომელიც მიიღებს `tuple`-ს და დააბრუნებს ახალ `tuple`-ს, რომელიც შეიცავს მხოლოდ პირველ და ბოლო ელემენტს.
def first_and_last(items):
    return (items[0], items[-1])

print(first_and_last(("gabo", "cat", "dog", "car")))

# 4) შექმენით ფუნქცია middle_element(items), რომელიც მიიღებს კენტსიგრძიან tuple-ს და დააბრუნებს მის შუა ელემენტს.
def middle_element(items):
    first, middle, last = items
    return middle

print(middle_element(("cat", "dog", "car")))

# 5) შექმენით ფუნქცია count_occurrences(items, value), რომელიც მიიღებს tuple-ს და ნებისმიერ მნიშვნელობას, შემდეგ კი დააბრუნებს რამდენჯერ გვხვდება ეს მნიშვნელობა tuple-ში. არ გამოიყენოთ count() მეთოდი.
def count_occurrences(items, value):
    count = 0  
    for item in items:  
        if item == value: 
            count = count + 1  
    return count  

print(count_occurrences((1, 2, 3), 2))


# 6) შექმენით ფუნქცია contains_duplicates(items), რომელიც მიიღებს tuple-ს და დააბრუნებს True, თუ მასში რომელიმე ელემენტი მეორდება, წინააღმდეგ შემთხვევაში კი False.
def contains_duplicates(items):
    seen_items = []  
    for item in items:  
        if item in seen_items:  
            return True 
        seen_items.append(item)  
    return False  

print(contains_duplicates((1, 2, 3, 4)))    
print(contains_duplicates((1, 2, 3, 1))) 



# 7) შექმენით ფუნქცია swap_edges(items), რომელიც მიიღებს მინიმუმ ორი ელემენტისგან შემდგარ tuple-ს და დააბრუნებს ახალ tuple-ს, სადაც პირველი და ბოლო ელემენტები ადგილებს გაცვლიან.
def swap_edges(items):
    return items[-1:] + items[1:-1] + items[:1]

print(swap_edges((1, 2, 3, 4, 5)))  
     

# 8) მოიძიეთ ინფორმაცია index() მეთოდზე და შექმენით ფუნქცია first_position(items, value), რომელიც დააბრუნებს გადაცემული მნიშვნელობის პირველ ინდექსს.
def first_position(items, value):
    if value in items:
        return items.index(value)
    return -1

my_tuple = ("gabo", "dog", "car", "cat")
print(first_position(my_tuple, "dog"))  
print(first_position(my_tuple, "gabo"))  

# 9) შექმენით ფუნქცია tuple_summary(numbers), რომელიც მიიღებს რიცხვების tuple-ს და დააბრუნებს შემდეგი ფორმატის ტექსტს:
# "რაოდენობა: X | ჯამი: Y | პირველი: A | ბოლო: B"
def tuple_summary(numbers):
    if not numbers:
        return "typle is empty"
        
    რაოდენობა = len(numbers)
    ჯამი = sum(numbers)
    პირველი = numbers[0]
    ბოლო = numbers[-1]

    return f"რაოდენობა: {რაოდენობა} | ჯამი: {ჯამი} | პირველი: {პირველი} | ბოლო: {ბოლო}"
my_numbers = (10, 20, 30, 40, 50)
print(tuple_summary(my_numbers))

# 10) შექმენით ფუნქცია reverse_tuple(items), რომელიც მიიღებს tuple-ს და დააბრუნებს მის შებრუნებულ ვერსიას. გამოიყენეთ slicing
def reverse_tuple(items):
    return items[::-1]

print(reverse_tuple((10, 20, 30, 40)))
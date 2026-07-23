# 1) ახსენით რა არის set და რა არის მისი მთავარი განსხვავება list-ისა და tuple-ისგან.
# Set არის პითონის მონაცემთა სტრუქტურა, რომელიც ინახავს უნიკალური ელემენტების კოლექციას.

# 2) მოიფიქრეთ, რომელ რეალურ სიტუაციებში გამოიყენებდით set-ს, სადაც მნიშვნელობების გამეორება დაუშვებელია.
#როცა გვინდა უნიკალური ელემენტების კოლექციის შექმნა

# 3) შექმენით ფუნქცია add_fruit(fruits, fruit), რომელიც მიიღებს set-ს და ერთ ხილს, შემდეგ კი დაამატებს მას add() მეთოდის გამოყენებით და დააბრუნებს განახლებულ set-ს.
def add_fruit(fruits, fruit):
    fruits.add(fruit)
    return fruits

# 4) შექმენით ფუნქცია merge_sets(first, second), რომელიც მიიღებს ორ set-ს, გააერთიანებს მათ update() მეთოდის გამოყენებით და დააბრუნებს შედეგს.
def merge_sets(first, second):
    first.update(second)
    return first

# 5) შექმენით ფუნქცია remove_color(colors, color), რომელიც მიიღებს set-ს და ფერს, შემდეგ კი წაშლის მას remove() მეთოდის გამოყენებით.
def remove_color(colors, color):
    colors.remove(color)
    return colors

# 6) შექმენით ფუნქცია safe_remove(numbers, value), რომელიც მიიღებს set-ს და რიცხვს, შემდეგ კი წაშლის მას ისე, რომ შეცდომა არ წარმოიშვას, თუ ელემენტი არ არსებობს.
def safe_remove(numbers, value):
    numbers.discard(value)
    return numbers

# 7) შექმენით ფუნქცია remove_random(items), რომელიც მიიღებს set-ს, წაშლის ერთ შემთხვევით ელემენტს pop() მეთოდის გამოყენებით და დააბრუნებს წაშლილ ელემენტს.
def remove_random(items):
    if items:
        return items.pop()
    return -1

# 8) შექმენით ფუნქცია clear_set(items), რომელიც მიიღებს set-ს, გაასუფთავებს მას clear() მეთოდის გამოყენებით და დააბრუნებს ცარიელ set-ს.
def clear_set(items):
    items.clear()
    return items

# 9) შექმენით ფუნქცია copy_set(items), რომელიც მიიღებს set-ს, შექმნის მის ასლს copy() მეთოდის გამოყენებით და დააბრუნებს ახალ set-ს.
def copy_set(items):
    return items.copy()

# 10) შექმენით ფუნქცია unique_letters(text), რომელიც მიიღებს ტექსტს და დააბრუნებს set-ს, რომელიც შეიცავს მხოლოდ უნიკალურ სიმბოლოებს.
def unique_letters(text):
    return set(text)

# 11) შექმენით ფუნქცია common_elements(first, second), რომელიც მიიღებს ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს მხოლოდ ორივე set-ში არსებულ ელემენტებს
#   - არ გამოიყენოთ სეტის მეთოდები!!!(no intersection).
# ვერ გავიგე

# 12) შექმენით ფუნქცია all_unique(numbers), რომელიც მიიღებს list-ს და დააბრუნებს True-ს, თუ ყველა ელემენტი განსხვავებულია, წინააღმდეგ შემთხვევაში კი False.
#   - გამოიყენეთ set.
# ვერ გავიგე

# 13) შექმენით ფუნქცია unique_digits(number), რომელიც მიიღებს მთელ რიცხვს და დააბრუნებს set-ს, რომელიც შეიცავს ამ რიცხვის ყველა უნიკალურ ციფრს.
# ვერ გავიგე
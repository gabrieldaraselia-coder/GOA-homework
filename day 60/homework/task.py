# შექმენით ფუნქცია get_student_grade, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. get() მეთოდის გამოყენებით მიიღეთ მითითებული მოსწავლის ქულა და დაბეჭდეთ იგი. თუ მოსწავლე dictionary-ში არ არსებობს, დაბეჭდეთ Student not found.
def get_student_grade(students_dict, student_name):
    grade = students_dict.get(student_name)

    
    if grade == None:
        print("Student not found")
    else:
        print(grade)



students = {
    "Gio": 95, 
    "Nika": 80, 
    "Lasha": 88}

get_student_grade(students, "Gio")  
get_student_grade(students, "Dato")  

# შექმენით ფუნქცია get_product_price, რომელიც მიიღებს პროდუქტების dictionary-ს და პროდუქტის სახელს. get() მეთოდის გამოყენებით მოძებნეთ პროდუქტის ფასი. თუ პროდუქტი არ არსებობს, დააბრუნეთ 0.
def get_product_price(product_dict, product_name):
    price = product_dict.get(product_name)

    if price == None:
            print(0)
    else:
        print(price)

products = {
     "bread":1,
     "water":3,
     "meat":30
} 

print(get_product_price(products,"bread"))
print(get_product_price(products,"apple"))

# შექმენით ფუნქცია remove_student, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. pop() მეთოდის გამოყენებით წაშალეთ მითითებული მოსწავლე dictionary-დან და დაბეჭდეთ მისი ქულა. თუ მოსწავლე არ არსებობს, დაბეჭდეთ Student not found.
def remove_student(students_d, student_n):
    remove = students_d.pop(student_n, None)

    if remove == None:
        print("Student not found")
    else:
        print(remove)

students = {
    "Gio": 95, 
    "Nika": 80, 
    "Lasha": 88}

remove_student(students, "Gio")  
remove_student(students, "Dato")  


# შექმენით ფუნქცია remove_last_item, რომელიც მიიღებს ნებისმიერ dictionary-ს. popitem() მეთოდის გამოყენებით წაშალეთ dictionary-ის ბოლო დამატებული ელემენტი და დაბეჭდეთ წაშლილი key და value.
def remove_last_item(my_dict):
    key, value = my_dict.popitem()

    print(f"Removed Key: {key}")
    print(f"Removed Value: {value}")


students = {"Ana": 95, "Giorgi": 80, "Lasha": 88}

remove_last_item(students)
print("Updated dictionary:", students)

# შექმენით ფუნქცია remove_items_until_empty, რომელიც მიიღებს dictionary-ს. while ციკლისა და popitem() მეთოდის გამოყენებით სათითაოდ წაშალეთ ყველა ელემენტი dictionary-დან და ყოველ ჯერზე დაბეჭდეთ წაშლილი ელემენტი.
def remove_items_until_empty(my_dict):
    while my_dict:
        key, value = my_dict.popitem()
        print(f"Removed: {key} = {value}")

data = {"a": 1, "b": 2, "c": 3}
remove_items_until_empty(data)

# შექმენით ფუნქცია clear_cart, რომელიც მიიღებს კალათის dictionary-ს, სადაც key არის პროდუქტის სახელი, ხოლო value — რაოდენობა. clear() მეთოდის გამოყენებით გაასუფთავეთ კალათა და დაბეჭდეთ საბოლოო dictionary.
def clear_cart(cart):
    cart.clear()
    print(cart)

shopping_cart = {"apple": 3, "milk": 1, "bread": 2}
clear_cart(shopping_cart)

# შექმენით ფუნქცია copy_students, რომელიც მიიღებს მოსწავლეების dictionary-ს. copy() მეთოდის გამოყენებით შექმენით მისი ასლი და დააბრუნეთ ახალი dictionary.
def copy_students(students_dict):
    new_students = students_dict.copy()
    return new_students


original_students = {"Ana": 95, "Giorgi": 80}
copied_students = copy_students(original_students)

print("Original:", original_students)
print("Copied:", copied_students)

# შექმენით ფუნქცია update_copy, რომელიც მიიღებს პროდუქტების dictionary-ს. copy() მეთოდის გამოყენებით შექმენით dictionary-ის ასლი. ასლში შეცვალეთ ერთი პროდუქტის ფასი და შემდეგ დაბეჭდეთ როგორც ორიგინალი dictionary, ასევე მისი ასლი. შეამოწმეთ შეიცვალა თუ არა ორიგინალი.
def update_copy(products):
    products_copy = products.copy()
    
    products_copy["apple"] = 2.5
    
    print("Original dictionary:", products)
    print("Copied dictionary:", products_copy)

items = {"apple": 1.5, "banana": 2.0}
update_copy(items)


# შექმენით ფუნქცია safe_remove, რომელიც მიიღებს dictionary-ს და key-ს. ჯერ get() მეთოდის გამოყენებით შეამოწმეთ არსებობს თუ არა ეს key. თუ არსებობს, pop() მეთოდის გამოყენებით წაშალეთ იგი და დაბეჭდეთ მისი value. წინააღმდეგ შემთხვევაში დაბეჭდეთ Key not found.
def safe_remove(my_dict, key):
    value = my_dict.get(key)
    
    if value == None:
        print("Key not found")
    else:
        removed_value = my_dict.pop(key)
        print("Removed value:", removed_value)


data = {"a": 10, "b": 20}
safe_remove(data, "a")  
safe_remove(data, "z") 


# შექმენით ფუნქცია copy_and_clear, რომელიც მიიღებს dictionary-ს. copy() მეთოდის გამოყენებით შექმენით მისი ასლი, შემდეგ clear() მეთოდის გამოყენებით გაასუფთავეთ ორიგინალი dictionary. დაბეჭდეთ ორივე dictionary და შეადარეთ შედეგები.
def copy_and_clear(my_dict):
    dict_copy = my_dict.copy()
    my_dict.clear()
    
    print("Original (cleared):", my_dict)
    print("Copy (saved):", dict_copy)

numbers = {"one": 1, "two": 2}
copy_and_clear(numbers)


# შექმენით ფუნქცია manage_students, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. get() მეთოდით მოძებნეთ მოსწავლე. თუ მისი ქულა 50-ზე ნაკლებია, pop() მეთოდით წაშალეთ იგი dictionary-დან. თუ მოსწავლე არ არსებობს, დაბეჭდეთ Student not found.
def manage_students(students_dict, student_name):
    grade = students_dict.get(student_name)
    
    if grade == None:
        print("Student not found")
    elif grade < 50:
        students_dict.pop(student_name)
        print(f"Removed {student_name} because grade is under 50.")
    else:
        print(f"{student_name} stays with grade {grade}.")


students = {"Ana": 90, "Giorgi": 40}
manage_students(students, "Giorgi")  
manage_students(students, "Lasha")   


# შექმენით ფუნქცია backup_dictionary, რომელიც მიიღებს dictionary-ს. copy() მეთოდის გამოყენებით შექმენით სარეზერვო ასლი. შემდეგ clear() მეთოდით გაასუფთავეთ ორიგინალი dictionary. დააბრუნეთ სარეზერვო ასლი.
def backup_dictionary(my_dict):
    backup = my_dict.copy()
    my_dict.clear()
    return backup

user_data = {"username": "alex", "role": "admin"}
saved_backup = backup_dictionary(user_data)

print("Original user_data:", user_data)  
print("Returned backup:", saved_backup)  
# ახსენით რა არის dictionary-ში key, value და item. მოიყვანეთ თითოეულის მაგალითი.
# Key - უნიკალური დასახელება, რომლითაც ვპოულობთ მნიშვნელობას.
# მაგალითი - "name"
# Value - გასაღებზე მიბმული მონაცემი 
# მაგალითი - "Zaza"
# Item - გასაღებისა და მნიშვნელობის ერთობლიობა.
# მაგალითი - "name": "Zaza"

# შექმენით ფუნქცია student_info, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს მასში არსებული ელემენტების რაოდენობას.
def student_info(student):
    return len(student)

print(student_info(student={
    "name": "Gabrieli",
    "surname": "daraselia"
}))


# შექმენით ფუნქცია get_student_name, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს "name" key-ის შესაბამის value-ს.
def get_student_name(student):
    return student["name"]

print(get_student_name(student={
    "name": "Gabrieli",
    "surname": "daraselia"
}))


# შექმენით ფუნქცია get_student_age, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს "age" key-ის შესაბამის value-ს.
def get_student_age(student):
    return student["age"]

print(get_student_age(student={
    "name": "Gabrieli",
    "surname": "daraselia",
    "age": 13   
}))

# შექმენით ფუნქცია count_products, რომელიც მიიღებს პროდუქტების dictionary-ს და დააბრუნებს მასში არსებული პროდუქტების რაოდენობას.
def count_products(products):
    return len(products)

print(count_products(products={
    "products": "bread",
    "products1": "milk",
    "products2": "meat",
    "products3": "water"
}))


# შექმენით ფუნქცია get_price, რომელიც მიიღებს პროდუქტების dictionary-ს და პროდუქტის სახელს და დააბრუნებს შესაბამის ფასს.
# 1. ჯერ ვწერთ თავად ფუნქციას
def get_price(products, product_name):
    return products[product_name]

my_products = {
    "meat": 50,
    "bread": 10,
    "water": 3
}

price = get_price(my_products, "meat")
print(price)


# შექმენით ფუნქცია create_student, რომელსაც ექნება name, lastname, age, weight, height, grades, passed_test პარამეტრები. თქვენმა ფუნქციამ უნდა შექმნას dict შესაბამისი key-value ებით.
def create_student(name, lastname, age, weight, height, grades, passed_test):
    student = {
        "name": name,
        "lastname": lastname,
        "age": age,
        "weight": weight,
        "height": height,
        "grades": grades,
        "passed_test": passed_test
    }
    return student


new_student = create_student("Zaza", "Dumbadze", 16, 78.5, 1.78, [9, 10, 8, 10], True)
print(new_student)


# შექმენით ფუნქცია print_student, რომელიც მიიღებს მოსწავლის dictionary-ს, რომელსაც ექნება name, lastname, age, weight, height, grades, passed_test გასაღებები.
#   - თქვენმა ფუნქციამ უნდა დაპრინტოს მოსწავლის შესახებ ინფორმაცია შემდეგი ფორმატით:
  
# -- Student Info --
# Name: Zaza
# Lastname: Dumbadze
# Age: 16
# Weight: 78.5
# Height: 1.78
# Grades: 9, 10, 8, 10, 9, 10, 10
# Passed_test: True 
# --- -- -- -- -- --- 
# ვერ გავიგე
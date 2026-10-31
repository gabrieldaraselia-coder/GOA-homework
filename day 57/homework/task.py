# 1) შექმენით ფუნქცია print_students, რომელიც მიიღებს მოსწავლეების dictionary-ს. dictionary-ში key იყოს მოსწავლის სახელი, ხოლო value — მისი ქულა. ციკლის გამოყენებით დაბეჭდეთ ყველა მოსწავლის სახელი და ქულა. თუ ქულა 50-ზე მეტია, დაბეჭდეთ "Passed", წინააღმდეგ შემთხვევაში — "Failed". გამოიყენეთ items() მეთოდი.
def print_students(students):
    for name, score in students.items():
        if score > 50:
            print(name, "-", score, "Passed")
        else:
            print(name, "-", score, "Failed")

# 2) შექმენით ფუნქცია count_passed_students, რომელიც მიიღებს მოსწავლეების dictionary-ს, სადაც key არის მოსწავლის სახელი, ხოლო value — მისი ქულა. ციკლისა და if-ის გამოყენებით დათვალეთ რამდენმა მოსწავლემ მიიღო 50 ან მეტი ქულა. გამოიყენეთ items() მეთოდი.
def count_passed_students(students):
    count = 0
    for name, score in students.items():
        if score >= 50:
            count = count + 1  # დამწყებები ხშირად ასე წერენ += 1-ის ნაცვლად
    return count

# 3) შექმენით ფუნქცია find_expensive_products, რომელიც მიიღებს პროდუქტების dictionary-ს, სადაც key არის პროდუქტის სახელი, ხოლო value — ფასი. ციკლის გამოყენებით დაბეჭდეთ მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია. გამოიყენეთ items() მეთოდი.
def find_expensive_products(products):
    for name, price in products.items():
        if price > 100:
            print(name, "-", price)

# 4) შექმენით ფუნქცია change_low_prices, რომელიც მიიღებს პროდუქტების dictionary-ს. ციკლის გამოყენებით შეამოწმეთ ყველა პროდუქტის ფასი. თუ ფასი 20-ზე ნაკლებია, შეცვალეთ იგი 20-ით. გამოიყენეთ items() მეთოდი.
def change_low_prices(products):
    for name, price in products.items():
        if price < 20:
            products[name] = 20
    return products

# 5) შექმენით ფუნქცია check_student_data, რომელიც მიიღებს მოსწავლის dictionary-ს და ციკლის გამოყენებით შეამოწმებს მის key-ებს. თუ dictionary-ში არის "name", "age" და "grade" key-ები, დაბეჭდეთ "Complete", წინააღმდეგ შემთხვევაში — "Incomplete". გამოიყენეთ keys() მეთოდი.
def check_student_data(student):
    has_name = False
    has_age = False
    has_grade = False
    
    for key in student.keys():
        if key == "name":
            has_name = True
        if key == "age":
            has_age = True
        if key == "grade":
            has_grade = True
            

    if has_name == True and has_age == True and has_grade == True:
        print("Complete")
    else:
        print("Incomplete")

# 6) შექმენით ფუნქცია count_adults, რომელიც მიიღებს ადამიანების dictionary-ს, სადაც key არის სახელი, ხოლო value — ასაკი. ციკლის გამოყენებით დათვალეთ რამდენი ადამიანია 18 წლის ან უფროსი. გამოიყენეთ values() მეთოდი.
def count_adults(people):
    count = 0
    for age in people.values():
        if age >= 18:
            count = count + 1
    return count

# 7) შექმენით ფუნქცია find_student, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. ციკლის გამოყენებით მოძებნეთ ეს სახელი. თუ არსებობს, დაბეჭდეთ მისი ქულა, ხოლო თუ არ არსებობს - "Student not found". გამოიყენეთ keys() მეთოდი.
def find_student(students, search_name):
    found = False
    for key in students.keys():
        if key == search_name:
            print("Score:", students[key])
            found = True
            
    if found == False:
        print("Student not found")

# 8) შექმენით ფუნქცია remove_failed_students, რომელიც მიიღებს მოსწავლეების dictionary-ს, სადაც key არის სახელი, ხოლო value - ქულა. ციკლის გამოყენებით იპოვეთ ყველა მოსწავლე, რომლის ქულაც 40-ზე ნაკლებია და წაშალეთ ისინი dictionary-დან.
def remove_failed_students(students):
    names_to_remove = []
    
    for name, score in students.items():
        if score < 40:
            names_to_remove.append(name)
            
    for name in names_to_remove:
        del students[name]
        
    return students
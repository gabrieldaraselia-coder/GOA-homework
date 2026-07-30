# 1) ახსენით რა განსხვავებაა union, intersection, difference და symmetric_difference მეთოდებს შორის.
# union - ეძებს უნიკალურ ელემენტებს

# intersection - ეძებს საერთო ელემენტებს

# difference - ეზებს იმ ელემეტებს რომელიც ეკუთვნის მარტო პირველ სიმრავლეს

# symmetric_difference - ეძებს იმ ელემეტებს რომელიც საერთო არაა ორ სიმრავლეს შორის

# 2) შექმენით ფუნქცია merge_students, რომელიც მიიღებს მოსწავლეების სახელების ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს ორივე ჯგუფის ყველა მოსწავლეს.
def merge_students(group1, group2):
    return group1.union(group2)

# 3) შექმენით ფუნქცია common_courses, რომელიც მიიღებს ორი მოსწავლის კურსების set-ებს და დააბრუნებს მხოლოდ იმ კურსებს, რომლებსაც ორივე მოსწავლე სწავლობს.
def common_courses(student1_courses, student2_courses):
    return student1_courses.intersection(student2_courses)

# 4) შექმენით ფუნქცია only_first, რომელიც მიიღებს ორ set-ს და დააბრუნებს იმ ელემენტებს, რომლებიც მხოლოდ პირველ set-შია.
def only_first(set1, set2):
    return set1.difference(set2)

# 5) შექმენით ფუნქცია different_hobbies, რომელიც მიიღებს ორი ადამიანის ჰობების set-ებს და დააბრუნებს იმ ჰობებს, რომლებიც მხოლოდ ერთ-ერთ ადამიანს აქვს.
def different_hobbies(hobbies1, hobbies2):
    return hobbies1.symmetric_difference(hobbies2)

# 6) შექმენით ფუნქცია all_colors, რომელიც მიიღებს თბილი და ცივი ფერების ორ set-ს და დააბრუნებს ყველა უნიკალურ ფერს.
def all_colors(warm_colors, cold_colors):
    return warm_colors.union(cold_colors)

# 7) შექმენით ფუნქცია shared_friends, რომელიც მიიღებს ორი მომხმარებლის მეგობრების set-ებს და დააბრუნებს მათ საერთო მეგობრებს.
def shared_friends(friends1, friends2):
    return friends1.intersection(friends2)

# 8) შექმენით ფუნქცია absent_students, რომელიც მიიღებს ყველა მოსწავლისა და გაკვეთილზე მყოფი მოსწავლეების set-ებს და დააბრუნებს გაცდენილი მოსწავლეების set-ს.
def absent_students(all_students, present_students):
    return all_students.difference(present_students)

# 9) შექმენით ფუნქცია unique_products, რომელიც მიიღებს ორი მაღაზიის პროდუქტების set-ებს და დააბრუნებს იმ პროდუქტებს, რომლებიც მხოლოდ ერთ-ერთ მაღაზიაში იყიდება.
def unique_products(store1, store2):
    return store1.symmetric_difference(store2)

# 10) შექმენით ფუნქცია combine_three_sets, რომელიც მიიღებს სამ set-ს და დააბრუნებს მათში არსებულ ყველა უნიკალურ ელემენტს.
def combine_three_sets(set1, set2, set3):
    first_step = set1.union(set2)
    final_result = first_step.union(set3)
    return final_result

# 11) შექმენით ფუნქცია common_in_three, რომელიც მიიღებს სამ set-ს და დააბრუნებს მხოლოდ იმ ელემენტებს, რომლებიც სამივე set-ში გვხვდება.
def common_in_three(set1, set2, set3):
    first_step = set1.intersection(set2)
    final_result = first_step.intersection(set3)
    return final_result

# 12) შექმენით ფუნქცია first_only_words, რომელიც მიიღებს ორ ტექსტს, თითოეულს გადააქცევს სიტყვების set-ად და დააბრუნებს იმ სიტყვებს, რომლებიც მხოლოდ პირველ ტექსტში გვხვდება.
def first_only_words(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    return words1.difference(words2)

# 13) შექმენით ფუნქცია different_letters, რომელიც მიიღებს ორ ტექსტს და დააბრუნებს იმ უნიკალურ სიმბოლოებს, რომლებიც მხოლოდ ერთ-ერთ ტექსტში გვხვდება.
def different_letters(text1, text2):
    chars1 = set(text1)
    chars2 = set(text2)
    
    return chars1.symmetric_difference(chars2)
# 14) შექმენით ფუნქცია has_common_element, რომელიც მიიღებს ორ set-ს და დააბრუნებს True-ს, თუ მათ ერთი საერთო ელემენტი მაინც აქვთ, წინააღმდეგ შემთხვევაში კი False-ს.
def has_common_element(set1, set2):
    common = set1.intersection(set2)
    
    if len(common) > 0:
        return True
    else:
        return False
    
# 15) შექმენით ფუნქცია are_disjoint, რომელიც მიიღებს ორ set-ს და დააბრუნებს True-ს, თუ მათ არცერთი საერთო ელემენტი არ აქვთ, წინააღმდეგ შემთხვევაში კი False-ს.
def are_disjoint(set1, set2):
    common = set1.intersection(set2)

    if len(common) == 0:
        return True
    else:
        return False
    
# 16) შექმენით ფუნქცია exclusive_count, რომელიც მიიღებს ორ set-ს და დააბრუნებს იმ ელემენტების რაოდენობას, რომლებიც მხოლოდ ერთ-ერთ set-ში გვხვდება.
def exclusive_count(set1, set2):
    exclusive_elements = set1.symmetric_difference(set2)
    
    return len(exclusive_elements)

# 17) შექმენით ფუნქცია missing_permissions, რომელიც მიიღებს საჭირო უფლებებისა და მომხმარებლის უფლებების set-ებს და დააბრუნებს იმ უფლებებს, რომლებიც მომხმარებელს აკლია.
def missing_permissions(required_permissions, user_permissions):
    return required_permissions.difference(user_permissions)

# 18) შექმენით ფუნქცია common_numbers, რომელიც მიიღებს ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს ორივე set-ში არსებულ რიცხვებს.
#     - არ გამოიყენოთ სეტის მეთოდები!!! no intersection.
#     - გამოიყენეთ ციკლი და პირობა.
# ვერ გავიგე

# 19) შექმენით ფუნქცია analyze_sets, რომელიც მიიღებს ორ set-ს და დააბრუნებს tuple-ს ოთხი შედეგით:
#     - ყველა უნიკალური ელემენტი.
#     - საერთო ელემენტები.
#     - მხოლოდ პირველ set-ში არსებული ელემენტები.
#     - მხოლოდ ერთ-ერთ set-ში არსებული ელემენტები.

def analyze_sets(set1, set2):
    union_result = set1.union(set2)                             
    intersection_result = set1.intersection(set2)               
    difference_result = set1.difference(set2)                   
    sym_diff_result = set1.symmetric_difference(set2)          
    
    return (union_result, intersection_result, difference_result, sym_diff_result)
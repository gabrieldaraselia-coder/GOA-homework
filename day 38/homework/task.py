# 1) აღსენით დღეს ნასწავლი 3 ფუნქცია: `min()`, `max()`, `sum()`
# min - პოულობს ყველაზე პატარა რიცხვებს
# max - პოულობს ყველაზე დიდ რიცხვებს
# sum - აჯამებს რიცხვებს
# 2) მოიფიქრეთ თუ როგორ გამოიყენებთ მათ პრაქტიკაში
list = [12, 35, 68, 98, 3]
print(min(list), max(list), sum(list))
# 3) შექმენით ფუნქცია `max_difference(numbers)`, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სხვაობას ყველაზე დიდ და ყველაზე პატარა ელემენტს შორის.
# მაგალითი:
# [8, 3, 15, 6] -> 12
# გამოიყენეთ `max()` და `min()` ფუნქციები.
list = [8, 3, 15, 6]
def max_difference(numbers):
    max_val = max(numbers)
    min_val = min(numbers)
    max_minus_min = max_val - min_val
    return max_minus_min

tottal = max_difference(list)
print(tottal)
# 4) შექმენით ფუნქცია `unique_characters(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს სიას იმ სიმბოლოებისგან, რომლებიც ტექსტში მხოლოდ ერთხელ გვხვდება.
# მაგალითი:
# "banana" -> ["b", "n"]
# ვერ გავიგე

# 5) შექმენით ფუნქცია `highest_char(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს იმ სიმბოლოს, რომელსაც ყველაზე დიდი char code აქვს.
# მაგალითი:
# "Az9" → "z"
# გამოიყენეთ `max()` ფუნქცია.
def highest_char(text):
    return max(text)

print(highest_char("Az9"))

# 6) შექმენით ფუნქცია `numbers_summary(numbers)`, რომელიც მიიღებს რიცხვების სიას და **დააბრუნებს** შემდეგი ფორმატის ტექსტს:
# მაგალითი:
# [5, 10, 15]
# შედეგი:
# "რაოდენობა: 3 | ჯამი: 30 | მინიმალური: 5 | მაქსიმალური: 15"
def numbers_summary(numbers):
    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return f"რაოდენობა: {count} | ჯამი: {total} | მინიმალური: {minimum} | მაქსიმალური: {maximum}"


result = numbers_summary([5, 10, 15])
print(result)
    
        
# 7) მოიძიეთ ინფორმაცია `ord()` ფუნქციაზე და შექმენით ფუნქცია `char_code_sum(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს მის ყველა სიმბოლოს char code-ების ჯამს.
# მაგალითი:
# "ABC" -> 198
def char_code_sum(text):
    total_sum = 0
    for char in text:
        total_sum += ord(char)
    return total_sum

print(char_code_sum("ABC")) 
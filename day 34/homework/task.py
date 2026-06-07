# რა არის ფუნქცია? ახსენით საკუთარი სიტყვებით.
# ფუნქცია არის მოქმედება ომელიც გვიადვილებს კოდის წერას,ჩევნ შეგვიძლია ერთი ფუნქცია ბევრჯერ გამოვიყენოთ

# რატომ არის ფუნქციები საჭირო პროგრამირებაში? - ჩამოწერეთ მინიმუმ 3 მიზეზი
# 1.რომ კოიდს წერა გავიადვილოთ
# 2.custom function რომ შევქმნათ
# 3.გამართული კოდი რომ შევქმნათ

# რა არის პარამეტრი
# პარამეტრი არის უმნიშვნელო მნივნელობა

# რა არის არგუმენტი 
# პარაგრაფს მიცემული მნიშვნელობა

            # პარამეტრი
# def number(number1):
#     if number1 % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
                    # არგუმენტი
# number(int(input("enter number1 here: ")))

# რა განსხვავებაა პარამეტრსა და არგუმენტს შორის?
# პარამეტრს მნიშვნელობა არ აქვს ხოლო არგუმენტს კი


# შექმენით ფუნქცია repeat_word(word, count).
# - ფუნქციამ count-ჯერ უნდა დაბეჭდოს `word`
# - გამოიყენეთ for ციკლი
def repeat_word(word, count):
    for i in range(count):
        print(word)
repeat_word("gabrieli", 3)


# შექმენით ფუნქცია print_numbers(start, end).
# - ფუნქციამ უნდა დაბეჭდოს ყველა რიცხვი start-დან end-მდე
def print_numbers(start, end):
    for i in range(start, end):
        print(i)
print_numbers(1, 10)


#  შექმენით ფუნქცია count_even(numbers).
# - პარამეტრად მიიღოს სია
# - დაითვალოს რამდენი ლუწი რიცხვია სიაში
# - გამოიტანოს შედეგი
# def count_even(numbers):
#     count = 0
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == 0:
#             count = count + 1
#     print("ლუწი = ", str(count))



# შექმენით ფუნქცია count_vowels(text).
# - პარამეტრად მიიღოს სტრინგი
# - დაითვალოს რამდენი ხმოვანია ტექსტში
# - გამოიტანოს შედეგი
def count_vowels(text):
    text = str(text)
    text = text.upper()
    vowels = "AEIOU"
    count = 0
    for word in (text):
        if word in vowels:
            count = count + 1
    print(count)
count_vowels("gamarjoba")


# შექმენით ფუნქცია longest_word(words).
# - პარამეტრად მიიღოს სიტყვების სია
# - გამოიტანოს ყველაზე გრძელი სიტყვა
def longest_word(words):
    longest = ""
    for i in range(len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
    print(longest)
longest_word(["gamarjoba", "madagaskar", "hi"])


#  შექმენით ფუნქცია filter_long_words(words, n).
# - პარამეტრად მიიღოს წინადადება
# - გამოიტანოს მხოლოდ ის სიტყვები, რომელთა სიგრძე n-ზე მეტია
def filter_long_words(words, n):
    list = words.split()
    for i in range(len(list)):
        if len(list[i]) > n:
            print(list[i])


# მომხმარებელს შემოატანინეთ რამდენიმე სახელი ერთი სტრინგის სახით (მაგ: "nika luka ana gio").
# - split მეთოდით გადააქციეთ სიად
# - შექმენით ფუნქცია name_lengths(names)
# - ფუნქციამ თითოეული სახელის გვერდით უნდა დაბეჭდოს მისი სიგრძე
names = str(input("Enter names here: "))
names = names.split
def name_lengths(names):
    for i in range(len(names)):
        print(names[i] + " " + str(len(names[i])))


# შექმენით ფუნქცია find_max(numbers).
# - პარამეტრად მიიღოს რიცხვების სია
# - ციკლის გამოყენებით იპოვოს ყველაზე დიდი რიცხვი
def find_max(numbers):
    largest = numbers[1]
    for i in range(len(numbers)):
        if largest < numbers[i]:
            largest= numbers[i]
    print(largest)


#  შექმენით ფუნქცია find_min(numbers).
# - პარამეტრად მიიღოს რიცხვების სია
# - ციკლის გამოყენებით იპოვოს ყველაზე პატარა რიცხვი
def find_min(numbers):
    smallest = numbers[1]
    for i in range(len(numbers)):
        if smallest > numbers[i]:
            smallest= numbers[i]
    print(smallest)

#  შექმენით ფუნქცია remove_duplicates(numbers).
# - პარამეტრად მიიღოს სია
# - შექმნას ახალი სია დუბლიკატების გარეშე
# - გამოიტანოს შედეგი
# ვერ გავიგე


# მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13").
# - split() მეთოდით დაყავით ელემენტებად
# - გადააქციეთ integer-ებად
# - შექმენით ფუნქცია `analyze_numbers(numbers)`
# - ფუნქციამ უნდა:
#   - გამოიტანოს ჯამი
#   - გამოიტანოს საშუალო არითმეტიკული
#   - გამოიტანოს ყველაზე დიდი რიცხვი
#   - გამოიტანოს ყველაზე პატარა რიცხვი
#   - დაითვალოს ლუწი რიცხვების რაოდენობა
# ეს ვერ გავიგე
# # ახსენით რას აკეთებს lower მეთოდი და მოიყვანეთ მაგალითი
# # აპატარავებს ასოებს
# name = "GABRIELI"
# print(name.lower())


# # შექმენით სტრინგი დიდი ასოებით. lower მეთოდის გამოყენებით გადააკეთეთ ყველა ასო პატარად და დაპრინტეთ შედეგი
# pet = "DOG"
# print(pet.lower())


# # ახსენით რას აკეთებს upper მეთოდი და მოიყვანეთ მაგალითი
# # ადიდებს ასოებს
# name = "gabrieli"
# print(name.upper())


# # მომხმარებელს შემოატანინეთ სიტყვა. upper მეთოდის გამოყენებით გადააკეთეთ ეს სიტყვა დიდ ასოებად
# word = input("enter your word here: ")
# print(word.upper())


# # ახსენით რას აკეთებს title მეთოდი და მოიყვანეთ მაგალითი
# # ადიდებს პირველ ასოს
# name = "gabrieli"
# print(name.title())


# # შექმენით სტრინგების სია. გამოიყენეთ title მეთოდი თითოეულ სტრინგზე
# # ეს ვერ გავიგე


# # შექმენით სტრინგი. count მეთოდის გამოყენებით დაითვალეთ რამდენჯერ გვხვდება კონკრეტული ასო
# name = "gabrieli"
# print(name.count("a"))


# # მომხმარებელს შემოატანინეთ წინადადება და ერთი სიმბოლო. count მეთოდის გამოყენებით გაიგეთ რამდენჯერ გვხვდება ეს სიმბოლო წინადადებაში
# word = input("Enter word and symbol here: ")
# symbol = input("Enter symbol: ")
# print(word.count(symbol))



# # მომხმარებელს შემოატანინეთ სახელი და გვარი. title მეთოდის გამოყენებით სწორ ფორმატში დაპრინტეთ ორივე.
# name_surname = input("Enter name and surname here: ")
# print(name_surname.title())


# მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც). დათვალეთ ხმოვნების რაოდენობა.
vowels = 0
string = input("Enter your word here: ")
lower = string.lower()
for i in range(len(lower)):
    if lower[i] == "a":
        vowels = vowels + 1
    elif lower[i] == "e":
        vowels = vowels + 1
    elif lower[i] == "i":
        vowels = vowels + 1
    elif lower[i] == "o":
        vowels = vowels + 1
    elif lower[i] == "u":
        vowels = vowels + 1
print(vowels, "ხმოვნების რაოდენობა")


# მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც).
#   - გაიგეთ დიდი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ პატარა ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ ხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ თანხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ სფეისების პროცენტული რაოდენობა სტრინგში
sentence = input("Enter your sentence here: ")
lenght = len(sentence)
lower = 0
upper = 0
vowels = 0
consonants = 0
space = 0
for i in range(lenght):
    if sentence[i] == sentence[i].upper():
        upper = upper + 1
    else:
        lower = lower + 1
    if sentence[i] in "aAeEiIoOuU":
        vowels = vowels + 1
    else:
        consonants = consonants + 1
    if sentence[i] == " ":
        space = space + 1
print(lower / lenght * 100) 
print(upper / lenght * 100) 
print(vowels / lenght * 100) 
print(consonants/ lenght * 100) 
print(space / lenght * 100)
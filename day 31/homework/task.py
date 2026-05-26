# შექმენით სტრინგი ზედმეტი სფეისებით დასაწყისში და ბოლოში. strip მეთოდის გამოყენებით მოაშორეთ ზედმეტი სფეისები
string = "         gabriel daraselia    "
print(string.strip())


# მომხმარებელს შემოატანინეთ სახელი ზედმეტი სფეისებით. მოაშორეთ ზედმეტი სფეისები და დაპრინტეთ შედეგი
string = "         giorgi tordia    "
print(string.strip())


# მომხმარებელს შემოატანინეთ სიტყვა. შეამოწმეთ იწყება თუ არა "A" ასოთი startswith მეთოდის გამოყენებით
word = input("Enter your word here: ")
print(word.startswith("A"))


# მომხმარებელს შემოატანინეთ ვებსაიტის მისამართი. შეამოწმეთ იწყება თუ არა "https"-ით
website_adress = input("Enter website adress here: ")
print(website_adress.startswith("https"))


# მომხმარებელს შემოატანინეთ ფაილის სახელი. შეამოწმეთ მთავრდება თუ არა .py-ზე endswith მეთოდის გამოყენებით
file = input("Enter file name here: ")
print(file.endswith(".py"))


# მომხმარებელს შემოატანინეთ ელფოსტა. შეამოწმეთ მთავრდება თუ არა "@gmail.com"-ზე
email = input("Enter your email here: ")
print(email.endswith("@gmail.com"))


# შექმენით ტექსტი. `replace()` მეთოდის გამოყენებით შეცვალეთ სიტყვა "dog" სიტყვით "cat"
text = "dog"
print(text.replace("dog", "cat"))


# მომხმარებელს შემოატანინეთ წინადადება. ყველა სფეისი შეცვალეთ "-" სიმბოლოთი
sentence = input("Enter your sentence here: ")
print(sentence.replace(" ", "-"))


# მომხმარებელს შემოატანინეთ ტელეფონის ნომერი ფორმატით "599-12-34-56". replace მეთოდის გამოყენებით წაშალეთ ყველა "-" სიმბოლო
phone_number = "599-12-34-56"
print(phone_number.replace("-", " "))


# მომხმარებელს შემოატანინეთ ტექსტი ზედმეტი სფეისებით. ჯერ strip მეთოდით მოაშორეთ ზედმეტი სფეისები, შემდეგ შეამოწმეთ იწყება თუ არა ტექსტი "Hello" სიტყვით
text = "   Hello my name is gabrieli       "
print(text.strip())
print(text.startswith("Hello"))


# მომხმარებელს შემოატანინეთ პაროლი. შეამოწმეთ:
# - იწყება თუ არა დიდი ასოთი
# - მთავრდება თუ არა ციფრით "1"
password = input("Enter password here: ")
print(password.startswith("A"))
print(password.endswith("1"))


# მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - მოაშოროს ზედმეტი სფეისები
# - ყველა სფეისი შეცვალოს "_" სიმბოლოთი
# - შეამოწმოს მთავრდება თუ არა "." სიმბოლოზე
# - თუ არ მთავრდება, ბოლოში დაამატოს "."
user = input("Enter sentence here: ")
words = user.strip()
sentence = words.replace(" ", "_")
if sentence.endswith("") != sentence.endswith("."):
    sentence = sentence + "."
print(sentence)

# მომხმარებელს შემოატანინეთ სრული სახელი (სახელი, გვარი, მამის სახელი). `split()` მეთოდის გამოყენებით:
# - ცალ-ცალკე გამოიტანეთ თითოეული ნაწილი
# - დაითვალეთ რამდენი სიტყვაა შეყვანილ ტექსტში
word = 0
name = input("Enter your name here: ")
split = name.split()
for i in range(len(name)):
    if name[i] == "a":
        word = word + 1
    elif name[i] == "s":
        word = word + 1
    elif name[i] == "d":
        word = word + 1
    elif name[i] == "f":
        word = word + 1
    elif name[i] == "g":
        word = word + 1
    elif name[i] == "h":
        word = word + 1
    elif name[i] == "j":
        word = word + 1
    elif name[i] == "k":
        word = word + 1
    elif name[i] == "l":
        word = word + 1
    elif name[i] == "q":
        word = word + 1
    elif name[i] == "w":
        word = word + 1
    elif name[i] == "e":
        word = word + 1
    elif name[i] == "r":
        word = word + 1
    elif name[i] == "t":
        word = word + 1
    elif name[i] == "y":
        word = word + 1
    elif name[i] == "u":
        word = word + 1
    elif name[i] == "i":
        word = word + 1
    elif name[i] == "o":
        word = word + 1
    elif name[i] == "p":
        word = word + 1
    elif name[i] == "z":
        word = word + 1
    elif name[i] == "x":
        word = word + 1
    elif name[i] == "c":
        word = word + 1
    elif name[i] == "v":
        word = word + 1
    elif name[i] == "b":
        word = word + 1
    elif name[i] == "n":
        word = word + 1
    elif name[i] == "m":
        word = word + 1
    else:
        word = word + 0
print(name, word)
print(split)
# მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - დაყოს ტექსტი სიტყვებად
# - გამოიტანოს ყველაზე გრძელი სიტყვა
# - გამოიტანოს ყველაზე მოკლე სიტყვა
sentence = input("Enter sentence here: ")
split = sentence.split()
min = len(split[0])
max = len(split[0])
for i in range(len(split)):
    if len(split[i]) > max:
        max = len(split[i])
    if len(split[i]) < min:
        min = len(split[i])
print(min)
print(max)


#  მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13"). split მეთოდის გამოყენებით:
# - გადააქციეთ ისინი integer-ებად
# - იპოვეთ ჯამი
# - იპოვეთ ყველაზე დიდი და ყველაზე პატარა რიცხვი
string = input("Enter your numbers: ")
spilt = string.split()
list = []
for i in range(len(spilt)):
    list.append(int(spilt[i]))
print(list)
jami = 0
for i in range(len(list)):
    jami = jami + list[i]
print(jami)
min = list[0]
max = list[0]
for i in range(len(list)):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]
print(min)
print(max)
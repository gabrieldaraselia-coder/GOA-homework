# 1) მომხმარებელს მოთხოვეთ რაიმე წინადადება და რაიმე სიტყვა. გაიგეტ იწყება თუ არა ეს წინადადება ამ სიტყვით
# 2) მომხმარებელს მოთხოვეთ რაიმე წინადადება და რაიმე სიტყვა. გაიგეტ მთავრდება თუ არა ეს წინადადება ამ სიტყვით
word = input("Enter word here: ")
words = input("Enter words here: ")
print(word.startswith("words"))

word = input("Enter word here: ")
words = input("Enter words here: ")
print(word.endswith("words"))

# 3) მომხმარებელს მოთხოვეთ რაიმე ჩამოთვალოს თავისი საყვარელი ფერები(input ით). გამოიყენეთ split მეთოდი და დაპრინტეთ მიღებული სია 
favourite_colors = input("Enter your favourite colors: ")
print(favourite_colors.split())

# 4) მომხმარებელს მოთხოვეთ შემოიყვანოს რიცხვები(input ით). გადაქციეთ ეს სტრინგი სიად ოღონდ ისე, რომ საბოლოო სია შეიცავდეს ინტეჯერებს 

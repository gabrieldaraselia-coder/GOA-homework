# შექმენი სტრინგი, სადაც ჩაწერ შენს სახელს.
#   -> დაბეჭდე პირველი სიმბოლო ინდექსის გამოყენებით
name = "gabrieli"
word = name[0]
print(word)


# შექმენი სტრინგი, სადაც ჩაწერ შენს გვარს.
#   -> დაბეჭდე ბოლო სიმბოლო ინდექსის გამოყენებით
surname = "daraselia"
word = surname[8]
print(word)


# შექმენი სტრინგი: "Python"
#   -> დაბეჭდე მესამე სიმბოლო
programm_language = "python"
word = programm_language[2]
print(word)



# შექმენი სტრინგი: "Programming"
#   -> დაბეჭდე პირველი 4 სიმბოლო (სლაისინგით)
programm = "Programming"
word = programm[0] + programm[1] + programm[2] + programm[3]
print(word)



# შექმენი სტრინგი: "Computer"
#   -> დაბეჭდე ბოლო 3 სიმბოლო (სლაისინგით)

# ეს ვერ გავიგე





# შექმენი სტრინგი: "HelloWorld"
# -> დაბეჭდე შუაში არსებული სიმბოლოები (მაგ: loWo)

# ეს ვერ გავიგე


# შექმენი სტრინგი: "Georgia"
# -> დაბეჭდე 2-დან 5-მდე ინდექსზე არსებული სიმბოლოები

country = "Georgia"
word = country[1] + country[2] + country[3] + country[4] 
print(word)

# შექმენი სტრინგი, სადაც ჩაწერ შენს საყვარელ სიტყვას
# -> თუ პირველი სიმბოლო არის "A":
#       დაბეჭდე პირველი 3 სიმბოლო
#   -> სხვა შემთხვევაში:
#       დაბეჭდე ბოლო 3 სიმბოლო

favourite_word = "Apple"
if favourite_word[0] == "A":
    print(favourite_word[0] + favourite_word[1] + favourite_word[2])
else:
    print(favourite_word[-1] + favourite_word[-2] + favourite_word[-3])


# შექმენი სტრინგი: "Education"
# -> ამოიღე პირველი და ბოლო სიმბოლო და დაბეჭდე დარჩენილი ნაწილი
string = "Education"
word = string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] 
print(word)
# შექმენი სტრინგი: "Developer"
# -> შეაერთე პირველი 3 და ბოლო 3 სიმბოლო (ახალ სტრინგში) და დაბეჭდე
String = "Dev"
string = "per"
word = String[0] + String[1] + String[2] + string[0] + string[1] + string[2] 
print(word)
# შექმენი სტრინგი, სადაც ჩაწერ რაიმე წინადადებას
# -> დაბეჭდე მხოლოდ პირველი სიტყვა (სლაისინგის გამოყენებით)
# ეს ვერ გავიგე

# შექმენი სტრინგი: "abcdef"
# -> დაბეჭდე ყოველი მეორე სიმბოლო
string = "abcdef"  
word = string[1] + string[3] + string[5]
print(word) 
# შექმენი სია, სადაც შეინახავ 8 ელემენტს (ნებისმიერი ტიპის)
# -> დაბეჭდე შუაში არსებული 4 ელემენტი
list = [True, "car", 12, 13, 14, True, False, "programm"]
word = list[2], list[3], list[4], list[5] 
print (word)
# შექმენი სია, სადაც შეინახავ 6 მუსიკოსის სახელს
# -> დაბეჭდე ბოლო 2 ელემენტი (სლაისინგით)
#ეს ვერ გავიგე
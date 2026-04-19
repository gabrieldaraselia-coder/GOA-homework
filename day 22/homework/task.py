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
slice = programm[:4]
print(slice)



# შექმენი სტრინგი: "Computer"
#   -> დაბეჭდე ბოლო 3 სიმბოლო (სლაისინგით)

string = "computer"
slice = string[5:]
print(slice)




# შექმენი სტრინგი: "HelloWorld"
# -> დაბეჭდე შუაში არსებული სიმბოლოები (მაგ: loWo)

string = "HelloWorld" 
slice = string[3:7]
print(slice)


# შექმენი სტრინგი: "Georgia"
# -> დაბეჭდე 2-დან 5-მდე ინდექსზე არსებული სიმბოლოები

country = "Georgia"
slice = country[2:5]
print(slice)

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
slice = string[1:8]
print(slice)



# შექმენი სტრინგი: "Developer"
# -> შეაერთე პირველი 3 და ბოლო 3 სიმბოლო (ახალ სტრინგში) და დაბეჭდე
String = "Developer"
slice = String[:3] + String[-3:]
print(slice)



# შექმენი სტრინგი, სადაც ჩაწერ რაიმე წინადადებას
# -> დაბეჭდე მხოლოდ პირველი სიტყვა (სლაისინგის გამოყენებით)

string = "apples and bananas"
slice = string[:6]
print(slice)



# შექმენი სტრინგი: "abcdef"
# -> დაბეჭდე ყოველი მეორე სიმბოლო
string = "abcdef"  
word = string[1] + string[3] + string[5]
print(word) 



# შექმენი სია, სადაც შეინახავ 8 ელემენტს (ნებისმიერი ტიპის)
# -> დაბეჭდე შუაში არსებული 4 ელემენტი
list = [True, "car", 12, 13, 14, True, False, "programm"]
slice = list[2:6] 
print (slice)



# შექმენი სია, სადაც შეინახავ 6 მუსიკოსის სახელს
# -> დაბეჭდე ბოლო 2 ელემენტი (სლაისინგით)
musikians = ["Drake", "mozart", "led zeppelin", "michael jackson", "taylor swift", "bruno mars"]
slice = musikians[-2:]
print(slice)
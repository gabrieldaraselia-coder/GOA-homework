# ახსენით რა არის mutable და immutable?
# mutable - შეცვლადი მნიშვნელობა
# immutable - უცვლადი მნიშვნელობა


# ახსენით რას აკეთებს len ფუნქცია
# len - ფუნქცია გვეხმარება მიმდევრობაში გავიგოთ ელემენტების რაოდენობა


# შექმენით ცვლადი სადაც შეინახავთ რაიმე სიტყვას. დაპრინტეთ რამდენი სიმბოლოა ამ სიტყვაში
word = "Apple"
print(len(word))


# შექმენით ცვლადი სადაც მომხმარებელს შემოაყვანინებთ რაიმე წინადადაებას. დაპრინტეთ სიმბოლოების რაოდენობა ამ წინადადებაში
word = input("enter your word here: ")
print(len(word))


# შექმენით სია სადაც შეინახავთ რიცხვებს. for loop ის გამოყენებით დაითვალეთ რამდენი დადებითი და რამდენი უარყოფითი რიცხვია ამ სიაში
positive = 0
negative = 0

numbers = [23, 34, 45, 7, -2, -4, -5, 12, 56]
for i in range(9):
    if numbers[i] < 0:
        negative = negative + 1
    else:
        positive = positive + 1
print(positive)
print(negative)


# შექმნეით სია სადაც შეინახავთ რიცხვებს. დაითვალეთ რამდენი რიცხვი არის ამ სიაში ისეთი, რომელიც იყოფა 5-ზე
numbers = [12, 30, 44, 53, 65, 73, 85]
for i in range(len(numbers)):
     if numbers[i] % 5 == 0:
        print(numbers[i])



# შექმენით სია სადაც შეინახავთ რიცხვებს. დაპრინტეთ მხოლოდ ისეთი რიცხვები, რომლებიც იყოფა 4-ზეც და 7-ზეც
numbers = [28, 34, 43, 54, 61, 75, 86]
for i in range(len(numbers)):
     if numbers[i] % 4 == 0 and numbers[i] % 7== 0:
        print(numbers[i])


# შექმენით სია სადაც შეინახავთ ნებისმიერ მნიშვნელობებს. დაპრინტეთ მხოლოდ ის ელემენტები, რომლებიც იმყოფებიან ლუწ ინდექსზე
arr = [True, "cat", False, 14, 55, 4.54, True]
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i]) 


# შექმენით სია სადაც შეინახავთ სიტყვებს. დაითვალეთ იმ სიტყვების რაოდენობა, რომელთა სიგრძეც მეტია 5-ზე
count = 0
words = ["cat", "footballer", "ball", "human", "elephat"]
for i in range(len(words)):
    print(words[i])
    if len(words[i]) > 5:
        count = count + 1
print(count)

                                 



# შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო
word = "apple and banana"
for i in range(len(word)):
    print(word[i])

# შექმენით ცვლადი, რომელშიც შეინახავთ რაიმე წინადადებას. for ლუპის გამოყენებით დაპრინტეთ თითოეული სიმბოლო გარდა გამოტოვებისა
arr = "apple or banana"
for i in range(len(arr)):
    if arr[i] != " ":
        print(arr[i])

# შექმენით სია სადაც შეინახავთ სიტყვებს. for ლუპის გამოყენებით დაპრინტეთ: 'სიტყვა - სიგრძე'
list = ["car", "cat", "dog", "ball", "duck"]
for i in range(len(list)):
    print(list[i], "-",    len(list[i]))
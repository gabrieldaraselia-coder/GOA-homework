# # 200 დან 500 მდე დაპრინტეთ 4-ის და 7-ის საერთო ჯერადები
# for i in range(200, 500):
#     if i % 10 == 0 and i % 7 == 0:
#         print(i)

# i = 200
# while i < 500:
#     if i % 10 == 0 and i % 7 == 0:
#         print(i)
#     i = i + 1
# #  300 დან 1000 მდე დაპრინტეთ 3-ის ან 10-ის ჯერადები

# for i in range(300, 1000):
#     if i % 10 == 0 or  i % 3 == 0:
#         print(i)

# i = 300
# while i < 1000:
#     if i % 3 == 0 or i % 10 == 0:
#         print(i)
#     i = i + 1

# # -1 დან 50 მდე დაპრინტეთ ყველა რიცხვი:
# #  - ლუწი რიცხვებისთვის დაწერეთ "Even: (რიცხვი)"
# #  - კენტი რიცხვებისთვის დაწერეთ "Odd: (რიცხვი)"



# for i in range(1, 50):
#     if i % 2 == 0:
#         print("odd " + str(i))
#     elif i % 2 == 1:
#         print("even " + str(i))

# i = 0
# while i < 50:
#     if i % 2 == 0:
#         print("odd " + str(i))
#     elif i % 2 == 1:
#         print("even " + str(i))
#     i = i + 1





# #  მომხმარებელს შემოატანინეთ 10 რიცხვი და:
# #   - დათვალეთ რამდენი არის დადებითი
# #   - რამდენი არის უარყოფითი

# positive = 0
# negative = 0

# for i in range(10):
#      n = int(input("enter number here: "))
#      if n > 0 :
#          positive = positive + 1
#      elif n < 0 :
#          negative = negative + 1
# print(positive)
# print(negative)






# #  მომხმარებელს შემოატანინეთ რიცხვი და:
# #  - თუ რიცხვი იყოფა 2-ზე და 3-ზე -> დაპრინტეთ "Good"
# #   - თუ მხოლოდ 2-ზე იყოფა -> "Two"
# #   - თუ მხოლოდ 3-ზე იყოფა -> "Three"
# #   - სხვა შემთხვევაში -> "None"


# number = int(input("enter number here: "))
# if number % 2 == 0 and number % 3 == 0 :
#     print("Good")
# elif number % 2 == 0 :
#     print("Two")
# elif number % 3 == 0 :
#     print("Three")
# else:
#     print("None")





# #  1 დან 100 მდე დაპრინტეთ ყველა რიცხვი, მაგრამ:
# #    - თუ რიცხვი იყოფა 3-ზე -> დაპრინტეთ "Fizz"
# #    - თუ იყოფა 5-ზე -> დაპრინტეთ "Buzz"
# #    - თუ ორივეზე იყოფა -> დაპრინტეთ "FizzBuzz"
# #   - სხვა შემთხვევაში -> თავად რიცხვი



# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)




# # შექმენით პროგრამა, რომელიც მომხმარებელს რიცხვს შემოატანინებს მანამ სანამ 0-ს არ შეიყვანს:
# #   - დადებითი რიცხვების რაოდენობა დაითვალეთ
# #   - უარყოფითებისაც
# #   - ბოლოს(ანუ როცა 0 შემოიყვანა) დაპრინტეთ ეს რაოდენობები


# positive = 0
# negative = 0

# n = int(input("enter number here: "))
# while 0 != n:
#     n = int(input("enter number here: "))
#     if n > 0:
#         positive = positive + 1
#     elif n < 0:
#         negative = negative + 1
# print(positive,negative)


# მომხმარებელს შემოატანინეთ რიცხვი და:
#   - დაპრინტეთ 1 დან ამ რიცხვამდე ყველა რიცხვი
#   - მაგრამ გამოტოვეთ ის რიცხვები, რომლებიც იყოფა 4-ზე


#  მომხმარებელს შემოატანინეთ რიცხვი 5-ჯერ (ციკლით) და ყოველ ჯერზე:
#   - თუ რიცხვი ლუწია -> დაპრინტეთ "Even"
#   - თუ კენტია -> დაპრინტეთ "Odd"
#   - ეს დავალება გააკეთეთ ორ ვარიანტში -> for ციკლითაც და while ციკლლითაც
for i in range(5):
      n = int(input("enter number here: "))
if i % 2 == 0:
        print("odd " + str(i))
elif i % 2 == 1:
        print("even " + str(i))


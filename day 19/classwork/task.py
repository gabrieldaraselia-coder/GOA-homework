# # შექმენით პროგრამა, რომელიც მომხმარებელს რიცხვს შემოატანინებს მანამ სანამ 0-ს არ შეიყვანს:
# #   - დადებითი რიცხვების რაოდენობა დაითვალეთ
# #   - უარყოფითებისაც
# #   - ბოლოს(ანუ როცა 0 შემოიყვანა) დაპრინტეთ ეს რაოდენობები


# positive = 0
# negative = 0 

# n = int(input("enter number here: "))
# while 0 != n:
#      n = int(input("enter number here: "))
#      if n > 0:
#          positive = positive + 1
#      elif n < 0:
#         negative = negative + 1
        
       
# print(positive,negative)


# n = int(input("შეიყვანე რიცხვი: "))
# for i in range(1, n):
#     if i % 4 != 0:
#         print(i)






i = 0

while i < 5:
    n = int(input("შეიყვანე რიცხვი: "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

    i = i + 1
print(i)





# 1 დან 100 მდე დაპრინტეთ ყველა რიცხვი, მაგრამ:
  
# თუ რიცხვი იყოფა 3-ზე -> დაპრინტეთ "Fizz"
# თუ იყოფა 5-ზე -> დაპრინტეთ "Buzz"
# თუ ორივეზე იყოფა -> დაპრინტეთ "FizzBuzz"
# სხვა შემთხვევაში -> თავად რიცხვი



for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
       print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
       print("Buzz")
    else:
     print(i)
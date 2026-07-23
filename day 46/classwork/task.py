# 1) შექმენით სეტი სადაც შეინახავთ თქვენი მეგობრების სახელ გვარებს. შეინახეთ რომელიმე მეგობრის სახელი გვარი 2ჯერ ან მეტჯერ. დაპრინტეთ შედეგი რამოდენიმეჯერ
my_set = {"levani quxilava", "beqa miqelbaia", "batuka janjrava", "ilia jobava", "ilia jobava"}
print(my_set)
print(my_set)
print(my_set)
print(my_set)
print(my_set)
print(my_set)
print(my_set)
print(my_set)


# 2) შექმენით სიმრავლე, რომელშიც შეიახავთ რაიმე სახელებს. 
#   - ფორ ლუპის საშუალებით დაუარეთ ამ სიმრავლეს
#   - თუ რომელიმე ელემენტი იწყება დიდი ასოთი მაშინ:
#     - დაპრინტეთ ეს ელემენტი და წაშალეთ
#     - მის ნაცვლად ჩაამატეთ ამ სიტყვის სიგრძე ინტეჯერის სახით
#   - ფორ ლუპის ბოლოს დაპრინტეტ სიმრავლე 




names_set = {"დათო", "გიორგი", "ანა", "ლუკა", "salome", "nika"}


for name in list(names_set):
    if name[0].isupper():
        print(f"დიდი ასოთი იწყება: {name}")
        names_set.remove(name) 
        names_set.add(len(name)) 

print("საბოლოო სიმრავლე:", names_set)
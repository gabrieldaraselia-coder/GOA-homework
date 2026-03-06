temperature = int(input("Enter temperature: "))

if temperature >= 30:
    print("ძალიან ცხელა!")

elif temperature >= 20:
    print("სასიამოვნო ამინდია")

elif temperature >= 10:
    print("ცოტა ცივა")

elif temperature >= 0:
    print("ცივა, ჩაიცვი თბილად")

else:
    print("გაიყინები, სახლში დარჩი!")




score = int(input("Enter your score here: "))
Attendance = int(input("Enter Attendance: "))

if score >= 80 and Attendance >= 90:
    print("შენ შესანიშნავად დაწერე გამოცდა")


elif score >=50 and Attendance >= 70:
    print("საშუალოდ დაწერე გამოცდა")

elif score >=30 and Attendance >= 50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")

else:
    print("ჩაიჭერი!")


Temperatura = int(input("Enter temperature here: "))
rain = bool(int(input("Is raining?(0-no , 1-yes): ")))

if Temperatura >= 25 and rain == False:
    print("შესანიშნავი ამინდია სასეირნოდ!")

elif Temperatura >= 25 and rain == True:
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!")

elif Temperatura <= 10 and rain ==True:
    print("სჯობს სახლში დარჩე")

else:
    print("სასიამოვნო ამინდია")



age = int(input("Enter your age here: "))
is_student = int(input("Are you student?(0-no , 1-yes)"))
 
if age < 12 and age > 65:
    print("ბილეთი უფასოა")

elif is_student == True and age > 12:
    print("ბილეთი ნახევარ ფასად")

else:
    print("სრული ფასი უნდა გადაიხადო")

username =input("Enter your username here: ")
password = input("Enter your password here: ")


if username >= "admin" and password >='superSecretPassword':
    print("მოგესალმები, ადმინ!")

elif username >= "guest" and password >="1234":
    print("მოგესალმები, სტუმარო!")

else:
    print("მომხმარებელი არ მოიძებნა!")
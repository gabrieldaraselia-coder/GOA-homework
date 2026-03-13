# Sequenicg - თანმიმდევრულად კოდის შესრულება
# Selection - კოდის შესრულება რაღაცა პირობის მიხედვით კოდების არჩევა შერჩევა ასევე selection-ით მუშაობენ if და else.
# პიტონსი ინდენტაცია ზალიან მთავარია და მას ჩვენ სხვადასხვა მიზნისთვის ვიყენებთ მაგალითად მრავალხაზიანი კოდი რომ დავიცვM



Math = int(input("enter math score: "))
English = int(input("enter english score: "))
Physics = int(input("enter physics score: "))

if Math >= 90 and English >= 90 and Physics >= 90:
    print("შესანიშნავი მოსწავლე ხარ")
    print("ყველა საგანში მაღალი შედეგი გაქვს")

elif Math >= 70 and English >= 70 and Physics >= 70:
    print("კარგი შედეგებია")
    print("სასწავლო წელი წარმატებულია")

elif Math < 50 and English < 50 and Physics < 50:
    print("ერთ-ერთ საგანში დაბალი ქულა გაქვს")
    print("მეტი სწავლა დაგჭირდება")

else:
    print("შედეგები საშუალოა")
    print("შეგიძლია უკეთესიც")




age = int(input("enter your age here: "))
license = int(input("license(0-False , 1-True)"))
drunk = int(input("drunk(0-False , 1-True)"))

if age >= 18 and license == True and drunk == False:
    print("შეგიძლია მანქანის მართვა")
    print("უსაფრთხო მგზავრობას გისურვებთ")

elif age >= 18 and license == False and drunk == False:
    print("ასაკი საკმარისია")
    print("მაგრამ მართვის მოწმობა არ გაქვს")

elif  drunk == True or age < 18 or license == False:
    print("მანქანის მართვა აკრძალულია")
    print("ეს შეიძლება საშიში იყოს")

else:
    print("მონაცემები ვერ გადამოწმდა")
    print("სცადე თავიდან")





price = int(input("enter price here: "))
quantity = int(input("enter quantity: "))
member = int(input("member(0-False , 1-True)"))

if  price >= 100 and quantity >= 3 and member == True:
    print("დიდი ფასდაკლება მიიღე")
    print("მადლობა ერთგული მომხმარებლობისთვის")

elif price >= 100 and quantity >= 3 and member == False:
    print("ფასდაკლება მიიღო")
    print("წევრობის შემთხვევაში უფრო მეტს მიიღებ")

elif price < 50 or quantity == 1 or member == False:
    print("ფასდაკლება არ გეკუთვნის")
    print("მეტი პროდუქტი შეიძინე")

else:
    print("მცირე ფასდაკლება მიიღე")
    print("გმადლობთ შენაძენისთვის")



weight = int(input("enter your weight: "))
height = int(input("enter your height: "))
Age = int(input("enter your age: "))
BMI = weight / (height * height)

if BMI < 18.5 and age >= 18:
    print("შენი BMI დაბალია")
    print("შესაძლოა წონის მომატება დაგჭირდეს")

elif BMI >= 18 and BMI <= 24.9 and age >= 18:
    print("შენი BMI ნორმალურია")
    print("ჯანმრთელ ფორმაში ხარ")

elif BMI >= 25 and BMI < 30 and age < 18:
    print("BMI საშუალოზე მაღალია")
    print("ჯანსაღი კვება მნიშვნელოვანია")

elif BMI >= 30:
    print("BMI მაღალია")
    print("სასურველია ექიმთან კონსულტაცია")

else:
    print("მონაცემები ვერ დამუშავდა")
    print("სცადე თავიდან")





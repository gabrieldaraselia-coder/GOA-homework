# შექმენი სია, სადაც შეინახავ შენს საყვარელ ფერებს.
colours = ["red", "blue", "black"]
print(colours)

# შექმენი სია, სადაც შეინახავ კვირის დღეებს.
Week_Days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# შექმენი სია, სადაც შეინახავ 5 სხვადასხვა რიცხვს. -> დაბეჭდე მესამე ინდექსზე მყოფი ელემენტი

numbers = [15, 16, 17, 18, 19, 20]
numbers[4] = 21
print(numbers)




# შექმენი სია, სადაც შეინახავ 5 ქალაქის სახელს. -> შეცვალე მეორე ინდექსზე მყოფი ელემენტი სხვა ქალაქით
cities = ["batumi", "zugdidi", "tbilisi", "berlin", "moskow"]
cities[2] = "qutaisi"
print(cities)


# შექმენი სია, სადაც შეინახავ შენი ოჯახის წევრების სახელებს. -> დაბეჭდე პირველი და ბოლო ელემენტი (ინდექსებით)
family = ["salome", "giga", "magda", "likuna", "nona", "fati", "avto", "tamazi"]
print(family[0])
print(family[7])

# შექმენი სია, სადაც შეინახავ 6 სხვადასხვა რიცხვს. -> შეცვალე მეოთხე ინდექსზე მყოფი ელემენტი 100-ით
numbers = [21, 22, 23, 24, 25, 26]
numbers[4] = 100
print(numbers)



# შექმენი სია, სადაც შეინახავ 10 ძაღლის სახელს. -> შეცვალე მეხუთე ელემენტი სხვა თამაშით
dog_Names = ["Otis", "Ace", "Finn", "Gus", "Ben", "Gizmo", "Blue", "Bo", "Jax", "Hank"]
dog_Names[4] = "Roblox"
print(dog_Names)


# შექმენი სია, სადაც შეინახავ 3 სტრინგს, 3 რიცხვს და 3 ბულეანს. -> დაბეჭდე ნებისმიერი ერთი ელემენტი ინდექსის გამოყენებით
data_types = ["cat", "car", "cow", 15, 16, 17, True, False, True]
print(data_types[2])


# შექმენი სია, სადაც შეინახავ 5 მუსიკოსის სახელს. -> თუ პირველი ელემენტი არის 'Drake' -> შეცვალე სხვა მუსიკოსით
musisikians = ["Drake", "mozart", "led zeppelin", "michael jackson", "taylor swift"]
if musisikians[0] == "Drake":
    musisikians[0] = "bruno mars"
print(musisikians)


# შექქმენი სია, სადაც შეინახავ რიცხვებს(როგორც მთელები ისე არამთელები) -> გაზარდე სიის პირველი და ბოლო ელემენტი 1000-ით
numbers = [3, 3.14, 5, 7.89, 10]
numbers[0] = numbers[0] + 1000
numbers[4] = numbers[4] + 1000
print(numbers)


# შექმენი სია, სადაც შეინახავ 3 რიცხვს(როგორც მთელები ისე არამთელები)
#   - თუ პირველი რიცხვი არის მეტი 10-ზე:
#       გაზარდე სიის მესამე ელემენტი პირველი და მეორე ელემენტის ნამრავლით
#   - სხვა შემთხვევაში:
#       გაზარდე სიის პირველი ელემენტი მეორე და მესამე ელემენტის ნამრავლით
numbers = [9, 15, 23.50]
if numbers[0] > 10:
    numbers[2] = numbers[2] + numbers[0] * numbers[1]
else:
    numbers[0] = numbers[0] + numbers[2] * numbers[1]
print(numbers)
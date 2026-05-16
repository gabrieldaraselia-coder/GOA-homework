# 1) მომხმარებელს მოთხოვეთ რაიმე წინადადება/სიტყვა.
#   - დაითვალეთ რამდენი დიდი და რამდენი პატარა ასო არის ამ სტრინგში
#   - დაპრინტეთ შედეგები

text = input("შეიყვანე წინადადება ან სიტყვა: ")
big_letters = 0
small_letters = 0

for i in range(len(text)):
    if text[i].up:
        big_letters =big_letters + 1
    elif text[i].lower():
        small_letters =small_letters + 1

print("დიდი ასოების რაოდენობა:", big_letters)
print("პატარა ასოების რაოდენობა:", small_letters)

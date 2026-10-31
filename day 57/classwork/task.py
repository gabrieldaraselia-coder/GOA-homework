# 1) შექმენით დიქთი, სადაც შეინახავთ ინფორმაციას კოსმოსური ხომალდის შესახებ
#   - დაპრინტეთ ამ კოსმოსური ხომალდის რაიმე მნიშვნელობა
#   - შეცვალეთ ამ კოსმოსური ხომალდის რაიმე გასაღების მნიშვნელობა
#   - დაამატეთ ამ კოსმოსურ ხომალდში რაიმე item
#   - წაშალეთ ამ კოსმოსური ხომალდიდან რაიმე item

rocket = {
    "Name" : "rocket3",
    "Weight" : "10t",
    "Height" : "10m",
    "Speed" : "3000_km/h"
}

print(rocket["Name"])

rocket["Name"] = "Rocket4"

rocket["From"] = "Planet_X"

del rocket["Weight"]



# 2) გამოიყენეთ წინა დავალებაში არსებული დიქთი. ფორ ლუპის საშუალებით დაპრინტეთ:
#   - მისი ყველა მნიშვნელობა ცალკ ცალკე
#   - მისი ყველა გასაღები ცალკ ცალკე 
#   - მისი ყველა item ცალკ ცალკე

my_dict = {
    "name": "Giorgi", 
    "age": 25, 
    "city": "Tbilisi"}


print("Keys:")
for key in my_dict.keys():
    print(key)


print("Values:")
for value in my_dict.values():
    print(value)


print("Items:")
for item in my_dict.items():
    print(item)
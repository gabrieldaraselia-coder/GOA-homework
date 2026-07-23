# 1) შექმენით თაფლი/კორტეჟი, სადაც შეინახავთ თქვენს სახელს, გვარს, ასაკს, წონას და ჰობის. დაპრინტეთ რომელიმე ელემენტი
my_tuple = ("Gabrieli", "Daraselia", 13, 43, "Footbal Play")
print(my_tuple[1])

# 2) თქვენი თაფლი დაშალეთ ცვლადებათ. ბოლო ორი მნიშვნელობა შეინახეთ რესტ ცვლადში

My_tuple = ("gabo", "giga", "salome", "magda", "nona")

pirveli, meore, mesame, *rest = My_tuple

print(pirveli)  
print(meore)    
print(mesame)   
print(rest)
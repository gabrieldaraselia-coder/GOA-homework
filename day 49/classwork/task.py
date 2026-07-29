# 1) შექმენით ორი სეტი. თითოეულში შეინახეთ რანდომ ელემენტები.
#   - გამოიყენეთ დღეს ნასწავლი ოთხივე მეთოდი და თან ოთხივე ახსენით კომენტარით
#   - ოთხივე მეთოდის შედეგი დაპრინტეთ
#   - დაპრინტეთ ორივე სეტი კოდის ბოლოს

set_1 = {1, 2, 3, "gabo", "car"}
set_2 = {2, 3, 5, "cat", "giga"}

# ეძებს საერთო ელემენტებს
new_set = set_1.intersection(set_2)

# ეძებს იმ ელემენტებს რომელიც ეძებს ირველი სეტის ელემენტებს
diff_set = set_1.difference(set_2)

# ეძებს უნიკალურ ელემენტებს
union_set = set_1.union(set_2)

# ეზებს ყელემეტებს გარდა საერთოებისა
symmetric_diff_set = set_1.symmetric_difference(set_2)

print(new_set)
print(diff_set)
print(union_set)
print(symmetric_diff_set)
print(set_1)
print(set_2)
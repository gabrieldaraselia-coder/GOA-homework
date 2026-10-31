# 1.
def angle(n):
  return (n - 2) * 180

# 2.
def round_to_next5(n):
    return (n + 4) // 5 * 5

# 3.
def factorial(n):
  if n == 0:
    return 1

  result = 1
  for i in range(1, n):
    result = result * i
  result = result * n
  return result

# 4.
def row_weights(array):
  team1 = 0
  team2 = 0

  for i in range(len(array)):
    if i % 2 == 0:
      team1 = team1 + array[i]
    else:
      team2 = team2 + array[i]

  return (team1, team2)

# 5.
def generate_shape(n):
    one_line = ""
    for i in range(n):
        one_line = one_line + "+"

    result = one_line

    for i in range(1, n):
        result = result + "\n" + one_line

    return result

# 6.
def largest_pair_sum(numbers):
    first_max = max(numbers)

    numbers.remove(first_max)

    second_max = max(numbers)

    result = first_max + second_max

    return result

# 7.
def alphabet_war(fight):
    left_score = 0
    right_score = 0
    
    for letter in fight:
        if letter == 'w':
            left_score = left_score + 4
        elif letter == 'p':
            left_score = left_score + 3
        elif letter == 'b':
            left_score = left_score + 2
        elif letter == 's':
            left_score = left_score + 1
            
        elif letter == 'm':
            right_score = right_score + 4
        elif letter == 'q':
            right_score = right_score + 3
        elif letter == 'd':
            right_score = right_score + 2
        elif letter == 'z':
            right_score = right_score + 1

    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"

# 8.
def switcheroo(s):
  result = ""

  for char in s:
    if char == "a":
      result = result + "b"
    elif char == "b":
      result = result + "a"
    else:
      result = result + char

  return result
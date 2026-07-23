# 1.
def area_or_perimeter(l, w):
    if l == w:   
        return l * w
    else:
        return 2 * (l + w)

# 2.
def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False

# 3.
def sum_array(arr):
    if len(arr) <= 1:
        return 0
    
    total_sum = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    
    return total_sum - min_val - max_val

# 4.
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    
    if (p1 == "rock" and p2== "scissors") or \
    (p1 == "scissors" and p2 == "paper") or \
    (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    

    return "Player 2 won!"

# 5.
def count_positives_sum_negatives(arr):
    if not arr:
        return tuple()

    count_positives = 0
    sum_negatives = 0


    for num in arr:
        if num > 0:
            count_positives = count_positives + 1
        if num < 0:
            sum_negatives = sum_negatives + num

    return (count_positives, sum_negatives)
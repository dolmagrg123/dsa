## Problem 7

def count_less_than(race_times, threshold):

    sum = 0

    for i in range(len(race_times)-1):
        if race_times[i-1] < threshold:
            sum += 1
        
    return sum

# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# print(count_less_than(race_times, threshold))

# race_times = []
# threshold = 4
# print(count_less_than(race_times, threshold))

## Problem 8

def print_todo_list(tasks):
    print("Pooh's To Dos:")

    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")

# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

## Problem 9

def can_pair(item_quantities):

    for i in range(len(item_quantities)):
        if item_quantities[i] % 2 != 0:
            return False
    
    return True

# item_quantities = [2, 4, 6, 8]
# print(can_pair(item_quantities))

# item_quantities = [1, 2, 3, 4]
# print(can_pair(item_quantities))

# item_quantities = []
# print(can_pair(item_quantities))

##Problem 10

def split_haycorns(quantity):
    divisors =[]

    for i in range(quantity):
        if quantity % (i+1) == 0:
            divisors.append(i + 1)
    
    return divisors

# quantity = 15
# print(split_haycorns(quantity))

## Problem 11

def tiggerfy(s):
    new_string = ""

    for i in s:
        if i.lower() not in "tiger":
            new_string +=  i
    return new_string

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))


## Problem 12
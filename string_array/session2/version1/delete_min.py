'''

UNDERSTAND

- create a function that takes in a list of integers
- remove the min val from the list until the list becomes empty
- creating a new list -> values from the prev list in the order they were removed

'''

def delete_minimum_elements(hunny_jar_sizes):

    hunny_jar_sizes.sort(reverse = True)
    new_list = []

    while hunny_jar_sizes:
        new_list.append(hunny_jar_sizes.pop())
    return new_list

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

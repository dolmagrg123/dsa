##Problem 1
def welcome():
    print ("Welcome to The Hundred Acre Wood")

##Problem 2
def greeting(name):
    print (f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greeting("Dolma")

##Problem 3
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

# print_catchphrase("Pooh")
# print_catchphrase("Piglet")

##Problem 4

#getitem(items,x)
# get len(items)
# x should be between 0 and len(items)-1
#if x is not valid return none
# returns items[x]

def get_item(items, x):

    if x > len(items)-1:
        return None
    else:
        return items[x]

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 4
# print(get_item(items, x))

##Problem 5

def sum_honey(hunny_jars):
    sum = 0

    for i in range(len(hunny_jars)):
        sum += hunny_jars[i]

    return sum

# hunny_jars = [1,2]
# print(sum_honey(hunny_jars))

##Problem 6

def doubled(hunny_jars):

    for i in range(len(hunny_jars)):
        hunny_jars[i] *=  2
    
    return(hunny_jars)

# hunny_jars = [1, 2, 3]
# print(doubled(hunny_jars))







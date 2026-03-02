

def is_acronym(words, s):
    new_string = ''

    for i in words:
        new_string += i[0]
    
    if new_string == s:
        return True
    else:
        return False

words = ["christopher", "robin", "milne"]
s = "cmr"
print(is_acronym(words, s))
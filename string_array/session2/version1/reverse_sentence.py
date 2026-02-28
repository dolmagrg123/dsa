#REVERSE SENTENCE

'''
UNDERSTAND

1. Create a function reverse_sentence()
2. Take string sentence as parameter
3. return the sentence with words in reverse
4. if only one word, return the original string

** sentence -> alphabetic characters and spaces(to separate) only

edge cases: what if it is empty string
happy cases: reverse_sentence("hello friend") -> friend hello
             reverse_sentence("hello") -> hello


PLAN

1. create function and take sentence string
2. split the sentence and add to a list
3. if len of list <=1 , return sentence
4. create another list to add the words in reverse
5. use .join() method to add the words from the second list into the string

IMPLEMENT
'''

def reverse_sentence(sentence):

    split_list = sentence.split()

    if len(split_list) <= 1:
        return sentence

    reverse_list = split_list[::-1]

    return_string = " ".join(reverse_list)

    return return_string

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))



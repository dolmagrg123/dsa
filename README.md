- [PURPOSE](#purpose)
- [OBJECTIVES](#objectives)
- [STEPS And Why each was Necessary](#the-steps-taken-and-why-each-was-necessaryimportant)
- [SYSTEM DESIGN DIAGRAM](#system-design-diagram)
- [ISSUES and TROUBLESHOOTING](#issuestroubleshooting)
- [OPTIMIZATION](#optimization)
- [CONCLUSION](#conclusion)


## Steps to Follow

Make sure to install all requirements:

pip install -r requirements.txt

Set your API Key in your system:
Windows (Command Prompt): set RANDOM_NUM_API_KEY=your_api_key_here
Windows (PowerShell): $env:RANDOM_NUM_API_KEY="your_api_key_here"
macOS/Linux (Bash/Zsh): export RANDOM_NUM_API_KEY=your_api_key_here

---

## Purpose  


---

## Objectives  

- total 10 attempts
- 4 random numbers out of total 10 numbers
- feedback on number and location

examples:
Gameinitializes and selects “0 1 3 5”
 Player guesses “2 2 4 6”, game responds “all incorrect”
 Player guesses “0 2 4 6”, game responds “1 correct number and 1 correct location”
 Player guesses “2 2 1 1”, game responds “1 correct number and 0 correct location”
 Player guesses “0 1 5 6”, game responds “3 correct numbers and 2 correct location”

 UI:
 Ability to guess the combinations of 4 numbers
 Ability to view the history of guesses and their feedback
 The number of guesses remaining is displayed


UseRandomgeneratorAPI(https://www.random.org/clients/http/api/)torandomlyselect
 4numbersfrom0~7(Duplicatenumbersareallowed)-Youcanchoosewhichevercombinationofprogramminglanguages, tools, frameworks,
 andlibrariesyoufindappropriatewithinreason(e.g.youcan’tuseagameframework
 that implementsMastermind)


---

## Different ways we could resolve this:

1. The base game with only 4 digit combination and a single user, we can use list and loop through the list to find the correct number and location. Keeping them all in a single file. 

Pros:

Since total number of combination is only 4, having a simple file we could easily loop through all the numbers and give feedback on the correct number of location and numbers.

Cons:

If we scale this into a super long combination, giving feedback every single time the user guess the number, it will take a long time to loop with time complexity of O(n^2).

2. Separate the game into different classes:



## The "STEPS" taken (and why each was necessary/important)  

1. Make sure to install all requirements:

pip install -r requirements.txt

Set your API Key in your system:
Windows (Command Prompt): set RANDOM_NUM_API_KEY=your_api_key_here
Windows (PowerShell): $env:RANDOM_NUM_API_KEY="your_api_key_here"
macOS/Linux (Bash/Zsh): export RANDOM_NUM_API_KEY=your_api_key_here

2. To ensure that the game continues even when the API isnt working, we generate the number internally, but we keep log of the times the API failed so that we can troubleshoot later.

---

## Monitoring  

---

## Issues & Troubleshooting  

1. Using a single loop to find both correct location and correct number. 
    def checklocation(user_list,random_list):
        correct_location = 0
        correct_number = 0
        index = 0
        for i in user_list:
            if i == random_list[index]:
                correct_location += 1
                correct_number +=1
                random_list[index]="matched"
                user_list[index] ="ignore"
            else:
                if user_list[index] in random_list:
                    correct_number += 1
            index +=1

        In this method, everytime the number is not in the correct location, it goes into the else statement

        so if random number is 1127 and user guessed 2342, it will answer 2 correct number instead of one. Which is incorrect.

2. The current provided API is obsolete, I used  new api I was rerouted to ( https://api.random.org/json-rpc/4/invoke ) in the same website.
It does not have GET request only POST is allowed
Some of the parameters are different but we are still able to get 4 random numbers from it in json format.

https://api.random.org/json-rpc/4/basic



### "SYSTEM DESIGN DIAGRAM"

![System_design_Diagram](Diagram.jpg)

---

## Optimization Suggestions  


## Conclusion  
 


 # Version 2:

Issue:
 The nested loops for finding correct numbers (those present but in the wrong location) have a time complexity of O(n^2), where n is the number of digits. 
Change:
 A more efficient approach would be to use frequency maps (dictionaries or counters) to count the occurrences of each digit in both the user's guess and the target combination. This would allow you to determine the number of correct digits in O(n) time.

Key features of Counter:

Dictionary-like interface: You can access the count of an item using dictionary-like syntax (e.g., frequency_map[2] would return 3). If an item is not in the collection, accessing its count returns 0 instead of raising a KeyError.
Easy to update: You can update counts by adding new items or using the update() method.
Useful methods: Counter provides useful methods like most_common() to get the most frequent items and their counts.
Supports arithmetic operations: You can perform arithmetic operations (addition, subtraction, etc.) on Counter objects.
The collections.Counter class makes it very easy to create frequency maps in Python. You just pass the iterable (list, string, etc.) to the Counter constructor:

from collections import Counter

my_list = [1, 2, 2, 3, 1, 4, 2]
frequency_map = Counter(my_list)
print(frequency_map)
# Output: Counter({2: 3, 1: 2, 3: 1, 4: 1})

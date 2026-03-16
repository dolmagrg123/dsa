"""
On your platform, comments on posts are displayed in the order they are received. 
However, for a special feature, you need to reverse the order of comments before displaying them. 
Given a queue of comments represented as a list of strings, reverse the order using a stack.


#UNDERSTAND:

input = queue

PLAN:
- create a stack
- for loop from queue and add to stack
- pop from stack and add to list


"""

def reverse_comments_queue(comments):
    stack = []

    for comment in comments:
        stack.append(comment)
    result =[]

    while stack:
        result.append(stack.pop())

    return result

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
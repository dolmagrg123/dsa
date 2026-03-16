"""

You are managing a social media platform and need to ensure that posts are properly formatted. 
Each post must have balanced and correctly nested tags, such as () for mentions, 
[] for hashtags, and {} for links. You are given a string representing a post's content, 
and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.


#UNDERSTAND:

- tags: (), [], {}
- check if its valid

PLAN:

- create a stack
- for loop in the posts
- if paren = ( { [  --> append
- else: paren == ], check if stack[1] will be [,  ......}): stack.pop()


"""

def is_valid_post_format(posts):

    stack = []

    for paren in posts:
        if paren == "(" or paren == "["  or paren == "{":
            stack.append(paren)

        elif paren == ")":
            if stack[-1] != "(":
                return False
            stack.pop()

        elif paren == "}":
            if stack[-1] != "{":
                return False
            stack.pop()
        elif paren == "]":
            if stack[-1] != "[":
                return False
            stack.pop()

    return True

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))


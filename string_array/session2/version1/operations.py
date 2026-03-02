'''Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because
 he's the only tigger around! Given a list of strings operations containing a list of operations, 
return the final value of tigger after performing all the operations.

'''


def final_value_after_operations(operations):
    
    tigger = 1
    
    for i in operations:
        if i in ["bouncy", "flouncy"]:
            tigger += 1
        elif i in ["trouncy", "pouncy"]:
            tigger -= 1
        else:
            tigger = tigger
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
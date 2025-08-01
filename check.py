

def checklocation(user_list,random_list):
        correct_location = 0
        correct_number = 0

        index = 0

        #create copies of the list to avoid modifying the original list
        user = list(user_list)
        random = list(random_list)

        #checking to see if the numbers are in correct location
        for i in user:
            if i == random[index]:
                correct_location += 1
                correct_number +=1
                random[index]="matched"
                user[index] ="ignore"
            index +=1

        for i in range(len(user)):
            for j in range (len(random)):
                if user[i] == random[j]:
                    correct_number += 1
                    random[j]="matched"
                    user[i] ="ignore"
        
        #print all incorrect if none of the numbers and location matches
        if correct_number == 0 and correct_location == 0:
            print ("all incorrect")
        else:
            print(f" {correct_number} correct number and {correct_location} correct location")


def correct_combination(user_input_list,random_generated_number):
    if random_generated_number == user_input_list:
        print("Congratulations!!! You have guessed the correct combination")
        return True
        
    else:
        checklocation(user_input_list,random_generated_number)
        return False

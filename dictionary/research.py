"""
In a wildlife research station, each letter of the alphabet represents a different observation point 
laid out in a single row. Given a string station_layout of length 26 indicating the layout of these
observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). 
To make observations in a specific order represented by a string observations, 
you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices,
 |i - j|.

Write a function that returns the total time it takes to visit all the required observation points 
in the given order with one movement.


#UNDERSTAND:

station_layout ->26 : index 0 to 25

observations -> string

enemurate

edge cases: empty string -> return 0

PLAN:
1. current_index = 0, total time = 0
2. loop through observations -> each char index
3. enemurate through station_layout 
4. if char in observation in station_layout: index of the char =Char_index
5. |char_index - current-index|
6. add the diff to total_time

7. return total time

"""

def navigate_research_station(station_layout, observations):
    current_index = 0
    total_time = 0

    for char in observations:
        for ind, letter in enumerate(station_layout):
            if char == letter :
                char_index = ind
                break
        total_time += abs(current_index - char_index)
        current_index = char_index

    return total_time


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

            
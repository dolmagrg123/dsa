"""
As part of conservation efforts, certain species are considered endangered 
and are represented by the string endangered_species. 
Each character in this string denotes a different endangered species.
 You also have a record of all observed species in a particular region, 
 represented by the string observed_species. Each character in observed_species 
 denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.


#UNDERSTAND:

endangered_species / observed_species -> string
edge cases: if nothing in intersection, return 0

#PLAN

1. Convert string into set: endangered_species
2. count varible
3. loop through observed species
4. if in endangered species -> increase count
5. return count
"""

def count_endangered_species(endangered_species, observed_species):
    new_set = set(endangered_species)
    count = 0

    for species in observed_species:
        if species in endangered_species:
            count += 1
    return count


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))
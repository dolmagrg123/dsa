"""
Imagine you are working on a wildlife conservation database.
 Write a function named most_endangered() that returns the species with the highest
   conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter.
 Each dictionary represents data associated with a species, 
 including its name, habitat, and wild population. 
 The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.

#Understand

input: take in a list of dictionaries named species_list
return : name of species with lowest pop
dict: species, including its name, habitat, and wild population.

edge case: empty list -> None
            : multiple species with lowest population


#PLAN:

1. Asssume first species has lowest population : store in a variable : name and popu
2. for loop the list: species_list
3. check if the current is lower than the lowest population
4. return species_name

#IMPLEMENT

"""

def most_endangered(species_list):
    min_population = species_list[0]["population"]
    species_name = species[0]["name"]

    for i in species_list:
        if i["population"] < min_population:
            min_population = i["population"]
            species_name = i["name"]

    return species_name
        

species = [
    {"name": "Tiger", "habitat": "Forest", "population": 3900},
    {"name": "Panda", "habitat": "Mountain", "population": 1864},
    {"name": "Amur Leopard", "habitat": "Forest", "population": 120000}
]

print(most_endangered(species))
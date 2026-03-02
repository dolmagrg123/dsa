def exclusive_elemts(lst1, lst2):
    
    return list(set(lst1) ^ set(lst2))

    # new_lst =[]

    # for items in lst1:
    
    #     if items not in lst2:
    #         new_lst.append(items)
    
    # for items in lst2:
    
    #     if items not in lst1:
    #         new_lst.append(items)

    # return new_lst


print(exclusive_elemts([1,2,3],[2,3,4]))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))        

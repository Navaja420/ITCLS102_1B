clothing_brand1 = "HighMinds"
clothing_brand2 = "MN+LA"
#List wtih default values

clothing_brand = ["HIGHMINDS" , "MN+LA" , "DAILY FLIGHT" , "HIGHEDNIS" , "GHoods" , "GRIME&GRIND" , " TIMELESSTREADS"]

                       #0           1            2                3           4            5                 6
print(clothing_brand)

# #Every list has an idex value / address
print(clothing_brand[2])
print(clothing_brand[2 : 5]) #List slicing

#Appending or adding item on the end of the list
clothing_brand.append("NIKE")
print(clothing_brand)
clothing_brand.append("SUPREME")
print(clothing_brand) 

#Inserts item at specific index
clothing_brand.insert(3, "DO'BE")
print(clothing_brand)

#Remove first occurence of item
clothing_brand.remove("HIGHMINDS")
print(clothing_brand)

#Remove and returns item at index
clothing_brand.pop()
print(clothing_brand)

#Return number of elements
print(len(clothing_brand))

#Sorts the lsit(ascending by default)
clothing_brand.sort()
print(clothing_brand)

#Revers the list order
clothing_brand.reverse()
print(clothing_brand)

# clothing_brand = clothing_brand = ["HIGHMINDS" , "MN+LA" , "DAILY FLIGHT" , "HIGHEDNIS" , "GHoods" , "GRIME&GRIND" , " TIMELESSTREADS"]
# clothing_brand.sort(reverse=True)
# print(clothing_brand)
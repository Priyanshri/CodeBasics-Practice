# from myModules import find_cylinder_volume, find_triangle_area

#this line imports the functions from myModules.py


# print(find_cylinder_volume(5, 10))

#this line is for the above import statement " from myModules import find_cylinder_volume, find_triangle_area"



import myModules #this imports the entire module

print(myModules.find_cylinder_volume(5, 10)) #this calls the function from the imported module

print(myModules.find_triangle_area(10, 15)) #this calls the function from the imported module
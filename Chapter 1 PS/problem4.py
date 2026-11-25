import os 

#Specify the Directory you want to list 
directory_path = '/Chapter 1 PS'

#List all files in the specified directory
contents = os.listdir(directory_path)

#Print each file and directory name 
for item in contents:
    print(item)
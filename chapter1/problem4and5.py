import os

#specify the directory you what to list
directory_path = '/quickchat'

#list all files and directories in the specified path
contents = os.listdir(directory_path)

#print each file and direxroey name
print(contents)
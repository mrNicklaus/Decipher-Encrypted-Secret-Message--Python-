import os

def rename_files():

    # file names from a folder
   file_list = os.listdir(r'C:\Users\Nick\Desktop\Secret_Message\secret_message')
   saved_path = os.getcwd()
   print ("Current working directory is " + saved_path)
   os.chdir(r'C:\Users\Nick\Desktop\Secret_Message\secret_message')
   for file_name in file_list:
       print ("Old Name -"+ file_name)
       print ("New Name -"+ file_name.translate(None,"0123456789"))
       os.rename(file_name,file_name.translate(None, "0123456789"))
   os.chdir(saved_path)
rename_files()








# Notes

# Python 2 .translate
# import string

# file_name = "48athens.jpg"

# res = file_name.translate(None,"0123456789")

# print (res)


# Python 3 .translate
# file_name = "48athens.jpg"

# trans_table = file_name.maketrans("None","None","0123456789")

# res = file_name.translate(trans_table)

# print (res)

# Documentation (Os documentation) 
# (https://docs.python.org/2/library/os.html)


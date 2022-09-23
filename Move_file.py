import os
import shutil



from_dir =  'C:/Users/Lenovo/Desktop/Source'
to_dir =  'C:/Users/Lenovo/Desktop/Desination'





list_of_files = os.listdir(from_dir)
#print(list_of_files)


for dir in list_of_files:
    key, extension = os.path.splitext(dir)
    print(extension)
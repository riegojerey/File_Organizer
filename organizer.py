import shutil, time, os
from holy_dik import path_extension

input_path = 'C:\\Users\\R. Terte\\Desktop\\Organizer'

for file_path in os.listdir(input_path):
    real_path = os.path.join(input_path, file_path)
    file_name, ext_name = os.path.splitext(real_path)
    if ext_name.lower() in path_extension:
        shutil.move(real_path, path_extension[ext_name])
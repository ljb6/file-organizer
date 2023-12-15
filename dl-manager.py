import os
import mimetypes
import shutil

directory = 'C:\\Users\\lucca\\Downloads'
desktop = 'C:\\Users\\lucca\\Desktop\\teste\\'

downloads = os.listdir(directory)

types = os.listdir(desktop)
for file in os.listdir(directory):
    file_directory = os.path.join(directory, file)

    mime, encoding = mimetypes.guess_type(file_directory)
    
    if mime:
      mime = mime.split('/')
      if mime[1] not in types:
        types.append(mime[1])
        os.makedirs(desktop + mime[1])

      shutil.copy(file_directory, desktop + mime[1])

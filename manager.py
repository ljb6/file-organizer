import os
import mimetypes
import shutil

def organize(DISORGANIZED_DIRECTORY, DESTINY_DIRECTORY):
  types = os.listdir(DESTINY_DIRECTORY)
  undefined_files = DESTINY_DIRECTORY + 'undefined-files'

  if not os.path.exists(undefined_files):
    os.makedirs(undefined_files)
  
  move_or_copy = 2

  for file in os.listdir(DISORGANIZED_DIRECTORY):
    file_directory = os.path.join(DISORGANIZED_DIRECTORY, file)

    mime, encoding = mimetypes.guess_type(file_directory)

    try:
      if mime:
        mime = mime.split('/')
        if mime[1] not in types:
          types.append(mime[1])
          os.makedirs(DESTINY_DIRECTORY + mime[1])

        if move_or_copy == 1:
          shutil.move(file_directory, DESTINY_DIRECTORY + mime[1])
        elif move_or_copy == 2:
          shutil.copy(file_directory, DESTINY_DIRECTORY + mime[1])

      else:
        shutil.copy(file_directory, DESTINY_DIRECTORY + 'undefined-files')

    except PermissionError:
      print('File:', file, 'has not permission to move')

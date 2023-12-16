import os
import mimetypes
import shutil

# Directories paths
DISORGANIZED_DIRECTORY = 'DOWNLOADS_DIRECTORY'
DESTINY_DIRECTORY = 'DESTINATION_FOLDER'

downloads = os.listdir(DISORGANIZED_DIRECTORY)
types = os.listdir(DESTINY_DIRECTORY)
undefined_files = DESTINY_DIRECTORY + 'undefined-files'

# Select type of usage
print('How do you want to manage your downloads?')
move_or_copy = int(input('1 - Move\n2 - Copy/paste\n> '))

if not os.path.exists(undefined_files):
    os.makedirs(undefined_files)

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

print('Done!')

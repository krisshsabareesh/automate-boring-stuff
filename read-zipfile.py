import zipfile,sys


def main():
  if len(sys.argv) == 2:
    try:
      read_file = zipfile.ZipFile(sys.argv[1])
      print(read_file.namelist())
      a_file_info = read_file.getinfo('example/myDogs.py')
      print(a_file_info.file_size)
      print(a_file_info.compress_size)
      print('Compressed file is %sx smaller!' %(round(a_file_info.file_size / a_file_info.compress_size, 2)))
      # read_file.extractall()                      #-uncomment(I am using this word as antonym for the word comment) to extract the zip file
      # read_file.extract('example/myDogs.py','.')  #- uncomment to extract the specified file
      read_file.close()
    except FileNotFoundError:
      print("File not found")
      print('Creating a new file with given name.....')
      #####---  UNCOMMENT BELOW COMMENTED SECTION TO CREATE A NEW ZIP FILE WITH GIVEN NAME ---#####
      #new_file = zipfile.ZipFile(sys.argv[1], 'w')
      #new_file.write('myDogs.py', compress_type=zipfile.ZIP_DEFLATED)
      #new_file.close()

if __name__ == '__main__':
  main()

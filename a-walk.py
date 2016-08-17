import os

def main():
  for foldername, subfolders, filenames in os.walk('.'):
    print('The current folder is ' + foldername)
    #----print subfolders below--------
    for subfolder in subfolders:
      print('SUBFOLDER OF %s : %s' % (foldername,subfolder))
    #----print files in the present folder below----------
    for filename in filenames:
      print('FILE INSIDE %s : %s' % (foldername,filename))

if __name__ == '__main__':
  main()

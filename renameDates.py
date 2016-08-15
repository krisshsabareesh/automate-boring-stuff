#! Python3
# renameDates.py - Renames Filenameswith American MM-DD-YYYY date format 
# to European DD-MM-YYYY.

import os,shutil,re

def main():
  datePattern = re.compile(r"""^(.*?) # all the text before date
  ((0|1)?\d)-                         # one or two digits for the month
  ((0|1|2|3)?\d)-                     # one or two digits for the day
  ((19|20)\d\d)                       # four digits for the year
  (.*?)$                              # all text after the date
  """, re.VERBOSE)
  for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
      continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart +afterPart
   
    #Now get the full abspath
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)

    #Rename the files
    print('Renaming "%s" to "%s"...' %(amerFilename,euroFilename))
    #shutil.move(ammerFilename, euroFilename)      #uncomment after testing

if __name__ == "__main__":
  main()

import re,commands,os

(status, output) = commands.getstatusoutput('ls *.txt')

if not status:
  search_string = raw_input('Enter a string/re to search through ".txt" files in the %s folder: ' %(os.path.abspath('.')))

  for filename in output.splitlines():
    f = open(filename)
    for line in f:
      tuple = re.findall(search_string,line.lower())
      if tuple: print line
    f.close()

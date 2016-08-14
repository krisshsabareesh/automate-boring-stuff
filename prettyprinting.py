import pprint
import shelve

shelfFile = shelve.open('mydata')
fileObj = open('myDogs.py','w')

fileObj.write('dogs = ' + pprint.pformat(shelfFile.values()) + '\n')
#print str(shelfFile.values())
fileObj.close()
shelfFile.close()

import myDogs

print myDogs.dogs


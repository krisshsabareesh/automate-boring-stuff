import shelve

shelfFile = shelve.open('mydata')
dogs = ['becky', 'ricky', 'jacky']
shelfFile['dogs'] = dogs
shelfFile.close()

shelfFile = shelve.open('mydata')
print shelfFile['dogs']
print shelfFile.keys()
print shelfFile.values()
shelfFile.close()

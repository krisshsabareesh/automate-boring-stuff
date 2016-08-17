import send2trash

beastFile = open('beast.txt','a')  #creates the file
beastFile.write('Beast is not vegetable.')
beastFile.close()

send2trash.send2trash('beast.txt')

import traceback,logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#logging.disable(logging.DEBUG)  #uncomment this to disable logging-levels(DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.debug('Start of program')

try:
  raise Exception('This is a error message')

except:
  errorFile = open('errorInfo.txt', 'w')
  errorFile.write(traceback.format_exc())
  errorFile.close()
  print("The traceback info was written to errorInfo.txt")


logging.debug('Starting switching lights')


#market_2nd = {'ns': 'green', 'ew': 'red'}  #this will generate an assertion error
market_2nd = {'ns': 'yellow', 'ew': 'red'}   #this will not generate assertion error

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)


logging.debug('Starting door status check')

doorStatus = 'open'
assert doorStatus == 'open', 'Need to be opened'

doorStatus = 'I am afraid, it not so...'         #generate assertion error
assert doorStatus == 'open', 'Need to be opened'


#call this program with -O option to the compiler to neglect all the assertion errors.

logging.debug('End of program')

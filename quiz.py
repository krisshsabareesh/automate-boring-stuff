import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

l = list(capitals)

for quizNo in xrange(35):
  random.shuffle(l)
  quizfile = open('capitalsquiz_%s.txt' % str(quizNo+1), 'w')
  answerfile = open('capitalsquiz_answers_%s.txt' % str(quizNo+1), 'w')
  quizstring = ' Name : \n Class: \n Period: \n \t\t\t Quiz Form' + str(quizNo+1) + '\n'
  ansstring = ''
  for i in range(len(l)):
    quizstring = quizstring + '\n' + str(i+1) + '. What is the capital of '+ l[i] + '\n'
    quizlist = []
    quizlist.append(capitals[l[i]])
    for j in xrange(3): 
      selection = random.randrange(len(l))
      quizlist.append(capitals[l[selection]])
    random.shuffle(quizlist)
    options = ['A', 'B', 'C', 'D']
    for option in range(4):
      quizstring = quizstring + '\t' + options[option]  +'. ' + quizlist[option] + '\n'
      if quizlist[option] == capitals[l[i]]:
        ansstring = ansstring + str(i+1) + '. ' + options[option] + '\n'
  quizfile.write(quizstring)
  answerfile.write(ansstring)
  quizfile.close()
  answerfile.close()

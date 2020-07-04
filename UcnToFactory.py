'''
Prereq: Take test keys from Usn list and put them into a .txt file with each key on new line
'''

file = open('/Users/bikramje/Downloads/list.txt', 'r').read().split('\n')
for test in file: # take each test key from the text file
    print('{"' + test + '"},') #. and convert it to factory format
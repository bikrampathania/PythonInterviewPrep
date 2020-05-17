'''
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'
'''

######################
#                    #
#     Solution 1     #            
#                    #
######################

def rev_sentence_1(sentence):
	return ' '.join(reversed(sentence.split()))

######################
#                    #
#     Solution 2     #            
#                    #
######################

def rev_sentence_2(sentence):
	return ' '.join(sentence.split()[::-1])


######################
#                    #
#     Solution 3     #            
#                    #
######################

def rev_sentence_3(sentence):

	words = []
	spaces = [' ']
	length = len(sentence)

	i = 0

	while i < length:
	    if sentence[i] not in spaces:
	        word_start = i

	        while i < length and s[i] not in spaces:
	        	i += 1

	        words.append(sentence[word_start: i])

	    i += 1

	return rev(words)

def rev(wordList):

    revList = []

    for word in wordList:
        revList = [word] + revList

#    return ' '.join(revList)

    rev_sent = ''

    for word in revList[:-1]:
    	rev_sent = rev_sent + str(word) + ' '

    return rev_sent + str(revList[-1])

'''
RUN THIS TO TEST THE SOLUTION
'''

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)

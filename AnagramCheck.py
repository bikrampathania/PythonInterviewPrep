'''
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
'''

def anagram(s, t):

	s = s.replace(' ', '').lower()
	t = t.replace(' '. '').lower()

	counter = {}

	for letter in s:
		if letter in counter:
			counter[letter] += 1
		else:
			counter[letter] = 1

	for letter in t:
		if letter in counter:
			counter[letter] -= 1
		else:
			counter[letter] = 1

	for k in counter:
		if counter[k] != 0:
			return False

	return True


'''
-> anagram('dog','god')
True

-> anagram('clint eastwood','old west action')
True

-> anagram('aa','bb')
False
'''
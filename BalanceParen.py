'''
Given a string of opening and closing parentheses, check whether it’s balanced.
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.

balance_check('[]')
True

balance_check('[](){([[[]]])}')
True

balance_check('()(){]}')
False
'''

def balance_paren_check(s):

	if len(s) % 2 != 0:
		return False

	chars = []
	matches = {')':'(', '}':'{', ']':'['}

	for c in s:
		if c in matches:
			if chars.pop() != matches[c]:
				return False
		else:
			chars.append(c)

	return chars == []
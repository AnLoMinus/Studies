#!/usr/bin/env python3
def ShowChars(num, token):
	return "\t" + (token * (num + 4))
			
def Show(message):
	xx = len(message)
	stars = ''
	if xx > 5:
		stars = ShowChars(xx, '$')
	else: 
	        stars = ShowChars(xx, '*')
	print(stars)
	print("\t* " + message + " *")
	print(stars)

Show("The is a MESSAGE")
Show("Doh!")


#!-*- coding: utf8 -*-
"""
 string2rule.py - Generates JtR rules from a string.
 Ver: 0.2 - May/2014

 Author: Daniel Marques (@0xc0da) - daniel _at_ codalabs _dot_ net
 http://codalabs.net

 Simple rule generator from user provided string. The script splits
 the string in chars, creates a string with the appropriate substitutions
 and outputs the generated rules (append and prepend such strings). 

 Substitutions are based on the 'Game of Hashes' research:
 http://codalabs.net/gameofhashes

 If the string codalabs is provided, the expected output is:

 [List.Rules:codalabs]
 A0"[cC(][oO0()][dD|)][aA4@][lL1][aA4@][bB8][sS5$]"
 Az"[cC(][oO0()][dD|)][aA4@][lL1][aA4@][bB8][sS5$]"

 This program is released as is and is not designed to be used to perform
 test against sites or infraestructures where the user do not have permission.
 Using this tool against others without authorization may breach end user
 license agreements. Use at your own discretion.
"""

import sys

substitutions = { # Character mapping. Seemed better than use translate().
	'a': 'aA4@',
	'b': 'bB8',
	'c': 'cC',
	'd': 'dD',
	'e': 'eE3&',
	'f': 'fFphPhPH',
	'g': 'gG9',
	'h': 'hH#',
	'i': 'iI1!',
	'j': 'jJ',
	'k': 'kK',
	'l': 'lL',
	'm': 'mM',
	'n': 'nN',
	'o': 'oO0',
	'p': 'pP',
	'q': 'qQ',
	'r': 'rR',
	's': 'sS5$',
	't': 'tT7',
	'u': 'uvUV',
	'v': 'vV',
	'w': 'wW',
	'x': 'xX',
	'y': 'yY',
	'z': 'zZ2',
	'0': 'oO0',
	'1': 'iI1!',
	'2': 'zZ2',
	'3': 'eE3&',
	'4': 'aA4@',
	'5': 'sS5$',
	'6': '6',
	'7': 'tT7',
	'8': 'bB8',
	'9': 'gG9',
	'!': 'iI1!',
	'@': 'aA4@',
	'#': 'hH#',
	'$': 'sS5$'	}

print '%s: Generates John the Ripper rules from a string.' % sys.argv[0]
print 'Created by Daniel C. Marques (@0xc0da) - http://codalabs.net\n'

if len(sys.argv) is not 2: 
	print "Usage: python %s <string>\n" % sys.argv[0]
else:
	print 'Just paste this in your JtR config file (usually john.conf):\n'
	print '[List.Rules:%s]' % sys.argv[1]
	print 'A0"%s"' % ''.join(['[%s]' % substitutions[char] for char in sys.argv[1].lower()])
	print 'Az"%s"' % ''.join(['[%s]' % substitutions[char] for char in sys.argv[1].lower()])
	print ''

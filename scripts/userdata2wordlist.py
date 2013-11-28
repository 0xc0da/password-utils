#!-*- coding: utf8 -*-
"""
 userdata2wordlist.py - Generates a wordlist from user data.

 The script uses user information (name, date of birth, etc) and generates
 a wordlist. Input file must be in the CSV format.
 
 Ver: 0.1 - 21/Oct/2013

 Daniel Marques - daniel _at_ codalabs _dot_ net
 http://codalabs.net

 Changelog
 v0.1 ~> Initial Release. 

"""

class wordlist(object):
	"""docstring for wordlist"""
	def __init__(self):
		self.wl = []
	def get_words(self):
		return self.wl
	def add_word(self, word):		
		if word not in self.wl:
			self.wl.append(word)
	def show_words(self):
		print "%s\n" % (word for word in self.wl)
	def generate(self,filename,mode):
		invalid_data = ["none","null","empty","vazio"]
		articles = ["da", "de", "do", "das", "dos"]
		suffixes = ["inho", "inha", "zinho", "zinha"]
		with open(filename,'r') as source_file:
			line_contents = []
			for line in source_file:
				line_contents = line.lower().split()
				if line_contents and line_contents not in invalid_data:
					if mode == 0:
						for content in line_contents:
							self.add_word(content)
					elif mode == 1:
						initials = []
						for content in line_contents:
							if content not in articles:
								initials.append(content[0])
						self.add_word("".join(initials))
					elif mode == 2:
						first3chars = []
						content = line_contents[0] 
						first3chars.append(content[:3])
						self.add_word("".join(first3chars))
					elif mode == 3:
						first4chars = []
						content = line_contents[0]
						first4chars.append(content[:4])
						self.add_word("".join(first4chars))
					else:
						print "Invalid mode."				
	def tofile(self,filename):
		fh = open(filename, 'w')
		fh.writelines("%s\n" % word for word in self.wl)
		fh.close()

import os
import sys

if not os.path.exists("output"):
	os.makedirs("output")

arquivo = "teste.txt"
wl_file = "/tmp/wl.txt"

wl = wordlist()
wl.generate(arquivo,3)
wl.tofile(wl_file)




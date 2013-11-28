#!-*- coding: utf8 -*-
"""
 mergehash.py - Merges .pot files with .csv files (e.g: sqlmap dumps)
 
 Versao: 0.1 - 20/Ago/2013

 Daniel Marques - daniel _at_ codalabs _dot_ net
 http://codalabs.net


** Files MUST be in the following format:

 [*] CSV : Username, hash
 [*] pot : Hash, password (default) 


 Changelog
 v0.1 ~> Initial Release. 

"""

import csv
import sys

def file2list(filename,delimiter):
	""" Reads a file to a list. """

	output_list = []

	with open(filename, 'r') as input_file:	
		for line in input_file:
			output_list.append(line.rstrip("\n").split(delimiter))

	return output_list

def merge_files(csv_file,pot_file):
	""" Merges the CSV with username and hash with the pot file. """
	#user_hash = file2list(csv_file,",")
	#hash_pass = file2list(pot_file,":")

	merged = []

	for found_hash,found_password in pot_file:		

		for username,password_hash in [user for user in csv_file
                                       if found_hash in user]:

			user_data = {'username':"",'hash':"",'password':""}
			user_data['username'] = username
			user_data['hash'] = password_hash
			user_data['password'] = found_password

			merged.append(user_data)
			
	return merged

def write2file(filename,field_delimiter,output_list):
	""" Writes the output to a file. """
	output_file = open(filename,"wt")

	writer = csv.DictWriter(output_file,fieldnames=["username","hash","password"],
		                    delimiter=field_delimiter)

	writer.writeheader()

	for data in output_list:
		writer.writerow(data)

print "%s: Merges username-hash CSV files with .pot files.\n" % (sys.argv[0])

if len(sys.argv) is not 4:
	print "Usage: %s <username-hash csv file> <pot file> <output file>\n"
	sys.exit(1)

csv_file = file2list(sys.argv[1],",")
pot_file = file2list(sys.argv[2],":")

output = merge_files(csv_file, pot_file)

write2file(sys.argv[3],",",output)

print "Done."



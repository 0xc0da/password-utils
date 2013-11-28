# -*- coding: latin-1 -*-
#
from unicodedata import normalize

def remover_acentos(palavra, codif='latin-1'):
	palavra_temp=unicode(palavra,'ASCII')
	#return normalize('NFKD', palavra.decode(codif).encode('ASCII', 'ignore'))
	return normalize('NFKD', palavra_temp)

with open("pt_BR.dic") as fh:
	palavra = fh.readline()
	while palavra:
		palavra_sem_acento = remover_acentos(palavra)
		print palavra_sem_acento
		palavra = fh.readline()
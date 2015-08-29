# Author: Denny K. Schuldt
# Operative Systems.

import sys

def main():
	data = sys.argv[1]
	politic = sys.argv[2]
	size = sys.argv[3]
	print '\n\tEvaluando una cache',politic,'con',size,'entradas.\n'
	if politic == 'LRU':
		print '#TO-DO'
	elif politic == 'OPTIMO':
		print '#TO-DO'
	elif politic == 'CLOCK':
		print '#TO-DO'

main()

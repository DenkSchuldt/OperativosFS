# Author: Denny K. Schuldt
# Operative Systems.

import sys
import collections


def LRU(workload, capacity):
	misses = 0
	warmMisses = 0
	references = 0
	centinel = True
	capacity = int(capacity)
	cache = collections.OrderedDict()
	with open(workload) as obj:
		for line in obj:
			references += 1
			try:
				cache.pop(line)
			except KeyError:
				misses += 1
				if len(cache) >= capacity:
					warmMisses += 1
					cache.popitem(last=False)
			cache[line] = 1
	results(misses, warmMisses, references, capacity)


def results(misses, warmMisses, references, capacity):
	missRate = (float(misses)/float(references))*100
	warmMissRate = (float(warmMisses)/float(references-capacity))*100
	misses = str(misses)
	warmMisses = str(warmMisses)
	references = str(references)
	capacity = str(capacity)
	print "Resultados:"
	print "\tMiss rate:               " + format(missRate,'.2f') + "% (" + misses, "out of", references, "references)"
	print "\tMiss rate: (warm cache): " + format(warmMissRate,'.2f') + "% (" + warmMisses, "out of", references + "-" + capacity, "references)"


def main():
	workload = sys.argv[1]
	politic = sys.argv[2]
	capacity = sys.argv[3]
	print '\nEvaluando una cache',politic,'con',capacity,'entradas.'
	if politic == 'LRU':
		LRU(workload, capacity)
	elif politic == 'OPTIMO':
		print '#TO-DO'
	elif politic == 'CLOCK':
		print '#TO-DO'
		'''from itertools import cycle
		cache = cycle(cache)
		for item in ref:
			if next(cache)[0] == item:'''


main()

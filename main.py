#!/usr/bin/env python
# main.py: Operative Systems, final project.

__author__  = "Denny K. Schuldt"
__version__ = "1.0.0"
__email__   = "dschuldt@espol.edu.ec"

import sys
import collections


def LRU(workload, capacity):
	misses = 0
	warmMisses = 0
	references = 0
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


def OPTIMO(workload, capacity):
	misses = 0
	warmMisses = 0
	references = 0
	capacity = int(capacity)
	cache = set()
	with open(workload) as f:
		references = f.read().splitlines()
	for index, element in enumerate(references):
		if element not in cache:
			if len(cache) >= capacity:
				warmMisses += 1
				candidates = collections.OrderedDict()
				for item in references[index:index+capacity]:
					try:
						candidates.pop(item)
					except:
						pass
					candidates[item] = 1
				while candidates:
					k, v = candidates.popitem()
					if k in cache:
						cache.remove(k)
						break
			misses += 1
		cache.add(element)
	results(misses, warmMisses, len(references), capacity)


def MRU(workload, capacity):
	misses = 0
	warmMisses = 0
	references = 0
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
					cache.popitem()
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
	print "\tMiss rate: (warm cache): " + format(warmMissRate,'.2f') + "% (" + warmMisses, "out of", references + "-" + capacity, "references)\n"


def main():
	workload = sys.argv[1]
	politic = sys.argv[2]
	capacity = sys.argv[3]
	print '\nEvaluando una cache',politic,'con',capacity,'entradas.'
	if politic == 'LRU':
		LRU(workload, capacity)
	if politic == 'MRU':
		MRU(workload, capacity)
	elif politic == 'OPTIMO':
		OPTIMO(workload, capacity)


main()
